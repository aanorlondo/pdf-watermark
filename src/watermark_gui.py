from misc import (
    APP_NAME,
    FONT_SIZE,
    FONT_STYLE,
    CONFIG_FILE,
    APP_INFO_GUI,
    GUI_ICON_PATH,
    TEMPLATE_FILE,
    DEFAULT_INPUT_DIR,
    DEFAULT_OUTPUT_DIR,
    AVAILABLE_POSITIONS,
    DEFAULT_WATERMARK_GUI,
)
from watermark_cli import WatermarkConfig, WatermarkApp
import sys, json, traceback, os

from PyQt6.QtWidgets import (
    QApplication,
    QColorDialog,
    QMainWindow,
    QFileDialog,
    QPushButton,
    QHBoxLayout,
    QMessageBox,
    QVBoxLayout,
    QComboBox,
    QTextEdit,
    QWidget,
    QFrame,
    QLabel,
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QPixmap, QColor


###########
# GUI APP #
###########
class PdfWatermarkApp(QMainWindow):
    # ------#
    # INIT #
    # ------#
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle(f"{APP_NAME} (GUI)")
        self.setGeometry(100, 100, 400, 450)

        self.watermark_config = WatermarkConfig()
        self.watermark_config_text = json.dumps(
            self.watermark_config.load_config(), indent=4
        )
        self.input_path = DEFAULT_INPUT_DIR
        self.output_path = DEFAULT_OUTPUT_DIR
        self.text_input = DEFAULT_WATERMARK_GUI
        self.watermark_template = DEFAULT_WATERMARK_GUI
        self.create_widgets()

    # --------#
    # WIDGETS #
    # --------#
    def add_separator(self, layout) -> None:
        """
        Add a horizontal line separator to the layout.
        """
        line = QFrame(self)
        line.setFrameShape(QFrame.Shape.HLine)
        line.setFrameShadow(QFrame.Shadow.Sunken)
        layout.addWidget(line)

    def create_widgets(self) -> None:
        """
        Create and arrange all the widgets in the main application window.
        """
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        central_widget.setLayout(layout)

        # INPUT DIRECTORY
        # ____________
        input_label = QLabel("Choose an Input Directory", self)
        input_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        input_label.setStyleSheet(FONT_STYLE)
        layout.addWidget(input_label)

        input_button = QPushButton("Browse", self)
        input_button.clicked.connect(self.browse_input)
        layout.addWidget(input_button)

        self.input_path_label = QLabel(self.input_path, self)
        self.input_path_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.input_path_label.setStyleSheet(FONT_SIZE)
        layout.addWidget(self.input_path_label)

        self.add_separator(layout)

        # OUTPUT DIRECTORY
        # ____________
        output_label = QLabel("Choose an Output Directory", self)
        output_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        output_label.setStyleSheet(FONT_STYLE)
        layout.addWidget(output_label)

        output_button = QPushButton("Browse", self)
        output_button.clicked.connect(self.browse_output)
        layout.addWidget(output_button)

        self.output_path_label = QLabel(self.output_path, self)
        self.output_path_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.output_path_label.setStyleSheet(FONT_SIZE)
        layout.addWidget(self.output_path_label)

        self.add_separator(layout)

        # WATERMARK TEXT
        # ____________
        text_label = QLabel("Enter your Text", self)
        text_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        text_label.setStyleSheet(FONT_STYLE)
        layout.addWidget(text_label)

        self.text_entry = QTextEdit(self)
        self.text_entry.setFixedWidth(380)
        self.text_entry.setFixedHeight(110)
        self.text_entry.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.text_entry)
        self.text_entry.setText(self.text_input)

        # WATERMARK: LOAD DEFAULT AND SAVE AS DEFAULT BUTTONS
        # _______
        wm_button_layout = QHBoxLayout()

        wm_save_button = QPushButton("Save as Template", self)
        wm_save_button.clicked.connect(self.save_template)
        wm_button_layout.addWidget(wm_save_button)

        wm_load_default = QPushButton("Load Default", self)
        wm_load_default.clicked.connect(self.load_template)
        wm_button_layout.addWidget(wm_load_default)

        layout.addLayout(wm_button_layout)

        self.add_separator(layout)

        # ADAPT CONFIG
        # ____________
        config_label = QLabel("Configuration", self)
        config_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        config_label.setStyleSheet(FONT_STYLE)
        layout.addWidget(config_label)

        self.config_entry = QTextEdit(self)
        self.config_entry.setFixedWidth(380)
        self.config_entry.setFixedHeight(140)
        self.config_entry.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.config_entry)
        self.config_entry.setText(self.watermark_config_text)

        # CONFIG : LOAD DEFAULT AND SAVE AS DEFAULT BUTTONS
        # ____________
        cf_button_layout = QHBoxLayout()

        cf_save_default = QPushButton("Save as Default", self)
        cf_save_default.clicked.connect(self.save_default_config)
        cf_button_layout.addWidget(cf_save_default)

        cf_load_default = QPushButton("Load Default", self)
        cf_load_default.clicked.connect(self.load_default_config)
        cf_button_layout.addWidget(cf_load_default)

        layout.addLayout(cf_button_layout)

        # CONFIRM
        # ____________
        process_button = QPushButton("Apply Watermark", self)
        process_button.clicked.connect(self.process)
        layout.addWidget(process_button)

        # APP INFO
        # ____________
        info_button = QPushButton(self)
        info_button.setIcon(QIcon(GUI_ICON_PATH))
        info_button.setGeometry(self.width() - 40, 10, 30, 30)
        info_button.clicked.connect(self.show_app_info)

        # COLOR PICKER
        # ________
        color_button = QPushButton("Color", self)
        color_button.setGeometry(self.width() - 54, 412, 44, 30)
        color_button.clicked.connect(self.show_color_dialog)

        # POSITIONS DROP_DOWN
        # ______
        self.dropdown = QComboBox(self)
        self.dropdown.addItem("Position")
        for item in AVAILABLE_POSITIONS:
            self.dropdown.addItem(item)
        self.dropdown.setGeometry(248, 414, 100, 30)
        self.dropdown.currentIndexChanged.connect(self.on_dropdown_selection)

    # ----------------#
    # BUTTON HANDLERS #
    # ----------------#

    # INPUT AND OUTPUT DIR PATHS
    # _______
    def browse_input(self) -> None:
        """
        Open a dialog to select the input directory.
        """
        self.input_path = QFileDialog.getExistingDirectory(
            self, "Choose an Input Directory"
        )
        self.input_path_label.setText(self.input_path)

    def browse_output(self) -> None:
        """
        Open a dialog to select the output directory.
        """
        self.output_path = QFileDialog.getExistingDirectory(
            self, "Choose an Output Directory"
        )
        self.output_path_label.setText(self.output_path)

    # SHOW APP INFO
    # ________
    def show_app_info(self) -> None:
        self.show_info(message=APP_INFO_GUI)

    # LOAD AND SAVE CONFIG
    # _____
    def load_default_config(self) -> None:
        """
        Load the default watermark configuration.
        """
        self.config_entry.setText(
            json.dumps(self.watermark_config.load_config(), indent=4)
        )

    def save_default_config(self) -> None:
        """
        Save the current configuration as the default watermark configuration.
        """
        config_text = self.config_entry.toPlainText()
        try:
            config_dict = json.loads(config_text)
            with open(CONFIG_FILE, "w") as f:
                json.dump(config_dict, f)
                f.close()
            self.show_info(message="Configuration saved as default.")
        except Exception as e:
            self.show_error(message="Failed to save configuration as default.")
            print(f"Error saving configuration: {e}")
            return

    # COLOR PICKER
    # ________
    def show_color_dialog(self) -> None:
        """
        Pick a color and get its hex code
        """
        color_dialog = QColorDialog(self)
        color = color_dialog.getColor()

        if color.isValid():
            hex_code = color.name(QColor.NameFormat.HexRgb)
            config_text = self.config_entry.toPlainText()
            try:
                config_dict = json.loads(config_text)
                config_dict["color"] = hex_code
                config_text = json.dumps(config_dict, indent=4)
                self.config_entry.setText(config_text)
            except Exception as e:
                self.show_error(
                    message="Failed to load the color code to your configuration. Add it manually or reload configuration default and try again."
                )
                print(f"Error setting the color code: {e}")
                traceback.print_exc()
                return

    # POSITION PICKER
    # ______
    def on_dropdown_selection(self, index) -> None:
        position = self.dropdown.itemText(index)
        if position in AVAILABLE_POSITIONS:
            config_text = self.config_entry.toPlainText()
            try:
                config_dict = json.loads(config_text)
                config_dict["position"] = position
                config_text = json.dumps(config_dict, indent=4)
                self.config_entry.setText(config_text)
            except Exception as e:
                self.show_error(
                    message="Failed to load the position to your configuration. Add it manually or reload configuration default and try again."
                )
                print(f"Error setting the position code: {e}")
                traceback.print_exc()
                return

    # LOAD AND SAVE TEMPLATE
    # ______
    def load_template(self) -> None:
        self.text_entry.setText(self.watermark_template)

    def save_template(self) -> None:
        try:
            text = self.text_entry.toPlainText()
            if text.strip() == "":
                self.show_error(message="Watermark text cannot be empty.")
                return
            if not os.path.exists(TEMPLATE_FILE):
                os.makedirs(TEMPLATE_FILE)
            with open(TEMPLATE_FILE, "w") as f:
                f.write(text)
                f.close()
            self.watermark_template = text

            self.show_info(message="Succesfully saved text as template.")

        except Exception as e:
            self.show_error(message="Failed to save template")
            print(f"Error saving template text: {e}")
            return

    # ------------#
    # MESSAGE BOX #
    # ------------#
    def show_error(self, message) -> None:
        QMessageBox.critical(self, "Error", message, QMessageBox.StandardButton.Ok)

    def show_info(self, message) -> None:
        box = QMessageBox(self)
        box.setIconPixmap(QPixmap(GUI_ICON_PATH))
        box.setStyleSheet(FONT_SIZE)
        box.setText(message)
        box.exec()

    # -----#
    # CORE #
    # -----#
    def process(self) -> None:
        """
        Process the watermark operation.
        """
        # Check different paths (to avoid loops)
        # ____________
        if self.input_path == self.output_path:
            self.show_error(message="Input and Output directories must be different.")
            return

        # Check non empty watermark
        # ____________
        watermark_text = self.text_entry.toPlainText()
        if watermark_text.strip() == "":
            self.show_error(message="Watermark text cannot be empty.")
            return

        # Check valid configuration
        # ____________
        config_text = self.config_entry.toPlainText()
        try:
            config_dict = json.loads(config_text)
        except Exception as e:
            self.show_error(message="Your configuration is invalid.")
            print(f"Error parsing configuration: {e}")
            return

        print("--Input Path:", self.input_path)
        print("--Output Path:", self.output_path)
        print("--Configuration:", config_dict)

        # Apply Watermark
        # ____________
        class EmptyDirectory(Exception):
            pass

        try:
            self.watermark_config.update_config(config=config_dict)
            watermark_app = WatermarkApp(self.watermark_config)
            processed_count = watermark_app.apply_watermark_to_all_pdfs(
                input_directory=self.input_path,
                output_directory=self.output_path,
                watermark_text=watermark_text,
            )

            if processed_count is None:
                raise EmptyDirectory(
                    "No PDF files found in the given input directory. Try another !"
                )

            self.show_info(message=f"Succesfully processed {processed_count} files.")
            print(f"--Succesfully processed {processed_count} files.")

        except EmptyDirectory as e:
            self.show_error(message=str(e))
        except Exception as e:
            self.show_error(message=f"Something went wrong: {e}")
            print(f"ERROR: Something went wrong. Cause: {e}\n_________")
            traceback.print_exc()
            return


# RUN THE GUI
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(GUI_ICON_PATH))
    window = PdfWatermarkApp()
    window.show()
    sys.exit(app.exec())
