import cv2
import random 
import os


file_dir = "" # images path 
save_dir = "" # save faces images path 

def myImg(image_dir, path):
    image = cv2.imread(image_dir)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=3,
        minSize=(30, 30))

    print("[INFO] Found {0} Faces.".format(len(faces)))

    for (x, y, w, h) in faces:
        random_id = random.randrange(1000,10000)
        roi_color = image[y:y + h, x:x + w]
        print("[INFO] Object found. Saving locally.")
        cv2.imwrite(path + "/" + str(random_id) + '_faces.jpg', roi_color)


def file_picker(filedir, img_path):
    files = os.listdir(filedir)
    i=0
    for file in files:
        i+=1
        myimg = filedir + "/" + file
        save_img_path = img_path
        myImg(myimg, save_img_path)


file_picker(file_dir, save_dir)
