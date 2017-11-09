import cv2
import glob

images=glob.glob("*.jpg")

for image in images:
	img=cv2.imread(image,1)
	re=cv2.resize(img,(350,320))
	cv2.imshow("Hey",re)
	cv2.waitKey(500)
	cv2.destroyAllWindows()
	cv2.imwrite("b_"+image,re)

