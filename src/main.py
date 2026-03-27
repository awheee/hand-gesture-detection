import cv2
from hand_tracker import HandTracker
from utils import count_fingers

def main():
    cap = cv2.VideoCapture(0)

    tracker = HandTracker()

    while True:
        success, img = cap.read()
        if not success:
            break

        img = tracker.find_hands(img)
        landmarks = tracker.get_landmarks(img)

        finger_count = count_fingers(landmarks)

        # Display result
        cv2.putText(img, f'Fingers: {finger_count}', (50, 100),
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)

        cv2.imshow("Hand Gesture Detector", img)

        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()