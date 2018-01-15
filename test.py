from PIL import ImageGrab, Image
import pytesseract


question = pytesseract.image_to_string(Image.open('question.png'))
print(question)
print(question is '')
