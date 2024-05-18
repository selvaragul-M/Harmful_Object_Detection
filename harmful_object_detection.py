import cv2
import numpy as np
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
import os
import pygame

#Initialize pygame mixer, which provides functionalities
pygame.mixer.init()

''' Load the pre-trained MobileNetV2 model to make predictions on
New images by passing the images through the network'''
model=MobileNetV2(weights='imagenet')

#Directory to save screenshots in the local storage
screenshot_dir = "screenshots"
os.makedirs(screenshot_dir,exist_ok=True) #Create directory if not exists.

def call_harmful_objects(frame):
    #Preprocess the frame with size
    frame =cv2.resize(frame,(224,224))
    x =np.expand_dims(frame,axis=0)
    x =preprocess_input(x)

    #Make predictions with x input
    preds = model.predict(x)

    #Decode predictions 
    decoded_preds =decode_predictions(preds,top=3)[0]

    #Check if any of the top predictions indicate harmful objects
    harmful_objects =[]
    for pred in decoded_preds:
        if pred[1] in ['revolver', 'assault_rifle', 'syringe', 'medicine_chest', 'chainsaw', 'bow']:
            harmful_objects.append(pred[1])

    return harmful_objects #Function definiton ending

# Initialize video capture
cap =cv2.VideoCapture(0)

# Counter for screenshot filenames
screenshot_counter=1

# Load alarm sound
alarm_sound =pygame.mixer.Sound("alarm.wav")

while True:
    #Capture frame-by-frame
    ret,frame =cap.read()
    
    #Perform harmful object detection
    harmful_objects =call_harmful_objects(frame)
    
    #Display harmful objects if any
    if harmful_objects:
        for obj in harmful_objects:
            cv2.putText(frame, obj, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
            '''Top-left,font type, Font size, Color BGR, Text in pixel, Smooth edges=LINE_AA'''
        #Play alarm sound
        alarm_sound.play()
            
        #Take screenshot and store in local path
        screenshot_filename =os.path.join(screenshot_dir, f"screenshot_{screenshot_counter}.png")
        cv2.imwrite(screenshot_filename,frame)
        #Stores and name file
        print(f"Screenshot saved as {screenshot_filename}")
        screenshot_counter +=1
    
    #Display the resulting frame
    cv2.imshow('Harmful Object Detection',frame)
    
    #Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

#Release video capture
cap.release()
cv2.destroyAllWindows()
