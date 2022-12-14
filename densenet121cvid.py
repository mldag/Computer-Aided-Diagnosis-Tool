# -*- coding: utf-8 -*-
"""Densenet121cvid.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aT-8h5rot9I-CaRl2wb8AabP6hX-lkYs
"""

import tensorflow as tf
tf.__version__

import os
import numpy as np
import tensorflow as tf
from keras.models import Sequential
import pathlib
import matplotlib.pyplot as plt
import cv2
from keras.preprocessing.image import ImageDataGenerator
from google.colab import drive
drive.mount('/content/drive')
from keras.metrics import TruePositives, FalsePositives, TrueNegatives, FalseNegatives, BinaryAccuracy, Precision, Recall, AUC

dataset_folder = os.path.join("/drive/MyDrive/COVID-19_Radiography_Dataset")

files_not_important = ["COVID.metadata.xlsx", 
                       "Lung_Opacity.metadata.xlsx",
                       "Normal.metadata.xlsx",
                       "README.md.txt",
                       "Viral Pneumonia.metadata.xlsx"]
for i in files_not_important:
  os.remove(os.path.join(dataset_folder, i))

import shutil
files_not_important = ["COVID/masks",
                       "Viral Pneumonia/masks"]
for i in files_not_important:
  shutil.rmtree(os.path.join(dataset_folder, i), ignore_errors=True)

datasetObject = pathlib.Path(os.path.join(dataset_folder))
images = list(datasetObject.glob("*/*/*.*"))
len(images)

image_data_generator = ImageDataGenerator(
    rescale = 1/255, vertical_flip= False, horizontal_flip=True, zoom_range=0.1, zca_whitening=False,
    samplewise_center=True, samplewise_std_normalization=True, validation_split= 0.25,
    rotation_range=0.2)
training_dataset = image_data_generator.flow_from_directory(
    dataset_folder, target_size = (224, 224), color_mode ='rgb',subset='training', batch_size=8, shuffle=True
)
valid_dataset = image_data_generator.flow_from_directory(
    dataset_folder,  target_size=(224, 224), color_mode = 'rgb', subset='validation', batch_size = 8, shuffle = True
)

image_data_generator = ImageDataGenerator(
    rescale = 0, vertical_flip= False, horizontal_flip=False, zoom_range=0, zca_whitening=False,
    samplewise_center=True, samplewise_std_normalization=True, validation_split= 0.4,
    rotation_range=0.2)
Validation_dataset = image_data_generator.flow_from_directory(
    valid_dataset, target_size = (224, 224), color_mode ='rgb',subset='training', batch_size=8, shuffle=True
)
Training_dataset = image_data_generator.flow_from_directory(
    valid_dataset,  target_size=(224, 224), color_mode = 'rgb', subset='validation', batch_size = 8, shuffle = True
)

single_batch = training_dataset.next()
images = single_batch[0]
label = single_batch[1]
plt.figure(figsize = (20, 10))
for i in range(8):
  plt.subplot(2, 4, (i + 1))
  plt.imshow(images[i])
  plt.title(label[i])
plt.show()

training_dataset.classes

training_dataset.class_indices

np.asarray(images[0]).shape

np.unique(images[0])

from keras.applications import densenet
from keras.initializers import GlorotNormal
d = densenet.DenseNet121(weights=None, include_top = False, input_shape = (224, 224, 3))
print(d.output_shape)
m = tf.keras.layers.Dropout(0.7)(d.output)
m = tf.keras.layers.GlobalAveragePooling2D()(m)                         
m = tf.keras.layers.Dropout(0.7)(m)
m = tf.keras.layers.Dense(2, kernel_initializer=GlorotNormal(),
                          activation = 'softmax', kernel_regularizer= tf.keras.regularizers.L2(0.0001),
                          bias_regularizer= tf.keras.regularizers.L2(0.0001))(m)
m = tf.keras.models.Model(inputs = d.input, outputs = m)
m.load_weights("chexnet-weights/brucechou1983_CheXNet_Keras_0.3.0_weights.h5", by_name=True, skip_mismatch=True)
for layer in m.layers[:200]:
    layer.trainable = False
for layer in m.layers[200:]:
    layer.trainable = True

m.compile(optimizer = tf.keras.optimizers.Adam(learning_rate = 0.0001)
          , loss = 'categorical_crossentropy', metrics =  [TruePositives(name='tp'),
                                                          FalsePositives(name='fp'),
                                                          TrueNegatives(name='tn'),
                                                          FalseNegatives(name='fn'), 
                                                          'accuracy',
                                                          Precision(name='precision'),
                                                          Recall(name='recall')])

m.summary()

ReduceLROnPlateau = tf.keras.callbacks.ReduceLROnPlateau(monitor='val_loss', factor=0.1, mode = 'min',
                                                  patience= 2)
history = m.fit(
    training_dataset,
    validation_data = validation_dataset,
    batch_size = 8,
    epochs = 2,
    callbacks = [ReduceLROnPlateau,
                 tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=7, mode = 'min',
                                                  restore_best_weights=True)]
)

plt.figure(figsize = (10, 5))
plt.plot(history.history['accuracy'], label="accuracy")
plt.plot(history.history['val_accuracy'], label="val_accuracy")
plt.legend()

plt.figure(figsize = (10, 5))
plt.plot(history.history['loss'], label = "loss")
plt.plot(history.history['val_loss'], label = "val_loss")
plt.legend()

m.evaluate(validation_dataset, batch_size = 8)