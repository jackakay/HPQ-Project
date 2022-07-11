import pytesseract
from PIL import Image

print(int((pytesseract.image_to_string(Image.open(r"C:\Users\jackk\__HPQ school project\Dead\test.png"))).replace(",", "")))
