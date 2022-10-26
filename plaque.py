import imutils
import cv2
import os

image = cv2.imread('plaque.jpg')
image = imutils.resize(image, width=300)

#to gray scale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# apply noise reducing filter
gray_image = cv2.bilateralFilter(gray_image, 11,17,17)

# apply canny border detection 
canny_res = cv2.Canny(gray_image, 30, 200)

# find all the contours
contours, _ = cv2.findContours(canny_res.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
img_test = image.copy()
# sort and get the 5 most marked contour
sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)[:100]
c_sort = [];

for c in sorted_contours:
    perimeter = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.01 * perimeter, True)
    cv2.drawContours(img_test,[approx], 0, (0), 3)
    if len(approx) == 4: 
        c_sort.append(approx)
        break

img_test_ = img_test.copy();

for c in c_sort:
    perimeter = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.01 * perimeter, True)
    cv2.drawContours(img_test_,[approx], 0, (255), 3)
    

cv2.imshow("image with detected license plate", img_test)
cv2.waitKey(0)
cv2.imshow("image with detected license plate", img_test_)
cv2.waitKey(0)