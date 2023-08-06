from misc import (
    CONFIG_FILE,
    TMP_WATERMARK,
    DEFAULT_CONFIG,
)
from PyPDF2 import PdfReader, PdfWriter
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
import json, os


class WatermarkConfig:
    def __init__(self, config_file=CONFIG_FILE) -> None:
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self) -> dict:
        try:
            with open(self.config_file, "r") as f:
                config = json.load(f)
                f.close()
                return config
        except Exception as e:
            print(f"Error reading configuration: {e}\nUsing default config.")
            return DEFAULT_CONFIG

    def update_config(self, config: dict) -> None:
        try:
            self.config = config
        except Exception as e:
            print(f"Error updating configuration: {e}\nUsing default file.")
            self.config = self.load_config()

    def get_text_size(self) -> int:
        return self.config.get("size", DEFAULT_CONFIG["size"])

    def get_font(self) -> str:
        return self.config.get("font", DEFAULT_CONFIG["font"])

    def get_color(self) -> str:
        return self.config.get("color", DEFAULT_CONFIG["color"])

    def get_position(self) -> str:
        return self.config.get("position", DEFAULT_CONFIG["position"])

    def get_angle(self) -> int:
        return self.config.get("angle", DEFAULT_CONFIG["angle"])

    def get_alpha(self) -> float:
        return self.config.get("alpha", DEFAULT_CONFIG["alpha"])


class WatermarkApp:
    def __init__(self, config: WatermarkConfig) -> None:
        self.config = config

    def calculate_position(
        self, position, page_width, page_height, text_size, canvas, font, lines
    ) -> tuple:
        """
        Calculate the x, y coordinates for the watermark text based on the specified position setting.

        Parameters:
            position (str): Watermark position setting ("center", "top", "bottom", "left", or "right").
            page_width (float): Width of the page in points (1 inch = 72 points).
            page_height (float): Height of the page in points (1 inch = 72 points).
            text_size (int): Font size of the text.
            canvas (obj): PDF canvas used to print the Watermark.
            font (str): Name of the font used to draw the Watermark.
            lines (list): List of the lines contained in the Watermark text.

        Returns:
            Tuple (x, y) with the calculated coordinates for the watermark text.
        """

        # Get Height = nb_lines x font_size
        nb_lines = len(lines)
        text_height = nb_lines * text_size

        # Get Width = longest_line x font_size % font_name
        longest_line = ""
        for line in lines:
            if len(line) > len(longest_line):
                longest_line = line
        text_width = canvas.stringWidth(
            text=longest_line,
            fontName=font,
            fontSize=text_size,
        )

        # Coordinates calculation
        # _______
        margin = 10
        x_center = ((page_width - text_width) / 2) + (text_width / 2)
        y_center = page_height / 2
        y_top = (page_height * 0.9) + margin
        y_bottom = text_height + margin
        x_left = (text_width / 2) + margin
        x_right = page_width - (text_width / 2) - margin

        # Positions Settings
        # _____
        position_settings = {
            "top": (x_center, y_top),
            "bottom": (x_center, y_bottom),
            "left": (x_left, y_center),
            "right": (x_right, y_center),
            "center": (x_center, y_center),
            "top-left": (x_left, y_top),
            "top-right": (x_right, y_top),
            "bottom-left": (x_left, y_bottom),
            "bottom-right": (x_right, y_bottom),
        }
        # Return specified position (center if not found)
        return position_settings.get(position, position_settings["center"])

    def add_watermark_to_pdf(self, input_path, output_path, watermark_text) -> None:
        # Save Watermark config
        text_size = self.config.get_text_size()
        position = self.config.get_position()
        color = self.config.get_color()
        angle = self.config.get_angle()
        font = self.config.get_font()
        alpha = self.config.get_alpha()
        width, height = A4

        # Create the watermark canvas with configurable settings
        watermark_canvas = canvas.Canvas(TMP_WATERMARK, pagesize=A4)
        watermark_canvas.setFillColor(
            aColor=colors.HexColor(color),
            alpha=alpha,
        )
        watermark_canvas.setFont(font, text_size)

        # Break the text to lines then write each line separately
        lines = watermark_text.split("\n")

        # Get coordinates
        x, y = self.calculate_position(
            position=position,
            page_width=width,
            page_height=height,
            text_size=text_size,
            canvas=watermark_canvas,
            font=font,
            lines=lines,
        )

        # Prepare Watermark Canvas
        for line in lines:
            watermark_canvas.drawCentredString(x=x, y=y, text=line)
            y -= text_size
        watermark_canvas.rotate(theta=angle)
        watermark_canvas.save()
        output_pdf = PdfWriter()

        # Read each page of the input PDF, add the watermark, and save it to the output PDF
        input_pdf = PdfReader(input_path)
        num_pages = len(input_pdf.pages)
        for page_num in range(num_pages):
            page = input_pdf.pages[page_num]
            watermark_pdf = PdfReader(TMP_WATERMARK)
            page.merge_page(watermark_pdf.pages[0])
            output_pdf.add_page(page)

        # Save the output PDF with the "_tagged" suffix in the output directory
        output_file_path = os.path.join(
            output_path,
            os.path.basename(input_path).replace(
                ".pdf",
                f"_marked_{position}_{text_size}.pdf",
            ),
        )
        with open(output_file_path, "wb") as output_file:
            output_pdf.write(output_file)
            output_file.close()
        os.remove(TMP_WATERMARK)

    def found_pdf_files(self, dir_path: str) -> bool:
        """
        Check the presence of PDF files in given directory
        """
        files_list = os.listdir(dir_path)
        for filename in files_list:
            if filename.lower().endswith(".pdf"):
                return True
        return False

    def count_pdf_files(self, dir_path: str) -> int:
        """
        Count the number of PDF files found in the given directory
        """
        count = 0
        files_list = os.listdir(dir_path)
        for filename in files_list:
            if filename.lower().endswith(".pdf"):
                count += 1
        return count

    def apply_watermark_to_all_pdfs(
        self, input_directory, output_directory, watermark_text
    ) -> int:
        """
        Apply watermark text to every page of every PDF file in the input directory
        and save the resulting PDFs in the output directory.

        Parameters:
            input_directory (str): Path to the input directory containing PDF files.
            output_directory (str): Path to the output directory where the resulting PDFs will be saved.
            watermark_text (str): Text to be used as the watermark.

        Returns:
            The number of succesfully processed PDF documents
        """

        # Create the Output dir if needed
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        print(f"--Input dir: {input_directory}")
        print(f"--Output dir: {output_directory}")
        print(f"--Configuration: {self.config.config}")
        print(f'--Applying watermark text: \n"{watermark_text}"\n')

        # Loop over the PDF files
        files_list = os.listdir(input_directory)
        processed_count = 0
        for filename in files_list:
            if filename.lower().endswith(".pdf"):
                input_path = os.path.join(input_directory, filename)
                self.add_watermark_to_pdf(
                    input_path=input_path,
                    output_path=output_directory,
                    watermark_text=watermark_text,
                )
                processed_count += 1
        return processed_count
