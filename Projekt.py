import pytesseract.pytesseract as pt
import cv2 as cv
import os

pt.pytesseract.tesseract_cmd = 'C:\\Users\\student\\AppData\\Local\\Tesseract-OCR\\tesseract.exe'


class ImageProcessing:
    def __init__(self, folder_images_path: str):
        self.path = folder_images_path
        self.images = []

    def read_files(self):
        dir_files = os.listdir(self.path)
        for file in dir_files:
            if file[-4:].lower() == 'jpeg':
                self.images.append(file)
            elif file[-4:].lower() == '.jpg':
                self.images.append(file)
            elif file[-4:].lower() == '.png':
                self.images.append(file)

        return self.images


processor = ImageProcessing('C:\\Users\\student\\source\\repos\\imageprocessing\\images')
images = processor.read_files()

print(images)