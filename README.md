# badjpg
Overview
This Python script allows you to hide a payload within a JPG image using steganography techniques. It uses the stegano library to encode and decode messages within the least significant bit (LSB) of the image pixels.

Installation
Clone the repository:
bash
Copy code
git clone https://github.com/your-username/steganography-tool.git
Install the required dependencies:
bash
Copy code
pip install -r requirements.txt
Usage
Place the image file (JPG format) you want to hide the payload in within the project directory.
Run the Python script steganography.py.
Follow the prompts to specify the image file path, the payload to hide, and the output file name.
The script will then encode the payload into the image and save the resulting image with the hidden payload.
To extract the hidden payload from the image:

Run the Python script steganography.py.
Choose the option to extract the payload.
Provide the path to the image file with the hidden payload.
The script will reveal the hidden payload from the image.
