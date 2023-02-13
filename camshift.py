import cv2
import numpy as np


def main():
    # Read the video
    cap = cv2.VideoCapture("Videos/Book.mp4")

    # Pause the video until user presses 'i' to draw the object to track
    paused = True
    while paused:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow("Draw a rectangle around the object to track and press 'i' to start tracking", frame)

        # If user presses 'i', start selecting the object to track
        k = cv2.waitKey(25)
        if k == ord('i'):
            # Select the object to track by drawing a rectangle
            roi = cv2.selectROI(frame)

            # Save the dimensions of the rectangle
            track_window = (int(roi[0]), int(roi[1]), int(roi[2]), int(roi[3]))

            # Start tracking the object
            paused = False

    # Set up the object tracker
    roi = frame[track_window[1]:track_window[1] + track_window[3], track_window[0]:track_window[0] + track_window[2]]
    hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    # Define the mask for tracking green objects
    lower_green = np.array([40, 15, 15])  # H: 40, S: 50, V: 50
    upper_green = np.array([100, 255, 255])  # H: 80, S: 255, V: 255
    mask = cv2.inRange(hsv_roi, lower_green, upper_green)
    roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0, 180])
    cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)

    term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        dst = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)

        ret, track_window = cv2.CamShift(dst, track_window, term_crit)

        pts = cv2.boxPoints(ret)
        pts = np.int0(pts)
        img2 = cv2.polylines(frame, [pts], True, 255, 2)

        cv2.imshow('Object Tracker', img2)

        k = cv2.waitKey(25) & 0xff
        if k == 27:
            break

    cv2.destroyAllWindows()
    cap.release()


if __name__ == '__main__':
    main()
