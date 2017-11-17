import cv2
import json
image = "nxnrcwja1poqmf.jpg"
x1 = []
x2 = []
y1 = []
y2 = []
with open('ca3a4be7e3884c21b50b7f78b914d92c.json') as json_data:

	#jsonRead = json.read()
	jsonData = json.load(json_data)
	length = len(jsonData["meters"])
	print jsonData['meters'][0]['coordinates']['xmin']
	xmin = jsonData['meters'][0]['coordinates']['xmin']
	xmax = jsonData['meters'][0]['coordinates']['xmax']
	ymin = jsonData['meters'][0]['coordinates']['ymin']
	ymax = jsonData['meters'][0]['coordinates']['ymax']
	boxWid = xmax-xmin
	boxHei = ymax-ymin
	img = cv2.imread(image)
	crop_img = img[ymin:ymin+boxHei,xmin:boxWid+xmin]
	cv2.imshow("image",crop_img)
	cv2.waitKey(0)

	print len(jsonData['meters'][0])
	for i in range(0,int(len(jsonData['meters'][0]))):

		x1 = jsonData['meters'][0]['calibration'][i]['x1']
		y1 = jsonData['meters'][0]['calibration'][i]['y1']
		x2 = jsonData['meters'][0]['calibration'][i]['x2']
		y2 = jsonData['meters'][0]['calibration'][i]['y2']
		boxWidth = x2-x1
		boxHeight = y2-y1
		img = cv2.imread(image)
		crop_img1 = img[y1:y1+boxHeight,x1:boxWidth+x1]
		cv2.imshow("image"+str(i),crop_img1)
		cv2.waitKey(0)

	cv2.destroyAllWindows()
