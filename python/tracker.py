import cv2
import mediapipe as mp

webcam = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands()

while webcam.isOpened():
    img = webcam.read()

    imgRGB = cv2.cvtColor(img[1], cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for hand_landmark in results.multi_hand_landmarks:
            for index, values in enumerate(hand_landmark.landmark):
                height, width, channel = img[1].shape
                cx,cy = int(values.x * width), int (values.y * height)
                print(index,cx,cy)
                if id == 0:
                    cv2.circle(img,(cx,cy), 25, (255,0,255), cv2.FILLED)

            mp_draw.draw_landmarks(img[1], hand_landmark, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("Image", img[1])
    cv2.waitKey(1)