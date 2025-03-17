import cv2
import time
import os
from eye_movement import process_eye_movement
from head_pose import process_head_pose
from mobile_detection import process_mobile_detection

cap = cv2.VideoCapture(0)
