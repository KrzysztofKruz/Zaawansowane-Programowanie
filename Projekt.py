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

    def process_image(self, image_path: str):
        cvNet = cv.dnn.readNetFromTensorflow('frozen_inference_graph.pb', 'graph.pbtxt')
        img = cv.imread(f'{self.path}/{image_path}')
        rows = img.shape[0]
        cols = img.shape[1]
        cvNet.setInput(cv.dnn.blobFromImage(img, size=(300, 300), swapRB=True, crop=False))
        cvOut = cvNet.forward()

        for detection in cvOut[0, 0, :, :]:
            score = float(detection[2])
            if score > 0.3:
                left = detection[3] * cols
                top = detection[4] * rows
                right = detection[5] * cols
                bottom = detection[6] * rows
                cv.rectangle(img, (int(left), int(top)), (int(right), int(bottom)), (23, 230, 210), thickness=2)

        cv.imshow('img', img)
        cv.waitKey()


processor = ImageProcessing('C:\\Users\\student\\source\\repos\\imageprocessing\\images')
images = processor.read_files()

print(images)