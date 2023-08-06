# KerasOCR.py
import cv2
import keras_ocr

# Set up KerasOCR
pipeline = keras_ocr.pipeline.Pipeline()

# Image path (replace with your own image path)
image_path = '../crop-result/LP5.jpg'

# Load the image
image = cv2.imread(image_path)

# Perform OCR
kerasocr_result = pipeline.recognize([image])
kerasocr_text = " ".join([word[0] for word in kerasocr_result[0]]) if kerasocr_result else ''

# Print the OCR result
print("KerasOCR Result:", kerasocr_text)