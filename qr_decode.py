# Install required libraries first:
# pip install opencv-python pylibdmtx

import cv2
from pylibdmtx.pylibdmtx import decode

# Load the image
image_path = 'qr.png'  # Replace with your actual image path
image = cv2.imread(image_path)

# Convert to grayscale for better decoding
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Decode the Data Matrix code
decoded_objects = decode(gray)

# Display results
for obj in decoded_objects:
    print("Decoded Data:", obj.data.decode('utf-8'))
    print("Bounding Box:", obj.rect)
