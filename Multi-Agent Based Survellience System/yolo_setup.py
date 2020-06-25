import cv2
import argparse
import numpy as np
classes = None
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=False, default='9.jpg',
                help = 'path to input image')
ap.add_argument('-c', '--config', required=False, default='star.cfg',
                help = 'path to yolo config file')
ap.add_argument('-w', '--weights', required=False, default='star_last.weights', # 3900 loss 0.87, # 4000+ loss unknown
                help = 'path to yolo pre-trained weights')
ap.add_argument('-cl', '--classes', required=False, default='star.txt',
                help = 'path to text file containing class names')
args = ap.parse_args()

args.weights = 'star_3900.weights'
args.config = 'star.cfg'
args.classes = 'star.txt'
classes_file = 'star.txt'
def get_output_layers(net):
    
    layer_names = net.getLayerNames()
    
    output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

    return output_layers

def draw_prediction(img, class_id, confidence, x, y, x_plus_w, y_plus_h,classes, confidences,i,COLORS):
    label = str(classes[class_id])
    print(label)
    print(label + " Confidence: " + str(confidences[i]) 
        + " x:" + str(x) 
        + " y:" +  str(y) 
        + " x_plus_w:" + str(x_plus_w) 
        + " y_plus_h:" + str(y_plus_h))
    color = COLORS[class_id]

    cv2.rectangle(img, (x,y), (x_plus_w,y_plus_h), color, 2)

    cv2.putText(img, label, (x-10,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
with open(classes_file, 'r') as f:
	classes = [line.strip() for line in f.readlines()]
COLORS = np.random.uniform(0, 255, size=(len(classes), 3))
def predict(image):
	
	Width = image.shape[1]
	Height = image.shape[0]
	scale = 0.00392
	net = cv2.dnn.readNet(args.weights, args.config)
	blob = cv2.dnn.blobFromImage(image, scale, (416,416), (0,0,0), True, crop=False)
	net.setInput(blob)
	outs = net.forward(get_output_layers(net))
	class_ids = []
	confidences = []
	boxes = []
	conf_threshold = 0.5
	nms_threshold = 0.4
	for out in outs:
	    for detection in out:
	        scores = detection[5:]
	        class_id = np.argmax(scores)
	        confidence = scores[class_id]
	        if confidence > 0.5:
	            center_x = int(detection[0] * Width)
	            center_y = int(detection[1] * Height)
	            w = int(detection[2] * Width)
	            h = int(detection[3] * Height)
	            x = center_x - w / 2
	            y = center_y - h / 2
	            class_ids.append(class_id)
	            confidences.append(float(confidence))
	            boxes.append([x, y, w, h])
	indices = cv2.dnn.NMSBoxes(boxes, confidences, conf_threshold, nms_threshold)
	for i in indices:
	    i = i[0]
	    box = boxes[i]
	    x = box[0]
	    y = box[1]
	    w = box[2]
	    h = box[3]

	    draw_prediction(image, class_ids[i], confidences[i], round(x), round(y), round(x+w), round(y+h),classes, confidences,i,COLORS)
	cv2.namedWindow("Multi-Agent Based Surveillence System",cv2.WINDOW_AUTOSIZE)
	cv2.moveWindow("Multi-Agent Based Surveillence System",0,0)
	cv2.imshow("Multi-Agent Based Surveillence System", image)
	# cv2.imwrite("frame.jpg",image)
	# cv2.waitKey(0)
def camera_prediction():
    cam = cv2.VideoCapture(0)
    while True:
        flag, image = cam.read()
        if flag:
        	# cv2.imshow("img", image)
        	predict(image)
        if cv2.waitKey(1) == 27:
        	cam.release()
        	break
# camera_prediction()
def video_prediction(video_path):
	cap = cv2.VideoCapture(video_path)
	nframe = cap.get(cv2.CAP_PROP_FRAME_COUNT)
	for x in range(int(nframe)):
		flag, image = cap.read()
		if flag:
			predict(image)
		if cv2.waitKey(1) == 27:
			cap.release()
			break
video_path = args.image
# video_prediction(video_path)
def picture_prediction(image_path):
	image = cv2.imread(image_path)
	predict(image)
	if cv2.waitKey(1) == 27:
		cv2.destroyAllWindows()
pic_path = "9.jpg"
# picture_prediction(pic_path)
