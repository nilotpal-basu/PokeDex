import os
import sys
import numpy as np
import pandas as pd
from tensorflow.keras.preprocessing.image import load_img,img_to_array
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
import warnings

warnings.filterwarnings("ignore")

def data_ldr(data_dir):
    label = [] 
    path = [] 
    for dir_name , _,filenames in os.walk(data_dir):
        for filename in filenames:
            if os.path.splitext(filename)[-1]=='.png':
                if dir_name.split()[-1]!='GT':
                    label.append(os.path.split(dir_name)[-1])
                    path.append(os.path.join(dir_name,filename))
    df = pd.DataFrame(columns=["path","label"])
    df["path"] = path
    df["label"] = label
    labels = df['label'].astype('category').cat.codes
    df['label_encoded'] = labels
    return df

def class_name_gen(df):
    class_name = np.array(df['label'].unique())
    return class_name

def data_splitter(df):
    img_size = (128, 128)  

    images = []
    for img_path in df['path']:
        img = load_img(img_path, target_size=img_size) 
        img_array = img_to_array(img) / 255
        images.append(img_array)

    X = np.array(images)
    y = to_categorical(df['label_encoded'])


    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42,shuffle=True)
    y_train = np.argmax(y_train, axis=1)
    y_test = np.argmax(y_test, axis=1)
    return X_train , X_test , y_train , y_test 


# if __name__=='__main__' :
    # script_directory = os.path.dirname(os.path.abspath(sys.argv[0])) 
    # script_directory = os.path.join(script_directory,'pokemon-dataset-1000')
    # script_directory = os.path.join(script_directory,'dataset')
    # df = data_ldr(script_directory)

    # X_train , X_test , y_train , y_test = data_splitter(df)
    # print(class_name_gen(df))