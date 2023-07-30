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

# INSTALL
# _______
APP_PACKAGE="PdfWatermark.app"
DIST_PATH="dist/${APP_PACKAGE}"
INSTALL_PATH="${HOME}/Applications/${APP_PACKAGE}"
rm -rf "${INSTALL_PATH}"
cp -rf "${DIST_PATH}/" "${INSTALL_PATH}"

# SUCCESS
# _______
echo "INSTALLATION SUCCESS
The PdfWatermark App has succesfully been built (${DIST_PATH}).
It has been installed in your User Applications folder: ${INSTALL_PATH} !
Enjoy It :)
"
