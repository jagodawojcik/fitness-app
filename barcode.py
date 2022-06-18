import cv2 #opencv to process video frames
from pyzbar import pyzbar    #to decode and read barcodes
import time

#capture video
cap = cv2.VideoCapture(0)
cap.set(3, 640) #3- width
cap.set(4, 480) #4 - height


camera = True
barcodes = []

while camera == True:
    success, frame = cap.read()

    for code in pyzbar.decode(frame):
        if code.data.decode('utf-8') not in barcodes:
            print(code.type)
            print('Code read successfully!')
            print(code.data.decode('utf-8'))
            barcodes.append(code.data.decode('utf-8'))
            time.sleep(5)
            
        elif code.data.decode('utf-8') in barcodes:
            print('Code already seen!')
            time.sleep(5)
        else:
            pass


    cv2.imshow('Barcode Scanner', frame)
    key = cv2.waitKey(1)
    if key == ord("q"):
         break


cv2.destroyAllWindows()
