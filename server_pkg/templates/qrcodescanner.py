#import libraries
import cv2
from pyzbar import pyzbar
# define a video capture object
vid = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()


def readQr():
    while True:
        # Capture the video frame by frame
        ret, frame = vid.read()
        data, bbox, straight_qrcode = detector.detectAndDecode(frame)
        if len(data) > 0:
            print(data)
        # Display the resulting frame
        cv2.imshow('frame', frame)
        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()


readQr()
# After the loop release the cap object
