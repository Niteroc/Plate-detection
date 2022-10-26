import cv2
import os

for i in range(1,10):

    image = cv2.imread('plaque'+ str(i) + '.jpg')
    image = cv2.resize(image, (620,480))
    image_nuance = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image_bilaterale = cv2.bilateralFilter(image_nuance, 11, 17, 17)
    image_contour = cv2.Canny(image_bilaterale, 100, 200)

    contours, _ = cv2.findContours(image_contour.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    contours_tries = sorted(contours, key=cv2.contourArea, reverse=True)[:30]
    quadrilateres = []

    for c in contours_tries:
        perimetre = cv2.arcLength(c, True)
        polygone = cv2.approxPolyDP(c, 0.02 * perimetre, True)
        cv2.drawContours(image_contour,[polygone], 0, (150), 3)
        if len(polygone) == 4: 
            quadrilateres.append(polygone)
            break

    image_contour_bis = image_contour.copy()
    j = 1

    for c in quadrilateres:
        perimetre = cv2.arcLength(c, True)
        polygone = cv2.approxPolyDP(c, 0.01 * perimetre, True)
        cv2.drawContours(image_contour_bis,[polygone], 0, (255), 3)
        x,y,w,h = cv2.boundingRect(c) 
        plate_temp = image[y:y+h,x:x+w]
        cv2.imwrite('temp_'+str(i)+ '_' +str(j)+'.png',plate_temp)
        j = j + 1

    cv2.imshow("",image_contour)
    cv2.waitKey(0)
    cv2.imshow("",image_contour_bis)
    cv2.waitKey(0)