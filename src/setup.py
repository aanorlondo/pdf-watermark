from setuptools import setup
from glob import glob

# APP DATA
# _________
APP = ["watermark_gui.py"]
APP_NAME = "PdfWatermark"
DATA_DIRNAME = "appdata"
VERSIONFILE = "VERSION.txt"
DATA_FILES = [
    (str(DATA_DIRNAME), glob(f"{DATA_DIRNAME}/*.*")),
]


# APP VERSION
# _________
def get_version():
    v = open(f"{DATA_DIRNAME}/{VERSIONFILE}")
    version = v.read()
    v.close()
    return version


VERSION = get_version()


# BUILD OPTIONS
# _________
OPTIONS = {
    "argv_emulation": True,
    "iconfile": f"{DATA_DIRNAME}/watermark.ico",
    "plist": {
        "CFBundleName": APP_NAME,
        "CFBundleDisplayName": APP_NAME,
        "CFBundleGetInfoString": f"{APP_NAME}",
        "CFBundleIdentifier": "com.aanorlondo.osx.pdfwatermark",
        "CFBundleVersion": f"{VERSION}",
        "CFBundleShortVersionString": f"{VERSION}",
        "NSHumanReadableCopyright": "Copyright © 2023, Khaled KHEBBEB, All Rights Reserved",
    },
}

# BUILD APP
# __________
setup(
    name=APP_NAME,
    app=APP,
    data_files=DATA_FILES,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
)
