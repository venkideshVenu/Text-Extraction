import cv2
import pytesseract


# Path to Tesseract executable (change this to your Tesseract installation path)
pytesseract.pytesseract.tesseract_cmd = r'<path of pytesseract cmd>'
def extract_text_from_image(image_path):
    # Read the image using OpenCV
    image = cv2.imread(image_path)
    
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply thresholding to preprocess the image
    _, threshold_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    
    # Use Tesseract to perform OCR on the thresholded image
    extracted_text = pytesseract.image_to_string(threshold_image)

    # Find contours around the text regions
    contours, _ = cv2.findContours(threshold_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Draw contours around the text regions
    image_with_contours = image.copy()
    cv2.drawContours(image_with_contours, contours, -1, (0, 255, 0), 2)
    
    print("Extracted Text from ",image_path,"  :  ")
    print(extracted_text)

    cv2.imshow(image_with_contours)
    cv2.waitKey(0)




# Example usage
image_path = 'text.jpg'  # Change this to the path of your image
extract_text_from_image('quote.jpg')
extract_text_from_image('quote2.jpg')


cv2.destroyAllWindows()
