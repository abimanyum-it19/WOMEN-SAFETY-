from tkinter import *
from tkinter import ttk
root = Tk()
def HUMAN():
    from keras.preprocessing.image import img_to_array
    from keras.models import load_model
    from keras.utils import get_file
    import numpy as np
    import cv2
    import os
    import cvlib as cv
    # initialize the HOG descriptor/person detector
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    cv2.startWindowThread()
    # open webcam video stream
    value = text.get('1.0', '1.end')
    value1 = text1.get('1.0', '1.end')
    value2 = text3.get('1.0', '1.end')
    a=('rtsp://'+value+':'+value1+'@'+value2+'/live')
    dwnld_link = "https://github.com/arunponnusamy/cvlib/releases/download/v0.2.0/gender_detection.model"
    model_path = get_file("gender_detection.model", dwnld_link,cache_subdir="pre-trained", cache_dir=os.getcwd())
    model = load_model(model_path)
    webcam = cv2.VideoCapture(a)
    if not webcam.isOpened():
        print("Could not open webcam")
        exit()
    classes = ['men','women']
    # loop through frames
    while webcam.isOpened():
        # read frame from webcam 
        status, frame = webcam.read()
        if not status:
            print("Could not read frame")
            exit()
        # apply face detection
        face, confidence = cv.detect_face(frame)
        print(face)
        print(confidence)
        # loop through detected faces
        for idx, f in enumerate(face):
            # get corner points of face rectangle
            (startX, startY) = f[0], f[1]
            (endX, endY) = f[2], f[3]
            # draw rectangle over face
            cv2.rectangle(frame, (startX,startY), (endX,endY), (0,255,0), 2)
            # crop the detected face region
            face_crop = np.copy(frame[startY:endY,startX:endX])
            if (face_crop.shape[0]) < 10 or (face_crop.shape[1]) < 10:
                continue
            face_crop = cv2.resize(face_crop, (96,96))
            face_crop = face_crop.astype("float") / 255.0
            face_crop = img_to_array(face_crop)
            face_crop = np.expand_dims(face_crop, axis=0)
            # apply gender detection on face
            conf = model.predict(face_crop)[0]
            print(conf)
            print(classes)
            # get label with max accuracy
            idx = np.argmax(conf)
            label = classes[idx]
            label = "{}: {:.2f}%".format(label, conf[idx] * 100)
            Y = startY - 10 if startY - 10 > 10 else startY + 10
            # write label and confidence above face rectangle
            cv2.putText(frame, label, (startX, Y),  cv2.FONT_HERSHEY_SIMPLEX,
                        0.7, (0, 255, 0), 2)
        # display output
        cv2.imshow("gender detection", frame)
        # press "Q" to stop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # release resources
    webcam.release()
    cv2.destroyAllWindows()
    cv2.destroyAllWindows()
def sms():
    value3 = text4.get('1.0', '1.end')
    a="A women has been identified in  "+value3
    from twilio.rest import Client
    # Your Account Sid and Auth Token from twilio.com/console
    # DANGER! This is insecure. See http://twil.io/secure
    account_sid = 'AC104d9ec12e13acad3c2aabd6890b2303'
    auth_token = '7a0e73832fa7ade9f3ef6dd1eecc02c4'
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body=a,
            from_='+12028580870',
            to='+91 94892 52155'
            )
    print(message.sid)


    


#LABEL
label = ttk.Label(root,text = 'IDENTIFYING WOMEN HARASSMENT IN PUBLIC CCTV CAMERA  AI')
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
