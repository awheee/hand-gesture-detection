def count_fingers(landmarks):
    if not landmarks or len(landmarks) < 21:
        return 0

    fingers = []

    # Finger tip indices
    tips = [4, 8, 12, 16, 20]

    # Thumb (horizontal check)
    if landmarks[tips[0]][1] > landmarks[tips[0] - 1][1]:
        fingers.append(1)
    else:
        fingers.append(0)

    # Other fingers (vertical check)
    for i in range(1, 5):
        if landmarks[tips[i]][2] < landmarks[tips[i] - 2][2]:
            fingers.append(1)
        else:
            fingers.append(0)

    return sum(fingers)