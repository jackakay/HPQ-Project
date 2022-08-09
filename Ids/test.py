from PIL import Image
import pytesseract
#img = Image.open(r'C:\Users\jackk\__HPQ school project\HPQ-Project\Ids\8.png').convert('L')
#img.save(r'C:\Users\jackk\__HPQ school project\HPQ-Project\Ids\pil-greyscale.png')
def scanImage(filename):
    return pytesseract.image_to_string(Image.open(filename))
print(scanImage(r'C:\Users\jackk\__HPQ school project\HPQ-Project\Ids\ 8GS.png'))
