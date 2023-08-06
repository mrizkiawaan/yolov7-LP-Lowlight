# EasyOCR.py
import cv2
import easyocr

# Set up EasyOCR
reader = easyocr.Reader(['en'])

# Image path (replace with your own image path)
image_path = '../crop-result/LP5.jpg'

# Load the image
image = cv2.imread(image_path)

# Perform OCR
easyocr_result = reader.readtext(image)
easyocr_text = easyocr_result[0][1] if easyocr_result else ''

# Print the OCR result
print("EasyOCR Result:", easyocr_text)