import cv2, mediapipe, numpy, math
from cvzone.SerialModule import SerialObject

webcam = cv2.VideoCapture(0)
mp_hands = mediapipe.solutions.hands
mp_draw = mediapipe.solutions.drawing_utils
hands = mp_hands.Hands()
minSpeed = 0
maxSpeed = 255

arduino = SerialObject("/dev/cu.usbmodem101")

while webcam.isOpened():
    lmList = []
    img = webcam.read()

    imgRGB = cv2.cvtColor(img[1], cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for hand_landmark in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img[1], hand_landmark, mp_hands.HAND_CONNECTIONS)

        for index, values in enumerate(hand_landmark.landmark):
            height, width, channel = img[1].shape
            xpos, ypos = int(values.x * width), int (values.y * height)
            lmList.append([index, xpos, ypos])

        if lmList.__len__() != 0:
            x1, y1 = lmList[4][1], lmList[4][2]
            x2, y2 = lmList[8][1], lmList[8][2]

            cv2.circle(img[1], (x1,y1), 15, (0,0,255), cv2.FILLED)
            cv2.circle(img[1], (x2,y2), 15, (0,0,255), cv2.FILLED)
            cv2.line(img[1], (x1,y1), (x2,y2), (100,100,255), 3)

            distance = math.hypot(x2-x1,y2-y1)

            speed = numpy.interp(distance, [30, 300], [minSpeed, maxSpeed])
            print(speed)
            arduino.sendData([speed])   

    cv2.imshow("Image", img[1])
    cv2.waitKey(1)