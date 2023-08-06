# PyTesseract.py
import cv2
import pytesseract

# Set up PyTesseract
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

# Image path (replace with your own image path)
image_path = '../crop-result/LP5.jpg'

# Load the image
image = cv2.imread(image_path)

# Perform OCR
pytesseract_result = pytesseract.image_to_string(image)
pytesseract_text = pytesseract_result.strip()

# Print the OCR result
print("PyTesseract Result:", pytesseract_text)