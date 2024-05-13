# badjpg
## Overview
This Python script allows you to hide a payload within a JPG image using steganography techniques. It uses the `stegano` library to encode and decode messages within the least significant bit (LSB) of the image pixels.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/steganography-tool.git
    ```
2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
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
