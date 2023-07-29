from os.path import dirname, abspath, join, exists

# GLOBAL
# ________
CURRENT_DIR = dirname(abspath(__file__))
DEFAULT_OUTPUT_DIR = join(CURRENT_DIR, "test", "output")
DEFAULT_INPUT_DIR = join(CURRENT_DIR, "test", "input")
CONFIG_FILE = join(CURRENT_DIR, "config.json")
TEMPLATE_FILE = join(CURRENT_DIR, "template.txt")

# GUI
# _____
GUI_ICON_PATH = join(CURRENT_DIR, "watermark.ico")
FONT_STYLE = "font: italic bold;"
FONT_SIZE = "font-size: 10px;"


# CORE
# _____
TMP_WATERMARK = join(CURRENT_DIR, "tmp_watermark.pdf")
DEFAULT_CONFIG = {
    "size": 15,
    "font": "Helvetica",
    "color": "#FF0000",
    "position": "center",
    "angle": 0,
    "alpha": 0.8,
}
AVAILABLE_POSITIONS = [
    "top",
    "bottom",
    "left",
    "right",
    "center",
    "top-left",
    "top-right",
    "bottom-left",
    "bottom-right",
]

# TEMPLATE
# _____
DEFAULT_WATERMARK_GUI = "Type down your Watermark text here"
DEFAULT_WATERMARK_CLI = "TESTING CLI STANDALONE"


if exists(TEMPLATE_FILE):
    with open(TEMPLATE_FILE, "r") as f:
        TEMPLATE_TEXT = f.read()
        f.close()
    if TEMPLATE_TEXT.strip() != "":
        DEFAULT_WATERMARK_CLI = TEMPLATE_TEXT
        DEFAULT_WATERMARK_GUI = TEMPLATE_TEXT


# VERSION
# _____
VERSION_FILE = join(CURRENT_DIR, "..", "VERSION")


def read_version_file() -> str:
    try:
        with open(VERSION_FILE, "r") as version_file:
            version = version_file.read().strip()
            version_file.close()
            return version
    except FileNotFoundError:
        return "N/A"


APP_VERSION = read_version_file()


# INFO
# _____
APP_PITCH = "A Home-Made app to Watermark your documents!"
APP_NAME = "PDF Watermark"
APP_INFO_GUI = """
{}
Version: {}\n\n \
{} \n\n \
CLI version:\n \
python waterkmark_cli.py --help\n\n \
Copyright © Khaled KHEBBEB \
https://github.com/aanorlondo \n\n \
2023
""".format(
    APP_NAME, APP_VERSION, APP_PITCH
)

APP_INFO_CLI = """                          ---
    ╭───────────────────────────────────────────────╮
    │  {} │
    │                Version: {}                 |
    |                                               |
    | Try the GUI version: `python watermark_gui.py`|
    │                                               |
    │          Copyright © Khaled KHEBBEB           |
    │     GitHub: https://github.com/aanorlondo     |
    │                     2023                      |
    ╰───────────────────────────────────────────────╯
""".format(
    APP_PITCH, APP_VERSION
)
