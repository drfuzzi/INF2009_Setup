#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")

# Capture one frame
ret, frame = cap.read()

# Save the captured image
cv2.imwrite('captured_image.jpg', frame)

# Release the webcam
cap.release()

print("Image captured and saved!")
