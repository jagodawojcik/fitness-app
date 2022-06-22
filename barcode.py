import cv2 #opencv to process video frames
from pyzbar.pyzbar import ZBarSymbol    #to decode and read barcodes
from pyzbar.pyzbar import decode    #to decode and read barcodes
import time

from pyzbar.pyzbar import ZBarSymbol



#capture video
def vidOn():
    stream = cv2.VideoCapture(0)
    stream.set(3, 640) #3- width
    stream.set(4, 480) #4 - height
    camera = True

    return camera, stream

def decodeVid(camera, stream):
    barcodes = []
    
    while camera == True:
        success, frame = stream.read()
        
        #EAN13 to restrict decoding to EAN13 type and avoid errors
        for code in decode(frame, symbols=[ZBarSymbol.EAN13]):
            #(x, y, w, h) = code.rect
            #print(x, y, w, h)
            #cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255), 2)
            #text = "{}".format(code.data.decode)
            #cv2.putText(frame, text, (x,y -15),
            #cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
            
		
            if code.data.decode('utf-8') not in barcodes:
                print(code.type)
                print('Code read successfully!')
                print(code.data.decode('utf-8'))
                barcodes.append(code.data.decode('utf-8'))
                time.sleep(5)
            elif code.data.decode('utf-8') in barcodes:
                print('Code already seen!')
            else:
                pass
    
        cv2.imshow('Barcode Scanner', frame)
        key = cv2.waitKey(1)
        if key == ord("q"):
            break
        
        cv2.destroyAllWindows()
    return barcodes


#test the code
if __name__ == '__main__':
    camera, stream = vidOn()
    barcodes = decodeVid(camera, stream)
    print('all barcodes stored are: \n', )
    print(barcodes)
    