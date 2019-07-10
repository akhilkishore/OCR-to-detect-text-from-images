import pytesseract
 
from PIL import Image
 
value=Image.open("/home/akhil/Desktop/a.jpg")
 
text=pytesseract.image_to_string(value)
 
print("text present in images:",text)