import cv2

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')



cap = cv2.VideoCapture(0)

while True:

	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5 , minNeighbors = 5)
	for(x,y,w,h) in faces:
		print(x,y,w,h)
		roi_gray = gray[y:y+h , x:x+w]
		roi_color = frame[y:y+h , x:x+w]
		img_item = "my-img.png"
		cv2.imwrite(img_item, roi_gray)

		color = (0, 255, 0)

		stroke = 1
		width = x+w
		height = y+h

		cv2.rectangle(frame , (x,y), (width, height), color , stroke)




	cv2.imshow('frame', frame)
	if cv2.waitKey(20) & 0xFF == ord('c'):
		break


cap.release()
cv2.destroyAllWindows()