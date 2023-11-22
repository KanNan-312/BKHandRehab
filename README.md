# BKHandRehab: A gesture-based gaming application for post-stroke hand rehabilitation #
## About this project ##
Hi all, welcome to my capstone project!

This project aims to create a hand gesture-based gaming application for post-stroke hand rehabilitation. We adopted a Leap Motion Controller for hand skeleton extraction and an underlying SVM model for gesture recognition.

Note: The current application supports Windows 10/11 only.

## Documents ##
Our project report, including every specific details of this project can be found [here](Final%20Report.pdf)

The demo video of our application can be found [here](BK%20Hand%20Rehab%20Demo.mp4)

## Prerequesite ##
1. LeapMotion Controller
2. Leap Motion Hand Tracking Software. Installation file can be found [here](https://www.ultraleap.com/tracking/gemini-hand-tracking-platform/)

## Installations ##
1. Create conda environment with python 3.9 and activate it
```
conda create -n myenv python=3.9
conda activate myenv
```
2. Move to the code directory and install dependencies
```
cd bk_hand_rehab
pip install -r requirements.txt
```

## Run the application ##
```
python main.py
```