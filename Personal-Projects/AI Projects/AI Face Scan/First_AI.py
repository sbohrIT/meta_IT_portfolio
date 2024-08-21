#!/usr/bin/python3


import cv2

#Load pre-trained data on face frontals from opencv (haar cascade algo)
trained_face_data = cv2.CascadeClassifier('frontface.xml')

# Choose an image to detect faces in
#img = cv2.imread('Frank.png')

# To capture video from webcam
webcam = cv2.VideoCapture(0) # '0' means default camera

# Iterate forever over frames
while True:

    # Read current frame
    successful_frame_read, frame = webcam.read()

    # Convert Frame to grayscale
    grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Detect faces
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_frame)

    #Draw rectangles around the faces
    for(x, y, w, h) in face_coordinates:
        cv2.rectangle(grayscaled_frame, (x,y), (x+w, y+h), (255,0,255), 2) #Top Left point, Bottom Right point, Color, line thickness
        cv2.putText(grayscaled_frame, 'UGLY', (x, y+h+40), fontScale = 3, fontFace = cv2.FONT_HERSHEY_PLAIN, color=(255, 255, 255))


    cv2.imshow('A.I. Face Detector', grayscaled_frame)
    cv2.waitKey(1)








"""
# Convert Image to grayscale
#grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Detect faces
face_coordinates = trained_face_data.detectMultiScale(img)


#Draw rectangles around the faces
for(x, y, w, h) in face_coordinates:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2) #Top Left point, Bottom Right point, Color, line thickness
#
cv2.imshow('A.I. Face Detector', img)
cv2.waitKey()



print("Code has run successfully")
"""
