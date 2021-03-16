import cv2

img = cv2.imread("test1.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imwrite("C:\\Users\\Rex\\Desktop\\opencv\\test"+"55"+ '.jpg', img)
cv2.imshow("test", img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()