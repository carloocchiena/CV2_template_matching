
# python template_matching.py --image images/image_where_to_search.png --template images/item_to_be_searched.png

import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, required=True,
	help="path to input image where we'll apply template matching")
ap.add_argument("-t", "--template", type=str, required=True,
	help="path to template image")
args = vars(ap.parse_args())

print("[INFO] loading images...")
image = cv2.imread(args["image"])
template = cv2.imread(args["template"])
cv2.imshow("Image", image)
cv2.imshow("Template", template)

imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
templateGray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

print("[INFO] performing template matching...")
result = cv2.matchTemplate(imageGray, templateGray,
	cv2.TM_CCOEFF_NORMED)
(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(result)

(startX, startY) = maxLoc
endX = startX + template.shape[1]
endY = startY + template.shape[0]

cv2.rectangle(image, (startX, startY), (endX, endY), (255, 0, 0), 3)

cv2.imshow("Output", image)
cv2.waitKey(0)