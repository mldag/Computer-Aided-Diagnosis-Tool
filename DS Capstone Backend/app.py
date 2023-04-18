import uuid
import math
from PIL import Image
from flask import Flask, request, send_file, redirect, jsonify
from flask_cors import CORS
import numpy as np
import tensorflow as tf
import os
import cv2
import scipy as sc
from matplotlib import pyplot as plt
import jsonpickle

app = Flask(__name__)
CORS(app)
basedir = os.path.abspath(os.path.dirname(__file__))
uploads_path = os.path.join(basedir, 'uploads')
m = tf.keras.models.load_model("Chnet.h5")
m2 = tf.keras.models.load_model("Xray_validation4.h5")


@app.route('/sample', methods = ['GET', 'POST'])
def sample():
    if(request.method == 'GET'): # i am using get you can change whatever you want
        data = [{"A": "a",
                 "B": "b",
                 "C": "c",
               }]
        return jsonify({'data': data})

@app.route("/process_image", methods=["POST"])
def process_image():
    file_name = str(uuid.uuid4())
    print(file_name)
    file = request.files['myFile']
    file.save(os.path.join(uploads_path, file.filename))
    file_path = uploads_path + "\\" + file.filename
    file_path = str(file_path)
    single_image = cv2.imread(file_path)
    single_image = cv2.resize(single_image, (224, 224))
    single_image = cv2.cvtColor(single_image, cv2.COLOR_BGR2GRAY)
    img = single_image / 255
    img = np.asarray(img)
    img = img.reshape(1, 224, 224, 1)
    valid_pred = m2.predict(img)[0]

    valid_pred = normal_round(valid_pred)
    if valid_pred == 0:
        class_prediction = 'Error: Not an X-ray image'
        data = [file_name, class_prediction]
        return jsonify({'data': data})

    else:       
        print(normal_round(valid_pred))
        valid_classes = list({'Not Xray': 0, 'Xray' : 1})
        valid_prediction = valid_classes[valid_pred]
        print(valid_prediction)
        img = cv2.cvtColor(single_image, cv2.COLOR_BGR2RGB)
        img = img.reshape(1,224,224,3)
        y_pred = m.predict(img)[0]
        y_pred = np.argmax(y_pred)
        classes = list({'COVID': 0, 'Lung_Opacity': 1, 'Normal': 2, 'Viral Pneumonia': 3})
        class_prediction = classes[y_pred]
        weights = m.layers[-1].get_weights()[0]
        weights = np.asarray(weights)
        weights = weights.reshape(weights.shape[1], weights.shape[0])
        weights_for_predicted_class_for_this_image = weights[y_pred]
        new_model = tf.keras.models.Model(
            m.input,
            m.get_layer('conv5_block16_concat').output
        )   
        output_con_layer = new_model.predict(img)[0]
        resize_image = sc.ndimage.zoom(output_con_layer, (int(224 / output_con_layer.shape[0]),
                                                      int(224 / output_con_layer.shape[1]), 1))
        final_image = np.dot(
            resize_image.reshape(resize_image.shape[0] * resize_image.shape[1], resize_image.shape[2]),
            weights_for_predicted_class_for_this_image
        ).reshape(resize_image.shape[0], resize_image.shape[1])

        img_ = img.reshape(224, 224, 3)
        data = Image.fromarray(final_image)
        im = Image.fromarray((img_ * 255).astype(np.uint8))
        plt.figure(figsize=(4, 4))
        plt.imshow(single_image)
        plt.imshow(final_image, cmap='jet', alpha=0.3)
        plt.savefig(f'{file_name}.jpeg')
        data = [file_name, class_prediction]
        return jsonify({'data': data})


@app.route("/process_image/<file_name>", methods=["GET"])
def get_image(file_name):
    return send_file(f"{file_name}.jpeg", mimetype='image/jpeg')

def normal_round(n):
    if n < 0.75:
        return math.floor(n)
    return math.ceil(n)