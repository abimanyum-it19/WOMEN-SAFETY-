from tkinter import *
from tkinter import ttk
root = Tk()
def HUMAN():
    import numpy as np
    import cv2
    # initialize the HOG descriptor/person detector
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    cv2.startWindowThread()
    # open webcam video stream
    value = text.get('1.0', '1.end')
    value1 = text1.get('1.0', '1.end')
    value2 = text3.get('1.0', '1.end')
    a=('rtsp://'+value+':'+value1+'@'+value2+'/live')
    cap = cv2.VideoCapture(a)
    # the output will be written to output.avi
    out = cv2.VideoWriter(
        'output.avi',
        cv2.VideoWriter_fourcc(*'MJPG'),
        15.,
        (640,480))

    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        # resizing for faster detection
        frame = cv2.resize(frame, (640, 480))
        # using a greyscale picture, also for faster detection
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        # detect people in the image
        # returns the bounding boxes for the detected objects
        boxes, weights = hog.detectMultiScale(frame, winStride=(8,8) )
        boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])
        for (xA, yA, xB, yB) in boxes:
            # display the detected boxes in the colour picture
            cv2.rectangle(frame,(xA, yA), (xB, yB),(0, 255, 0), 2)
        # Write the output video 
        out.write(frame.astype('uint8'))
        # Display the resulting frame
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # When everything done, release the capture
    cap.release()
    # and release the output
    out.release()
    # finally, close the window
    cv2.destroyAllWindows()
    cv2.waitKey(1)
def sms():
    value3 = text4.get('1.0', '1.end')
    a="Unauthorized human activity detected @ "+value3
    from twilio.rest import Client
    # Your Account Sid and Auth Token from twilio.com/console
    # DANGER! This is insecure. See http://twil.io/secure
    account_sid = 'AC104d9ec12e13acad3c2aabd6890b2303'
    auth_token = '7a0e73832fa7ade9f3ef6dd1eecc02c4'
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body='a',
            from_='+12028580870',
            to='+91 94892 52155'
            )
    print(message.sid)


    


#LABEL
label = ttk.Label(root,text = 'IDENTIFYING WOMEN HARASSMENT IN PUBLIC CCTV CAMERA USING AI')
label.pack()
label.config(justify = CENTER)
label.config(foreground ='blue')

Label(root, text="USER").pack()
#TEXTBOX
text = Text(root,width = 40, height = 1)
text.pack()
Label(root, text="PASSWORD").pack()
#TEXTBOX
text1= Text(root,width = 40, height = 1)
text1.pack()
Label(root, text="IP").pack()
#TEXTBOX
text3= Text(root,width = 40, height = 1)
text3.pack()
Label(root, text="LOCATION").pack()
#TEXTBOX
text4= Text(root,width = 40, height = 1)
text4.pack()


#BUTTON
button = ttk.Button(root, text = 'SUMBIT',command = HUMAN)
button.pack()

#FUNCTION DEF




root.mainloop()
