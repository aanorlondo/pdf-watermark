
<div align="center">
<h1 align="center">
<img src="src/appdata/watermark.ico" width="100" />
<br>
pdf-watermark
</h1>
<h3 align="center">📍 Level up your PDFs with pdf-watermark: Leave your mark on every page!</h3>
<h3 align="center">⚙️ Developed with the software and tools below:</h3>

<p align="center">
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/Qt-%23217346.svg?style=for-the-badge&logo=Qt&logoColor=white" alt="QT" />
<img src="https://img.shields.io/badge/JSON-000000.svg?style=for-the-badge&logo=JSON&logoColor=white" alt="JSON" />
<img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=for-the-badge&logo=GNU-Bash&logoColor=white" alt="GNU%20Bash" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style=for-the-badge&logo=Markdown&logoColor=white" alt="Markdown" />
</p>
</div>

---

## 📚 Table of Contents
- [📚 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [💫 Features](#-features)
- [📂 Project Structure](#project-structure)
- [🧩 Modules](#modules)
- [🚀 Getting Started](#-getting-started)
- [🗺 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---


## 📍 Overview

The PDF Watermark project is a Python application that offers both a command-line interface (CLI) and a graphical user interface (GUI) for adding watermarks to PDF files. The core functionality includes loading a configuration file, calculating the position and size of the watermark, and applying it to each page of the PDF. The project's purpose is to provide an easy and efficient way to apply watermarks, allowing users to protect their PDFs and add branding or copyright information. Its value proposition lies in its flexibility, as it supports custom configuration files and provides options for both CLI and GUI interactions.

---

## 💫 Features

Feature | Description |
|---|---|
| **🏗 Structure and Organization** | The codebase has a clear organization with separate files for the CLI and GUI versions, as well as a file for constants and variables. There is also a version file and a separate directory for storing input and output files. |
| **📝 Code Documentation** | The codebase lacks comprehensive documentation, making it difficult for new developers to understand the functionality and usage of the application. |
| **🧩 Dependency Management** | The codebase manages dependencies using external libraries such as PyPDF2, reportlab, and PyQt6, which are imported in the necessary files for PDF manipulation, watermark generation, and GUI development, respectively. The codebase uses the `requirements.txt` file to specify the required dependencies, and the `setup.py` file manages the installation of these dependencies using `pip`. This ensures consistent dependency management and ease of installation. |
| **♻️ Modularity and Reusability** | The codebase demonstrates modularity and reusability by separating the CLI and GUI versions into individual files, allowing these components to be used independently or together. |
| **🔒 Security Measures** | There is no specific information available about security measures, so it's unclear if there are any specific measures implemented to protect user data or prevent vulnerabilities. |
| **🔌 External Integrations** | The codebase integrates external libraries such as PyPDF2, reportlab, and PyQt6 for PDF manipulation, watermark generation, and GUI development, respectively. |
| **📈 Scalability and Extensibility** | The codebase can be extended and scaled by adding new functionality or modifying existing code due to its modular design and separation of different components. |

---


<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-github-open.svg" width="80" />

## 📂 Project Structure


```bash
repo
├── LICENSE
├── README.md
├── docs
│   ├── cli.png
│   └── gui.png
├── src
│   ├── appdata
│   │   ├── VERSION.txt
│   │   ├── config.json
│   │   ├── template.txt
│   │   └── watermark.ico
│   ├── misc.py
│   ├── requirements.txt
│   ├── setup.py
│   ├── setup.sh
│   ├── watermark_cli.py
│   └── watermark_gui.py
└── test
    ├── input
    │   └── pdf-test.pdf
    └── output
        ├── NAME_MARKED_POSITION_SIZE.pdf
        ├── pdf-test_marked_bottom-left_8.pdf
        ├── pdf-test_marked_bottom-right_8.pdf
        ├── pdf-test_marked_bottom_8.pdf
        ├── pdf-test_marked_center_8.pdf
        ├── pdf-test_marked_left_8.pdf
        ├── pdf-test_marked_right_8.pdf
        ├── pdf-test_marked_top-left_8.pdf
        ├── pdf-test_marked_top-right_8.pdf
        └── pdf-test_marked_top_8.pdf

6 directories, 25 files
```

---

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-src-open.svg" width="80" />

## 🧩 Modules

<details closed><summary>Src</summary>

| File             | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Module               |
|:-----------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------|
| watermark_cli.py | This code snippet is a Python script that applies a watermark to PDF files. It uses the PyPDF2, reportlab, and json libraries to load a configuration file, calculate the position and size of the watermark, and add the watermark to each page of the input PDF files. The script can be run from the command line, accepting arguments for the input directory, output directory, and watermark text, and it also supports a custom configuration file. | src/watermark_cli.py |
| setup.sh         | This code snippet performs a set of tasks to build a Python application:                                                                                                                                                                                                                                                                                                                                                                                   | src/setup.sh         |
|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                      |
|                  | 1. It sets up a virtual environment using Python's `venv` module and activates it.                                                                                                                                                                                                                                                                                                                                                                         |                      |
|                  | 2. It installs the required dependencies listed in the `requirements.txt` file using `pip`.                                                                                                                                                                                                                                                                                                                                                                |                      |
|                  | 3. It deletes any previous build artifacts and runs the `setup.py` script to generate a macOS application package using `py2app`.                                                                                                                                                                                                                                                                                                                          |                      |
|                  | 4. Finally, it deactivates the virtual environment and cleans it up, and displays a success message with the path to the built application.                                                                                                                                                                                                                                                                                                                |                      |
| misc.py          | This code snippet defines various file paths and directory locations used in a PDF watermarking application. It also initializes default configuration values and provides information about the application's version and information for both the GUI and CLI versions. Additionally, it reads a template file to set default watermark text if the file exists.                                                                                         | src/misc.py          |
| watermark_gui.py | The code snippet is a Python script that creates a graphical user interface (GUI) for a PDF watermarking application. It uses the PyQt6 library for building the GUI components. The GUI allows users to select input and output directories, enter text for the watermark, configure settings, and apply the watermark to PDF files. The script also handles error messages and provides information to the user.                                         | src/watermark_gui.py |
| setup.py         | This code snippet sets up a Python application called "PdfWatermark" using the `setuptools` library. It defines the application's data, version, and build options. The application is built using `py2app` and includes data files and an icon. The setup configuration also includes information such as the application name, version, and copyright details.                                                                                           | src/setup.py         |

</details>

---

## 🚀 Getting Started

### ✅ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> - Tested on MacOS Monterey V12.5
> - Requires Python 3.11.4 and +

### 🖥 Installation

1. Clone the pdf-watermark repository:
```sh
git clone https://github.com/aanorlondo/pdf-watermark.git
```

2. Change to the project directory:
```sh
cd pdf-watermark
```

3. Install the dependencies:
```sh
pip install -r requirements.txt
```

## 🤖 Using pdf-watermark


### Configuration management 
The tools configuration (color, font, position, etc.) is held within the `src/config.json` file
    - You can edit and redefine the default configuration as you please.

### Template management:
You can save your custom text as template for your your watermarks
    - You can save your template wihin the `src/template.txt` file

### Using the CLI Interface
- Run the following commands :
    ```
    cd pdf-watermark/src
    python watermark_cli.py --help
    ```
- Enjoy !

<img src="docs/cli.png" alt="CLI" width="650px"/>


### Using the GUI Interface

#### 1- Run from Codebase
- Run the following commands :
    ```
    cd pdf-watermark/src
    python watermark_gui.py
    ```
- Enjoy !

#### 2- Install as MacOS Desktop Application

- Run the following commands :
    ```
    cd pdf-watermark/src
    sh setup.sh
    ```
- Then, using the finder, go under `pdf-watermark/src/dist/` folder. 
- `Double-click` or `Drag&drop` the Application directly to your Dock.

    <img src="docs/install.png" alt="CLI" width="450px"/>

- Run the application

    <img src="docs/gui.png" alt="CLI" width="450px"/>

- Enjoy !
---


## 🗺 Roadmap

> - [] Improve the rotation algorithm


---

## 🤝 Contributing

Contributions are always welcome! Please follow these steps:
1. Fork the project repository. This creates a copy of the project on your account that you can modify without affecting the original project.
2. Clone the forked repository to your local machine using a Git client like Git or GitHub Desktop.
3. Create a new branch with a descriptive name (e.g., `new-feature-branch` or `bugfix-issue-123`).
```sh
git checkout -b new-feature-branch
```
4. Make changes to the project's codebase.
5. Commit your changes to your local branch with a clear commit message that explains the changes you've made.
```sh
git commit -m 'Implemented new feature.'
```
6. Push your changes to your forked repository on GitHub using the following command
```sh
git push origin new-feature-branch
```
7. Create a pull request to the original repository.
Open a new pull request to the original project repository. In the pull request, describe the changes you've made and why they're necessary.
The project maintainers will review your changes and provide feedback or merge them into the main branch.

---

## 📄 License

This project is licensed under the `MIT` License. See the [LICENSE](LICENSE) file for additional info.

---

## 👏 Acknowledgments
Personal project

---

## Credits

This awesome documentation was automatically generated using the [README-AI Project](https://github.com/eli64s/README-AI)

---