import cv2
import os
import numpy as np

subjects = ["None", "Obama"]

def detect_face(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(r"C:\Users\hardip thummar\AppData\Local\Programs\Python\Python38-32\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml")
    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.5, minNeighbors = 5)
    if len(faces) == 0:
		return None,None
	(x, y, w, h) = faces[0]
	return gray[y: y+w, x: x+h], faces[0]

def prepare_training_data(data_folder_path):
	dirs = os.listdir(data_folder_path)
	faces, labels = [], []
	for dir_name in dirs:
		if not dir_name.startswith("s"):
			continue
		label = int(dir_name.replace("s", ""))
		subject_dir_path = data_folder_path + "/" + dir_name
		subject_image_names = os.listdir(subject_dir_path)
		for image_name in subject_image_names:
			if image_name.startswith("."):
				continue
			image_path = subject_dir_path + "/" + image_name
			image = cv2.imread(image_path)
			cv2.imshow("Training on image..", image)
			cv2.waitKey()
			face, rect = detect_face(image)
			if face is not None:
				faces.append(face)
				labels.append(label)
				cv2.destroyAllWindows()
				cv2.waitKey(1)
			cv2.destroyAllWindows()
	return faces, labels

print("Preparing data....")
faces, labels = prepare_training_data(r"C:\Users\hardip thummar\Desktop\face\training_data")
print("Data prepared")

print("Total Faces :", len(faces))
print("Total labels :", len(labels))

face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.train(faces, np.array(labels))

def draw_rectangle(img, rect):
	(x, y, w, h) = rect
	cv2.rectangle(img, (x, y), (x+w, y+h), (0,255,0), 2)

def draw_text(img, text, x, y):
	cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)

def prediction(test_img):
	img = test_img.copy()
	face, rect = detect_face(img)
	label_id,confidence = face_recognizer.predict(face)
	label_text = subjects[label_id]
	draw_rectangle(img, rect)
	draw_text(img, label_text, rect[0], rect[1]-5)
	return img

print("Predicting images..")

test_img1 = cv2.imread(r"C:\Users\hardip thummar\Desktop\face\collection\ob&biden.jpg")
test_img2 = cv2.imread(r"C:\Users\hardip thummar\Desktop\face\collection\cumings.jpg")
test_img3 = cv2.imread(r"C:\Users\hardip thummar\Desktop\face\collection\ob&jin3.jpg")
test_img4 = cv2.imread(r"C:\Users\hardip thummar\Desktop\face\collection\ob1.jpg")
test_img5 = cv2.imread(r"C:\Users\hardip thummar\Desktop\face\collection\ob2.jpg")
test_img6 = cv2.imread(r"C:\Users\hardip thummar\Desktop\face\collection\repoter.jpg")
test_img7 = cv2.imread(r"C:\Users\hardip thummar\Desktop\face\collection\trump&x.jpg")


predicted_img = prediction(test_img2)
# print(f"Prediction complete with {confidence} confidence")
cv2.imshow(subjects[1], predicted_img)
cv2.waitKey()
cv2.destroyAllWindows()