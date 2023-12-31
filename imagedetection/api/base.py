import cv2
import numpy as np
import time
import os
import re

# tensorflow imports
import tensorflow as tf
import tensorflow_hub as hub
# from core import utils
# from core.config import cfg
# from tensorflow.python.saved_model import tag_constants
from datetime import datetime

from ultralytics import YOLO

# import onnxruntime as ort



class Serial_DetectionAPIView():

    # Instance attribute
    def __init__(self):
        print("loading model...")
        # weights = 'yolov8-640-v1'
        # self.saved_model_loaded = tf.saved_model.load(
        #     weights, tags=[tag_constants.SERVING]
        # )

        # # Load the TFLite model and allocate tensors.
        # self.interpreter = tf.lite.Interpreter(model_path="best_float32.tflite")
        self.model = YOLO("imagedetection/api/best.pt")
        # self.model_onnx = ort.InferenceSession("best.onnx")


        self.loaded_model_digits = tf.keras.models.load_model(
            ('imagedetection/api/my_model_digits_v3_3.h5'),
            custom_objects={'KerasLayer':hub.KerasLayer}
        )

        self.loaded_model_aphabets = tf.keras.models.load_model(
            ('imagedetection/api/my_model_alphabets_v3_5.h5'),
            custom_objects={'KerasLayer':hub.KerasLayer}
        )


        print("done loading model...")

    


    def detection(self, original_image):

        start_time1 = time.time()
        results = self.model.predict(original_image, conf=0.55)
        result = results[0]

        bounding_boxes_list = []
        ori_image = original_image.copy()
        for i in range(len(result.boxes)):
            box = result.boxes[i]
            class_id = result.names[box.cls[0].item()]
            cords = box.xyxy[0].tolist()
            cords = [round(x) for x in cords]
            conf = round(box.conf[0].item(), 2)

            xmin=cords[0]
            ymin=cords[1]
            xmax=cords[2]
            ymax=cords[3]
            bounding_boxes_list.append((cords[0], cords[1], cords[2], cords[3]))

            # crop_path = r"C:\Users\MMaleka\Desktop\traceability_api_backend\detections\complete\test_1"
            # cropped_img = ori_image[int(ymin)-1:int(ymax)+1, int(xmin)-1:int(xmax)+1]
            # now = datetime.now()
            # current_time = now.strftime("%H:%M:%S")
            # img_name = str(i)+"_"+str(current_time).replace(":", "-")+'.jpg'
            # img_path = os.path.join(crop_path, img_name)
            # cv2.imwrite(img_path, cropped_img)

            # cv2.rectangle(
            #     original_image, 
            #     (int(xmin)-4, int(ymin)-4), 
            #     (int(xmax)+4, int(ymax)+4), 
            #     (0, 0, 255), 
            #     2
            # )

            # cv2.putText(
            #     original_image, 
            #     str(conf), 
            #     (int(xmin)+50, int(ymin) - 15), 
            #     cv2.FONT_HERSHEY_PLAIN, 
            #     2, 
            #     (0, 0, 255), 
            #     2
            # )

        # crop_path = r"C:\Users\mmaleka\Desktop\data"
        # now = datetime.now()
        # current_time = now.strftime("%H:%M:%S")
        # current_date = now.strftime("%B %d, %Y")
        # img_name = str(current_date).replace(" ", "_").replace(",", "_") + str(current_time).replace(":", "-").replace(" ", "_")+'.jpg'
        # print("img_name: ", img_name)
        # img_path = os.path.join(crop_path, img_name)
        # cv2.imwrite(img_path, original_image)

        print("box - process is complete...: ", time.time()-start_time1)
        scores_list=[]
        return bounding_boxes_list, scores_list, ori_image


    def detection_onnx(self, original_image):

        inputs = self.model_onnx.get_inputs()
        print(len(inputs))

        bounding_boxes_list=[]
        scores_list=[]
        ori_image=[]
        return bounding_boxes_list, scores_list, ori_image
    
    def detect_digits(self, bb_digits, frame, original_image):

        labels = ['0','1','2','3','4','5','6','7','8','9']
        bb_digits_sorted=sorted(bb_digits, key=lambda x: x[0])
        shell_no = ''
        X3 = []
        for i in range(len(bb_digits_sorted)):
            # try:
                xmin=bb_digits_sorted[i][0]
                ymin=bb_digits_sorted[i][1]
                xmax=xmin+bb_digits_sorted[i][2]
                ymax=ymin+bb_digits_sorted[i][3]
                # prinnow = datetime.now()t("xmin, ymin, xmax, ymax: ", xmin, ymin, xmax, ymax)
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                cropped_img = original_image[int(ymin)-1:int(ymax)+1, int(xmin)-1:int(xmax)+1]
                

                
                resized_img_test = cv2.resize(cropped_img,(50,50))
                resized_img_test_scale = resized_img_test / 255
                X3.append(resized_img_test_scale)
                # x = np.expand_dims(resized_img_test_scale, axis=0)
                # prediction = self.loaded_model_digits.predict(x)
                # y_predicted_labels = [np.argmax(i) for i in prediction]
                # y_predicted_labels = np.array(y_predicted_labels)
                # prediction_label = labels[y_predicted_labels[0]].upper()

                # crop_path = r"C:\Users\MMaleka\Desktop\traceability_api_backend\detections\complete\digits\{}".format(prediction_label)
                # # Check if the directory exists
                # if not os.path.exists(crop_path):
                #     # If it doesn't exist, create it
                #     os.makedirs(crop_path)

                
                # img_name = str(prediction_label)+"_"+str(current_time).replace(":", "-")+'.jpg'
                # img_path = os.path.join(crop_path, img_name)
                # cv2.imwrite(img_path, cropped_img)

                # cv2.rectangle(
                #     original_image, 
                #     (int(xmin)-4, int(ymin)-4), 
                #     (int(xmax)+4, int(ymax)+4), 
                #     (0, 0, 255), 
                #     2
                #     )
                # cv2.putText(
                #     frame, 
                #     prediction_label, 
                #     (int(xmin), int(ymin) - 15), 
                #     cv2.FONT_HERSHEY_PLAIN, 
                #     2, 
                #     (255, 0, 0), 
                #     2
                #     )

                # save image to retrain the model.
                # This is the complete image
                # crop_path = r"C:\Users\MMaleka\Desktop\traceability_api_backend\detections\complete"
                # img_name = str(i)+"_"+str(current_time).replace(":", "-")+'.jpg'
                # img_path = os.path.join(crop_path, img_name)
                # cv2.imwrite(img_path, cropped_img)

                

            #     shell_no = shell_no+prediction_label

            # except Exception as e:
            #     shell_no="---"
            #     print("error detecting digits: ", e)


        start_time2 = time.time()
        try:
            X3 = np.array(X3)
            print("X3.shape: ", X3.shape)
            predictions=self.loaded_model_digits.predict(X3)
            y_predicted_labels = [np.argmax(i) for i in predictions]
            print(y_predicted_labels)
            for index in y_predicted_labels:
                prediction_label = labels[index].upper()
                shell_no = shell_no+prediction_label
        except Exception as e:
                shell_no="---"
                print("error detecting digits: ", e)
        print("digits1 process complete in: ", time.time()-start_time2)

        

        return shell_no
    


    def detect_alphabets(self, bb_alphabets, frame, original_image):

        labels = ['a','b','c','d','e','f','g','h','j','k','l','m','n','p','r','s','t','u','v','w','x','y','z']
        bb_alphabets_sorted=sorted(bb_alphabets, key=lambda x: x[0])
        batch = ''
        X2 = []
        for i in range(len(bb_alphabets_sorted)):
            xmin=bb_alphabets_sorted[i][0]
            ymin=bb_alphabets_sorted[i][1]
            xmax=xmin+bb_alphabets_sorted[i][2]
            ymax=ymin+bb_alphabets_sorted[i][3]
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            cropped_img = original_image[int(ymin)-1:int(ymax)+1, int(xmin)-1:int(xmax)+1]


            resized_img_test = cv2.resize(cropped_img,(50,50))
            resized_img_test_scale = resized_img_test / 255
            # x = np.expand_dims(resized_img_test_scale, axis=0)
            X2.append(resized_img_test_scale)

            # prediction = self.loaded_model_aphabets.predict(x)
            # # prediction_1 = self.loaded_model_aphabets_v1.predict(x)
            # # prediction_2 = self.loaded_model_aphabets_v2.predict(x)
            
            # y_predicted_labels = [np.argmax(i) for i in prediction]
            # # y_predicted_labels_1 = [np.argmax(i) for i in prediction]
            # # y_predicted_labels_2 = [np.argmax(i) for i in prediction]
            # y_predicted_labels = np.array(y_predicted_labels)
            # # y_predicted_labels_1 = np.array(y_predicted_labels_1)
            # # y_predicted_labels_2 = np.array(y_predicted_labels_2)

            # # softmax = tf.nn.softmax(prediction)
            # # print("y_predicted_labels: ", y_predicted_labels[0]," softmax: ", softmax[y_predicted_labels[0]])

            # prediction_label = labels[y_predicted_labels[0]].upper()
            # prediction_label_1 = labels[y_predicted_labels_1[0]].upper()
            # prediction_label_2 = labels[y_predicted_labels_2[0]].upper()

            # # save image to retrain the model.
            # crop_path = r"C:\Users\MMaleka\Desktop\traceability_api_backend\detections\complete\alphabets\{}".format(prediction_label)
            # # Check if the directory exists
            # if not os.path.exists(crop_path):
            #     # If it doesn't exist, create it
            #     os.makedirs(crop_path)

            # img_name = str(prediction_label)+"_"+str(current_time).replace(":", "-")+'.jpg'
            # img_path = os.path.join(crop_path, img_name)
            # cv2.imwrite(img_path, cropped_img)

            # cv2.rectangle(
            #     original_image, 
            #     (int(xmin)-2, int(ymin)-2), 
            #     (int(xmax)+2, int(ymax)+2), 
            #     (0, 0, 255), 
            #     2
            #     )
            # cv2.putText(
            #     frame, 
            #     prediction_label, 
            #     (int(xmin), int(ymax)+40), 
            #     cv2.FONT_HERSHEY_PLAIN, 
            #     2, 
            #     (255, 0, 0), 
            #     2
            #     )

            # crop_path = r"C:\Users\MMaleka\Desktop\traceability_api_backend\detections\complete\test_1"
            # # cropped_img = ori_image[int(ymin)-1:int(ymax)+1, int(xmin)-1:int(xmax)+1]
            # now = datetime.now()
            # current_time = now.strftime("%H:%M:%S")
            # img_name = str(current_time).replace(":", "-")+'.jpg'
            # img_path = os.path.join(crop_path, img_name)
            # cv2.imwrite(img_path, frame)

            # batch = batch+prediction_label


        start_time2 = time.time()
        try:
            X2 = np.array(X2)
            print("X2.shape: ", X2.shape)
            predictions=self.loaded_model_aphabets.predict(X2)
            y_predicted_labels = [np.argmax(i) for i in predictions]
            print(y_predicted_labels)
            for index in y_predicted_labels:
                prediction_label = labels[index].upper()
                batch = batch+prediction_label
        except Exception as e:
                batch="------"
                print("error detecting letters: ", e)
        print("alphabets1 process complete in: ", time.time()-start_time2)

        print("batch: ", batch)
        # arr = arr.reshape(6,50,50,3)
        # prediction = self.loaded_model_aphabets.predict(x)
        # print("prediction: ", prediction)

        return batch
    



    def speak(self, name):
        print("My name is {}".format(name))




# serial = Serial_DetectionAPIView()
# img = cv2.imread('2008.jpg')
# (bounding_boxes_list, scores_list) = serial.detection(img)












