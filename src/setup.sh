#!/bin/sh

# DEPS
# ________
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# BUILD APP
# ________
rm -rf build dist .eggs
python setup.py py2app
deactivate
rm -rf .eggs
rm -rf .venv

# SUCCESS
# _______
APP_NAME="PdfWatermark"
DIST_PATH="dist/${APP_NAME}.app/Contents/MacOS/${APP_NAME}"
echo "Congrats ! The app has been built here: ${DIST_PATH}. You can run it on your MacOs system :)"
