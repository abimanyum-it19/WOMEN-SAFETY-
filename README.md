# -IDENTIFYING-WOMEN-HARASSMENTS-IN-PUBLIC-CCTV-CAMERAS-USING-ARTIFICIAL-INTELLIGENCE-TECHNIQUES
Designed software for women Safety


Providing Safety for women in the nighttime by Artificial Intelligences techniques. The cameras will be able to detect any change in the facial expressions of a woman being subjected to stalking, threats, or harassment on the streets, and an alert will be sent to the police control room.

## NEED FOR PROJECT


* The society probably living in the worst time. Our current society has ever seen in terms of women security. The projects aim is to make women experience as strong as ever and sufficiently able to fight the parasites of our general public. Our project is an idea that makes every place safer for women.

* Nowadays the news about women harassment is more than their accomplishments. The purpose of the proposed system is to decrease the incidence of sexual harassment faced by women experiences in their life and to increase women self-confidence to step out to their office during nights and desire to use public spaces in the city particularly during night.

* Women feel unsafe to move alone at bizarre times. There are many applications that are built for women safety.  Even there are many uneducated women those who do not have android phones or do not know how to handle it. The proposed system aims to provide safety for the women who are in trouble. Surely there will be CCTV cameras in every public place.

* This model does not require any special hardware and it uses algorithm for the precaution of women. The algorithm is then applied on the CCTV cameras and then the gender of the person will be predicted. The Warning message will be sent to the close by police head quatres; This project is made for the conveniences of all women.

## IMPLEMENTATION METHODOLOGY

Even though there are specialized apps and many IOT devices for women safety, this proposed system doesn’t require any special computer hardware to process. Since, it is user friendly and will be supportive for the uneducated and poor people. The preprocessed CCTV footage are applied to Convolution Neural Network (CNN) and tensor flow for classification.
 
 Implementation Methodology is classified into three modules.
     
     A) Human Detection
     
     B) Gender Prediction
     
     C) Anomalous Activity Detection
## WORK FLOW

Step 1:  Access Live CCTV camera stream.

Step 2:   detects the Presence of humans

Step 3: If any human activity is detected it will enter the next module (i.e.) Gender prediction.

Step 4: It will be identifying any women is    there or not.

Step 5: Then it will be looking for anomalous activity.

Step 6: If any activity is found it will be sending an alert notification to the close by police station or control room.

![image](https://user-images.githubusercontent.com/53464755/178768257-288101bc-4fc0-4f4b-97a7-5d9ac584a046.png)

## A. HUMAN DETECTION
* Access the live camera and detect presences of the human.

![image](https://user-images.githubusercontent.com/53464755/178768594-faed3858-c26a-435f-8fa4-4398f3b29ddf.png)

## B. GENDER PREDICTION
* After detecting the human movement it will be trying to predict the gender of the detected human.

* In case, if a female is standing alone in a railway station or in any different open location .

* Particular at night time’s it  is observed by the CCTV camera and the alarm message will be sent to the nearby by police headquarters.

![image](https://user-images.githubusercontent.com/53464755/178768813-02fe5269-a38a-42da-991f-c4881562211a.png)

## C. ANOMALOUS ACTIVITY DETECTION
* Human abnormal activity is detected

![image](https://user-images.githubusercontent.com/53464755/178769095-bdad739e-643a-41ad-a5b3-8bca2250a4ac.png)

## ALERT THROUGH WHATSAPP
* When ever the anomalous activity is detected the alert notification will be sent through WhatsApp message

![image](https://user-images.githubusercontent.com/53464755/178769220-959653bc-513d-4634-be66-23fadee7bf70.png)

User Feedback

* No special Hardware, existing CCTV can be reused.

* Safety to uneducated people who are not using Smart phones .

* Prevent the occurrences of event before harassment happens

# Environment setup:

1. Install Anaconda:

 https://www.anaconda.com/download/
 
2.Creating an environment with commands

   * To create an environment:
   
           conda create --name myenv
     
     !Note:
     Replace myenv with the environment name.
   
   * When conda asks you to proceed, type y:
   
           proceed ([y]/n)?
           
     This creates the myenv environment in /envs/. No packages will be installed in this environment.

     !Note:
Replace myenv with the environment name or or directory path.
       
3. Activating an environment
 
  * To activate an environment:
       
           conda activate myenv
       
4. Install Python packages

     * Tkinter
     * Numpy
     * OpenCV
     * Keras
     * os
     * cvlib
     * Twilio

   Install the required packages by executing the following command.

       pip install (package name)
   
       example:
 
           $ pip install numpy
           
    Make sure pip is linked to Python
   
    Using Python virtual environment is highly recommended.
   
    ## Usage:
   
    webcam
   
   
              $ python gender_webcam.py
              $ python human_webcam.py
             
     Input image
   
   
              $ python gender.py
              $ python human.py
             
     When you run the script for the first time, it will download the pre-trained model from this link and place it under pre-trained directory in the current path.
     
## output

    https://youtu.be/p4SF9obtEZo

## Help
   
If you are facing any difficulty, feel free to create a new issue or reach out on [Linkedin](https://www.linkedin.com/in/abimanyu-m-872258208/)
