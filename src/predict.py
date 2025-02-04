from tensorflow.keras.preprocessing.image import load_img,img_to_array
import tensorflow as tf
import numpy as np
import os , sys 
from data_loader import data_ldr , class_name_gen
from model_gen import model
import keras

def pred_poke(img_path,img_size=(128,128)):
    pw_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    pw_dir = os.path.abspath(os.path.join(pw_dir, os.pardir))
    ds_directory = os.path.join(pw_dir,'pokemon-dataset-1000')
    ds_directory = os.path.join(ds_directory,'dataset')

    df = data_ldr(ds_directory)
    class_name = class_name_gen(df)
    
    model_dir = os.path.join(pw_dir,'your model name')
    my_model = keras.models.load_model(model_dir)

    img = load_img(img_path, target_size=img_size) 
    img_array = img_to_array(img) / 255
    img_array = np.array([img_array])

    pred_class_num = np.argmax(my_model.predict(img_array,verbose=0))
    return class_name[pred_class_num]
