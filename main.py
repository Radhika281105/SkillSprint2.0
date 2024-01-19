import cv2
import numpy as np

# img=cv2.imread("modi.jpg")
# img2=cv2.resize(img,(540,480))
# # cv2.imshow("Image",img2)
# print(img2.shape)
# img4=cv2.rotate(img2, cv2.ROTATE_90_COUNTERCLOCKWISE)
# # cv2.imshow("Image1",img4)
# imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# imgblur=cv2.GaussianBlur(imggray,(9,9),0)
# imgblur3=cv2.GaussianBlur(imggray,(3,3),0)
# imgcanny=cv2.Canny(imggray,100,100)
# cv2.imshow("Image Gray",imggray)
# cv2.imshow("Image Blur 3",imgblur)
# cv2.imshow("Image_resize",img2)
# cv2.imshow("Image_grayscale",imggray)
# cv2.imshow("Canny Image",imgcanny)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()

import datetime as dt

cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)

while True:
    ret, frame = cap.read()
    date_time=str(dt.datetime.now())
    cv2.putText(frame,"RADHIKA SAXENA",(10,100),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2,cv2.LINE_AA)
    frame=cv2.putText(frame,date_time,(10,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2,cv2.LINE_AA)
    cv2.line(frame,(200,200),(100,200),(255,0,0),3)
    cv2.line(frame, (100, 200), (100, 150), (255, 0, 0), 3)
    cv2.line(frame, (100, 150), (200, 200), (255, 0, 0), 3)
    cv2.circle(frame,(400,400),50,(255,255,0),0)
    cv2.rectangle(frame,(100,400),(8,470),(255,0,0),-1)  #2-thickness
    cv2.imshow("Video",frame)
    # fourcc=cv2.VideoWriter_fourcc(*'XVID')
    # out=cv2.VideoWriter('output.avi',fourcc,50,(640,480),True)
    if cv2.waitKey(1)==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

# img=cv2.imread("modi.jpg")
# cv2.putText(img,"radhika",(100,100),cv2.FONT_HERSHEY_COMPLEX,2,(255,255,0),2,cv2.LINE_AA)
# cv2.imshow("Image",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# img=cv2.imread("modi.jpg",-1)
# cv2.imshow("Image",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# import cv2
# import numpy as np
#
# # Create a black image
# img = np.zeros((512, 512, 3), np.uint8)
#
# # Display the image to create the window
# cv2.imshow('image', img)
# cv2.waitKey(1)  # Needed to create the window
#
# # Initialize variables for coordinates
# coordinates = ""
#
# # Define the mouse callback function using a lambda function
# cv2.setMouseCallback('image', lambda event, x, y, flags, param:
#     [print(f'Mouse event: {event}, Coordinates: ({x}, {y})'),
#      (cv2.putText(img, f'{x},{y}', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2, cv2.LINE_AA) if event == cv2.EVENT_LBUTTONDOWN else None)][-1])
#
# # Main loop
# while True:
#     cv2.imshow('image', img)
#     if cv2.waitKey(1) == ord("q"):
#         break
#
# cv2.destroyAllWindows()
