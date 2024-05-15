# Text Extraction from Images using OpenCV and Tesseract

This project demonstrates how to extract text from images using the OpenCV library for image processing and Tesseract OCR (Optical Character Recognition) engine.

## Prerequisites

- Python 3.12 or above
- OpenCV (`pip install opencv-python`)
- pytesseract (`pip install pytesseract`)
- Tesseract OCR installed on your system (refer to [Tesseract installation guide](https://github.com/tesseract-ocr/tesseract))

## Usage

1. Clone or download this repository.
2. Install the required dependencies mentioned in the 'Prerequisites' section.
3. Ensure that Tesseract OCR is installed and its path is correctly set in the code (`pytesseract.pytesseract.tesseract_cmd` variable).
4. Place the images from which you want to extract text in the project directory.
5. Update the `image_path` variable in the `extract_text_from_image` function call with the path to your image.
6. Run the `extract_text_from_image` function with your image path as an argument.

```python
# Example usage
image_path = 'your_image.jpg'  # Change this to the path of your image
extract_text_from_image(image_path)
