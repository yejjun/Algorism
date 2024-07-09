import cv2
import sys
import mediapipe as mp
import math

def distance(p1, p2):
    return math.dist((p1.x, p1.y), (p2.x, p2.y))

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera is not opend")
    sys.exit(1)

hands = mp_hands.Hands()

while True:
    res, frame = cap.read()

    if not res:
        print("Camera error")
        break

    frame = cv2.flip(frame, 1)
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(image)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style(),
            )

            points = hand_landmarks.landmark


            fingers = 0


            if distance(points[4], points[9]) < distance(points[3], points[9]):
                fingers += 1

            for i in range(8, 21, 4):
                if distance(points[i], points[0]) < distance(points[i-1], points[0]):
                    fingers += 1
                

            if fingers == 0:
                hand_shape = "paper"
            elif fingers == 3:
                hand_shape = "scissors"
            elif fingers == 5:
                hand_shape = "rock"
            elif fingers == 2:
                hand_shape = "GOAT"
            else:
                hand_shape = ''
            cv2.putText(
                frame,
                hand_shape,
                (int(points[12].x*frame.shape[1]), int(points[12].y*frame.shape[0])), 
                cv2.FONT_HERSHEY_COMPLEX,
                3,
                (0, 255, 0),
                5,
                )

    
    cv2.imshow("Mediapipe hands", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == 27:
        break

cv2.destroyAllwindows
cap.release()
