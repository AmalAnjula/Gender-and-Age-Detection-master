#A Gender and Age Detection program by Mahesh Sawant

import cv2
import math
import argparse
import threading
import time
import numpy as np
import statistics
import subprocess as sp
counter=0

global v_thread
v_thread=1

array=[]

def highlightFace(net, frame, conf_threshold=0.7):
    frameOpencvDnn=frame.copy()
    frameHeight=frameOpencvDnn.shape[0]
    frameWidth=frameOpencvDnn.shape[1]
    blob=cv2.dnn.blobFromImage(frameOpencvDnn, 1.0, (300, 300), [104, 117, 123], True, False)

    net.setInput(blob)
    detections=net.forward()
    faceBoxes=[]
    for i in range(detections.shape[2]):
        confidence=detections[0,0,i,2]
        if confidence>conf_threshold:
            x1=int(detections[0,0,i,3]*frameWidth)
            y1=int(detections[0,0,i,4]*frameHeight)
            x2=int(detections[0,0,i,5]*frameWidth)
            y2=int(detections[0,0,i,6]*frameHeight)
            faceBoxes.append([x1,y1,x2,y2])
            cv2.rectangle(frameOpencvDnn, (x1,y1), (x2,y2), (0,255,0), int(round(frameHeight/150)), 8)
    return frameOpencvDnn,faceBoxes

def worker_function():
    


    try:
        sp.run(['taskkill /f /FI "WINDOWTITLE eq Slidshow*"']) 
        time.sleep(1)

    except:
        print("error stop add")
        
    try:

        
            # Path to the Python script you want to run
        script_path = r"C:\Users\Amal\Downloads\Gender-and-Age-Detection-master\addrun.py"
        # Run the script
        sp.run(["python", script_path])


    except:
        print("error run adds")


        

parser=argparse.ArgumentParser()
parser.add_argument('--image')

args=parser.parse_args()

faceProto="opencv_face_detector.pbtxt"
faceModel="opencv_face_detector_uint8.pb"
ageProto="age_deploy.prototxt"
ageModel="age_net.caffemodel"
genderProto="gender_deploy.prototxt"
genderModel="gender_net.caffemodel"

MODEL_MEAN_VALUES=(78.4263377603, 87.7689143744, 114.895847746)
ageList=['(0-2)', '(4-6)', '(8-12)', '(15-20)', '(25-32)', '(38-43)', '(48-53)', '(60-100)']
genderList=['Male','Female']

faceNet=cv2.dnn.readNet(faceModel,faceProto)
ageNet=cv2.dnn.readNet(ageModel,ageProto)
genderNet=cv2.dnn.readNet(genderModel,genderProto)

video=cv2.VideoCapture(args.image if args.image else 0)
padding=20






def writeInfo(fileInfo):

    fileInfo=fileInfo.replace(" ", "")
    f = open("first_characters.txt", "w")
    f.write(fileInfo)
    f.close()



old_time=time.time()
while cv2.waitKey(1)<0 :


    nowTime=time.time()
    if(nowTime-old_time>1):
        old_time= ( time.time())
        counter=counter+1
        #print(counter)
        if(counter>5):
            counter=0
            #find unique values in array along with their counts
            #vals, counts = np.unique(array, return_counts=True)
            #find mode
            #mode_value = np.argwhere(counts == np.max(counts))

            print (statistics.mode(array))
            writeInfo(statistics.mode(array))
            array.clear()

                        # Create a virtual thread
            virtual_thread = threading.Thread(target=worker_function)

            # Start the virtual thread
            virtual_thread.start()
         

    
    hasFrame,frame=video.read()
    if not hasFrame:
        cv2.waitKey()
        break
    #cv2.imshow("img", frame)

    resultImg,faceBoxes=highlightFace(faceNet,frame)
    if not faceBoxes:
        print("No face detected")
        counter=0
        array.clear()
         

    for faceBox in faceBoxes:
        face=frame[max(0,faceBox[1]-padding):
                   min(faceBox[3]+padding,frame.shape[0]-1),max(0,faceBox[0]-padding)
                   :min(faceBox[2]+padding, frame.shape[1]-1)]

        blob=cv2.dnn.blobFromImage(face, 1.0, (227,227), MODEL_MEAN_VALUES, swapRB=False)
        genderNet.setInput(blob)
        genderPreds=genderNet.forward()
        gender=genderList[genderPreds[0].argmax()]
        #print(f'Gender: {gender}')

        ageNet.setInput(blob)
        agePreds=ageNet.forward()
        age=ageList[agePreds[0].argmax()]
        #print(f'Age: {age[1:-1]} years')

        #print(f'Age: {age[1:-1]} y Gender: {gender}')
        #print(counter)

        cv2.putText(resultImg, "Counter "+str(counter),(10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,255), 2, cv2.LINE_AA)
        
        cv2.putText(resultImg, f'{gender}, {age}', (faceBox[0], faceBox[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,255), 2, cv2.LINE_AA)
        cv2.imshow("Detecting age and gender", resultImg)
        array.append( f'{gender}, {age}')


# Wait for the virtual thread to complete (optional)
v_thread=0
