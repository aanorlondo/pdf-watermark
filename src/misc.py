from os.path import dirname, abspath, join, exists
from os import environ
import sys

# GLOBAL
# ________
HOME_DIR = environ["HOME"]
DOWNLOADS_DIR = "Downloads"
APPDATA_DIR = "appdata"

# ROOT
# _____
CURRENT_DIR = "UNDEFINED"
FROZEN = getattr(sys, "frozen", "")
if not FROZEN:
    # not frozen: in regular python interpreter
    CURRENT_DIR = dirname(abspath(__file__))
    DEFAULT_INPUT_DIR = join(CURRENT_DIR, "..", "test", "input")
    DEFAULT_OUTPUT_DIR = join(CURRENT_DIR, "..", "test", "output")

elif FROZEN in ("macosx_app",):
    # py2app
    CURRENT_DIR = environ["RESOURCEPATH"]
    DEFAULT_INPUT_DIR = join(HOME_DIR, DOWNLOADS_DIR, "input")
    DEFAULT_OUTPUT_DIR = join(HOME_DIR, DOWNLOADS_DIR, "output")


# APP DATA
# ________
VERSION_FILE = join(CURRENT_DIR, APPDATA_DIR, "VERSION.txt")
CONFIG_FILE = join(CURRENT_DIR, APPDATA_DIR, "config.json")
TEMPLATE_FILE = join(CURRENT_DIR, APPDATA_DIR, "template.txt")

# GUI
# _____
GUI_ICON_PATH = join(CURRENT_DIR, APPDATA_DIR, "pdfwatermark.ico")
FONTUP_ICON_PATH = join(CURRENT_DIR, APPDATA_DIR, "fontup.png")
FONTDOWN_ICON_PATH = join(CURRENT_DIR, APPDATA_DIR, "fontdown.png")
COLOR_ICON_PATH = join(CURRENT_DIR, APPDATA_DIR, "color.png")
FONT_STYLE = "font: italic bold;"
FONT_SIZE = "font-size: 10px;"


# CORE
# _____
TMP_WATERMARK = join(CURRENT_DIR, "tmp_watermark.pdf")
DEFAULT_CONFIG = {
    "size": 15,
    "font": "Courier",
    "color": "#FF0000",
    "position": "center",
    "angle": 0,
    "alpha": 0.8,
}

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
