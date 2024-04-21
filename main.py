import numpy
import cv2
import sys

# img = cv2.imread('img.jpg')
cap = cv2.VideoCapture(0)  # , cv2.CAP_DSHOW)

cap.set(3, 640)
cap.set(4, 480)


classNames = []
classFile = 'coco.names'
with open(classFile, 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

# 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
# 'frozen_inference_graph.pb'
weightsPath = 'frozen_inference_graph.pb'

net = cv2.dnn_DetectionModel(weightsPath, configPath)
net.setInputSize(320, 320)
net.setInputScale(1.0 / 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

while True:
    ret, img = cap.read()
    classIds, confs, bbox = net.detect(img, confThreshold=0.5)
    print(classIds, bbox)
    if len(classIds) != 0:
        for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
            cv2.rectangle(img, box, color=(0, 255, 0), thickness=2)
            cv2.putText(img, classNames[classId-1].upper(), (box[0]+10, box[1]+20),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
            cv2.putText(img, str(round(confidence*100, 2)), (box[0]+150, box[1]+20),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("output", img)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cap.release()
cv2.destroyAllWindows()
