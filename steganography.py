from stegano import lsb
from PIL import Image

def hide_payload(image_path, payload, output_path):
    try:
        secret = lsb.hide(image_path, payload)
        secret.save(output_path)
        print("Payload successfully hidden in the image!")
    except Exception as e:
        print("Error:", e)

def extract_payload(image_path):
    try:
        secret = lsb.reveal(image_path)
        print("Extracted Payload:", secret)
    except Exception as e:
        print("Error:", e)

# Example usage
image_path = "example.jpg"
payload = "This is a secret message!"
output_path = "output_image_with_payload.jpg"

# Hide payload
hide_payload(image_path, payload, output_path)

# Extract payload
extract_payload(output_path)
