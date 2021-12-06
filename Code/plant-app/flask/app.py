from flask import Flask, render_template, request

from tensorflow import keras
from tensorflow.keras.preprocessing.image import array_to_img, img_to_array, load_img
import numpy as np
import os, json

app = Flask(__name__)
#longer run time with pre-trained models
# model = keras.models.load_model("optimal_weights_DenseNet201.h5")

#shorter runtime with initial model
model = keras.models.load_model("optimal_weights.h5")

@app.route('/upload', methods = ["POST"])
def upload():
    file = request.files['imagefile']
    path = os.path.join("./images", file.filename)
    file.save(path)
    labels = ['healthy', 'multiple_diseases', 'rust', 'scab']
    img = load_img(path, target_size = (224,224))
    img_arr = img_to_array(img)
    img_arr = np.expand_dims(img_arr, axis=0)
    img_arr /= 255
    y_pred = model.predict(img_arr)
    index = np.argmax(y_pred)
    acc = np.ndarray.flatten(y_pred)[index]
    feature = labels[index]

    text = "The model predicts that the image is/has " + str(round(acc*100, 2)) + "% " + feature
    removefiles("./images")
    return text

def removefiles(_dir):
    for file in os.listdir(_dir):
        os.remove(os.path.join(_dir, file))

if __name__ == "__main__":
    app.run(port = 3000, debug = True)
