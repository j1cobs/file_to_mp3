# file_to_mp3

Convert text-based files (PDFs, PPTX, DOCX, TXT) into MP3 audio using Python. Leverage Google Translate, pyttsx3, PyPDF2, and python-pptx/python-docx for translation, speech synthesis, and file handling. Enhance accessibility and learning by turning content into spoken audio.

Enjoy streamlined conversion of documents to MP3 for improved accessibility and learning experiences.

## Installation

You can quickly set up and run the File-to-MP3 Converter on your system by following these steps:

### Prerequisites

Python 3.6 or higher is required.
Ensure you have git installed for cloning the repository.

### Clone the Repository

```bash
git clone https://github.com/your-username/file-to-mp3-converter.git
cd file-to-mp3-converter
```

### Create and Activate Virtual Environment (Optional but Recommended)

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

Use the **requirements.txt** file to install the necessary packages:

```bash
pip install -r requirements.txt
```

or just run the **install_packages.py** file:

```bash
python install_package.py
```

**_Please note that this code assumes that you have pip installed and available in your system's PATH. Additionally, you should run this script using a Python interpreter that has sufficient permissions to install packages._**

### Run the Application

```bash
python file_to_mp3.py
```

The graphical user interface (GUI) will open, and you can start converting your files to MP3 audio with ease.

## How to Use the Project

Breakdown of every file/folder in that project

### Voices

This folder is where the voices are stored, you can add more if you would like.  
Useful links to do it:
https://stackoverflow.com/questions/66884970/how-to-add-your-own-tts-voices-for-pyttsx3-python
https://puneet166.medium.com/how-to-added-more-speakers-and-voices-in-pyttsx3-offline-text-to-speech-812c83d14c13

### file_to_mp3.py

Main logic of the program, calling the functions from **functions.py** and handling the different file formats.
This is where you would add another file format to handle.

### functions.py

Called functions are stored in this file.
This is where you would add a function.

### install_packages.py

This is a python script to automate the installation of the modules needed for this project.

### requirements.txt

Modules needed for this project.

## Credits

Inspiration for the project: https://youtu.be/LXsdt6RMNfY?si=G_lxIe-87cZIJ9Zf

## License

MIT License

Copyright (c) 2023 j1cobs

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
