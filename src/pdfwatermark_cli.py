# RUNNING STANDALONE CLI
# _______________________
import argparse
import pyfiglet
import traceback
from misc import (
    APP_NAME,
    APP_VERSION,
    CONFIG_FILE,
    APP_INFO_CLI,
    DEFAULT_INPUT_DIR,
    DEFAULT_OUTPUT_DIR,
    DEFAULT_WATERMARK_CLI,
)
from pdfwatermark_core import WatermarkConfig, WatermarkApp


if __name__ == "__main__":
    # Define parser
    parser = argparse.ArgumentParser(
        description=f"{APP_NAME} (CLI)",
        epilog=f"App version: {APP_VERSION}",
        formatter_class=argparse.RawTextHelpFormatter,
    )

    # Core args
    parser.add_argument(
        "--input_dir",
        type=str,
        help="Input directory path for the PDF files",
        default=DEFAULT_INPUT_DIR,
    )
    parser.add_argument(
        "--output_dir",
        type=str,
        help="Output directory path for the watermarked PDF files",
        default=DEFAULT_OUTPUT_DIR,
    )
    parser.add_argument(
        "--text",
        type=str,
        help="Text to be used as watermark",
        default=DEFAULT_WATERMARK_CLI,
    )

    parser.add_argument(
        "--config",
        type=str,
        help=f"Custom config file path to use. Default: {CONFIG_FILE}.",
        default=CONFIG_FILE,
    )

    # Version and app info
    # FONT options: 'standard', 'big', 'slant', 'block', 'small', '3-d', '5lineoblique', 'digital'
    ASCII_FONT = "small"
    parser.add_argument(
        "--version",
        action="version",
        version=f"{pyfiglet.figlet_format(APP_NAME, font=ASCII_FONT)}{APP_INFO_CLI}",
        help="Show App version and information",
    )

    # Read values
    args = parser.parse_args()
    input_directory = args.input_dir
    output_directory = args.output_dir
    watermark_text = args.text
    custom_config = args.config

    # Check directories
    if input_directory == output_directory:
        print("Input and Output directories must be different.")
        exit(1)

    # Check text
    if watermark_text.strip() == "":
        print("Watermark text cannot be empty.")
        exit(1)

    # Run app
    try:
        # Config app
        config = WatermarkConfig(config_file=custom_config)
        watermark = WatermarkApp(config)

        # Exit if no PDF files found
        if not watermark.found_pdf_files(dir_path=input_directory):
            print("No PDF files found in the input directory.")
            exit(1)

        processed_count = watermark.apply_watermark_to_all_pdfs(
            input_directory=input_directory,
            output_directory=output_directory,
            watermark_text=watermark_text,
        )
        print(f"--Succesfully processed {processed_count} files.")
    except Exception as e:
        print(f"ERROR: Something went wrong. Cause: {e}\n_____________")
        traceback.print_exc()
