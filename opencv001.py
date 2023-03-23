import cv2
import numpy
import PIL

# Video
frameWidth = 640
frameHeight = 480

#Video Source
#cap = cv2.VideoCapture('videos/traffic.mp4') #自分のmp4のpathを入力
cap = cv2.VideoCapture(0)
cap_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
cap_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
size =(cap_width,cap_height)
num_of_frame = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
fps = int(cap.get(cv2.CAP_PROP_FPS))
print(cap_width,cap_height,num_of_frame,fps)

while True:
    ret, img = cap.read()
    #img = cv2.resize(img, (frameWidth, frameHeight))
    img2 = cv2.flip(img,1)
    cv2.imshow('Video', img2)
    #print('ret=', ret)

    # qを押すと止まる。
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
