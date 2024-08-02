# Harmful_Object_Detection

This project uses a pre-trained MobileNetV2 model to detect harmful objects in a real-time video feed from a webcam. If any harmful objects are detected, the script highlights them on the video frame, sounds an alarm, and saves a screenshot of the frame.

## Features

- Real-time video feed analysis using OpenCV.
- Detection of harmful objects such as revolvers, assault rifles, syringes, medicine chests, chainsaws, and bows.
- Visual indication of detected harmful objects on the video frame.
- Alarm sound played upon detection of harmful objects.
- Screenshot taken and saved when harmful objects are detected.
- It only detect harmful objects.

## Prerequisites

- Python 3.11
- OpenCV
- TensorFlow
- NumPy
- Pygame

## Script Overview

The script consists of the following main parts:

1. **Initialization:**
   - Pygame mixer is initialized for sound playback.
   - MobileNetV2 model is loaded with pre-trained ImageNet weights.
   - Directory for saving screenshots is created if it doesn't exist.

2. **Harmful Object Detection Function:**
   - The `call_harmful_objects` function preprocesses the video frame and makes predictions using the MobileNetV2 model.
   - It checks the top predictions for harmful objects and returns a list of detected harmful objects.

3. **Real-time Video Capture and Processing:**
   - The webcam video feed is captured frame-by-frame.
   - Harmful objects are detected using the `call_harmful_objects` function.
   - If harmful objects are detected, they are highlighted on the video frame, an alarm sound is played, and a screenshot is saved.
   - The processed video frame is displayed in a window.
   - The loop can be terminated by pressing the `q` key.

4. **Add alarm sound:**
   - Place an `alarm.wav` file in the project directory. You can use any alarm sound of your choice.

## Example Output

- When a harmful object is detected, the video frame displays the name of the detected object.
- An alarm sound is played to alert the user.
- Screenshots are saved in the `screenshots` directory with filenames like `screenshot_1.png`, `screenshot_2.png`, etc.

![screenshot_73](https://github.com/selvaragul-M/Harmful_Object_Detection/assets/156414212/7ccbb0b3-4a81-4c32-9924-5613170cb6ab)

![image](https://github.com/user-attachments/assets/60ee2e8d-2a29-4cd7-a35b-5c774cffda20)

