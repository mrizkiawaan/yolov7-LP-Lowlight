import cv2
import easyocr
import keras_ocr
import pytesseract
import pathlib
import numpy as np
from fuzzywuzzy import fuzz

def perform_easyocr(image_path):
    reader = easyocr.Reader(['en'])
    image_string = str(image_path)
    easyocr_result = reader.readtext(image_string)
    easyocr_text = easyocr_result[0][1] if easyocr_result else ''
    return easyocr_text.lower()

def perform_kerasocr(image_path):
    pipeline = keras_ocr.pipeline.Pipeline()
    image_array = np.array(image_path)
    kerasocr_result = pipeline.recognize([image_array])
    kerasocr_text = " ".join([word[0] for word in kerasocr_result[0]]) if kerasocr_result else ''
    return kerasocr_text.lower()

def perform_pytesseract(image_path):
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
    pytesseract_result = pytesseract.image_to_string(image_path)
    pytesseract_text = pytesseract_result.strip()
    return pytesseract_text.lower()

def calculate_accuracy(ocr_text, ground_truth):
    return fuzz.ratio(ocr_text, ground_truth) / 100.0

def perform_ocr(image_path, ground_truth):
    image = cv2.imread(image_path)
    image_path = pathlib.Path(image_path)
    easyocr_text = perform_easyocr(image_path)
    kerasocr_text = perform_kerasocr(image)
    pytesseract_text = perform_pytesseract(image)
    easyocr_accuracy = calculate_accuracy(easyocr_text, ground_truth.lower())
    kerasocr_accuracy = calculate_accuracy(kerasocr_text, ground_truth.lower())
    pytesseract_accuracy = calculate_accuracy(pytesseract_text, ground_truth.lower())
    return easyocr_text, easyocr_accuracy, kerasocr_text, kerasocr_accuracy, pytesseract_text, pytesseract_accuracy

# Ground truth text
ground_truth = "B 2897 SIA"
# Image path
image_path = 'D:/Dev/TugasAkhir/crop_result/fully_detected/133.jpg'

# Perform OCR
easyocr_text, easyocr_accuracy, kerasocr_text, kerasocr_accuracy, pytesseract_text, pytesseract_accuracy = perform_ocr(image_path, ground_truth)

# Print the OCR results and accuracy
print("EasyOCR Result:", easyocr_text)
print("EasyOCR Accuracy: {:.3f}".format(easyocr_accuracy))
print()
print("KerasOCR Result:", kerasocr_text)
print("KerasOCR Accuracy: {:.3f}".format(kerasocr_accuracy))
print()
print("PyTesseract Result:", pytesseract_text)
print("PyTesseract Accuracy: {:.3f}".format(pytesseract_accuracy))
