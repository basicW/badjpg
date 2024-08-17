# badjpg
## Overview
This Python script allows you to hide a payload within a JPG image using steganography techniques. It uses the `stegano` library to encode and decode messages within the least significant bit (LSB) of the image pixels.
## Warning
I must emphasize that using such techniques for malicious purposes is unethical and potentially illegal. However, if you have a legitimate use case, such as for educational purposes or digital watermarking.
## Installing Dependencies
This code requires two external libraries:
1. stegano: This is the core library used for hiding and revealing data within images using Least Significant Bit (LSB) steganography.
2. Pillow (PIL Fork): This library provides functionalities for image manipulation, including opening, saving, and processing images.
   ## How?
   Use pip:
   ```bash
   pip install stegano Pillow
   ```
   ## Explanation of Dependencies:
1. stegano: This library likely provides functions like hide and reveal for manipulating image data and embedding messages using LSB steganography.  
2. Pillow (PIL Fork): Pillow is a popular library for image processing in Python. It offers functions like Image.open and save for working with image files in various formats.
   ## Note:
Depending on the specific implementation of stegano, the actual function names might differ slightly. Consult the library's documentation for precise details. I'm no expert.
Make sure you install the Pillow library, not the original PIL (Python Imaging Library).  
## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/basicW/badjpg.git
    ```
2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Install the `stegano` library if you have not already:
   ```bash
   pip install stegano
   ```

## Usage
1. Place the image file (JPG format) you want to hide the payload in within the project directory.
2. Run the Python script `steganography.py`.
3. Follow the prompts to specify the image file path, the payload to hide, and the output file name.
4. The script will then encode the payload into the image and save the resulting image with the hidden payload.

To extract the hidden payload from the image:
1. Run the Python script `steganography.py`.
2. Choose the option to extract the payload.
3. Provide the path to the image file with the hidden payload.
4. The script will reveal the hidden payload from the image.

## Example
```bash
python steganography.py
```
## Requirements
1. Python 3.x
2. `stegano` library

## Acknowledgements
This project uses the stegano library.
