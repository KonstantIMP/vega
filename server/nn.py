import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np

def get_name(face_img_file, keras_file, labels_file, min_prob = 0.95) :
    np.set_printoptions(suppress=True)
    model = tensorflow.keras.models.load_model(keras_file)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    image = Image.open(face_img_file)

    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    image_array = np.asarray(image)

    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

    data[0] = normalized_image_array
    prediction = model.predict(data)
    
    if max(prediction[0]) < min_prob :
        return False

    print('Pobably is :', max(prediction[0]))
    print('User index :', np.argmax(prediction[0]))

    with open(labels_file, 'r') as f :
        for i in range(np.argmax(prediction[0])) :
            f.readline()

        return f.readline()[len(str(np.argmax(prediction[0]))) + 1 :-1:]
    
