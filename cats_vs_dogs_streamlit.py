
import streamlit as st
import tensorflow as tf
import os
import zipfile
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from PIL import Image

st.set_page_config(page_title="Cats vs Dogs Classifier", layout="centered")

st.title("🐱🐶 Cats vs Dogs Classifier")

@st.cache_data
def download_and_prepare_data():
    dataset_url = "https://storage.googleapis.com/mledu-datasets/cats_and_dogs_filtered.zip"
    zip_path = tf.keras.utils.get_file('cats_and_dogs_filtered.zip', origin=dataset_url, extract=False)
    extract_path = os.path.join(os.path.dirname(zip_path), 'cats_and_dogs_filtered')

    if not os.path.exists(extract_path):
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(os.path.dirname(zip_path))

    return os.path.join(extract_path, 'train'), os.path.join(extract_path, 'validation')

@st.cache_resource
def train_model(train_dir, validation_dir):
    BATCH_SIZE = 32
    IMG_SIZE = (160, 160)

    train_datagen = ImageDataGenerator(rescale=1./255)
    val_datagen = ImageDataGenerator(rescale=1./255)

    train_gen = train_datagen.flow_from_directory(train_dir, target_size=IMG_SIZE, batch_size=BATCH_SIZE, class_mode='binary')
    val_gen = val_datagen.flow_from_directory(validation_dir, target_size=IMG_SIZE, batch_size=BATCH_SIZE, class_mode='binary')

    model = tf.keras.Sequential([
        tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(160,160,3)),
        tf.keras.layers.MaxPooling2D(2,2),
        tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
        tf.keras.layers.MaxPooling2D(2,2),
        tf.keras.layers.Conv2D(128, (3,3), activation='relu'),
        tf.keras.layers.MaxPooling2D(2,2),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(512, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])

    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    model.fit(train_gen, epochs=20, validation_data=val_gen)
    return model

st.info("Click the button to prepare data and train model. May take a few minutes.")
if st.button("Prepare & Train"):
    train_path, val_path = download_and_prepare_data()
    model = train_model(train_path, val_path)
    st.success("✅ Model trained successfully!")

    st.session_state['model'] = model

if 'model' in st.session_state:
    st.header("📤 Upload an Image to Classify")
    uploaded_file = st.file_uploader("Upload an image of a cat or dog", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        image = Image.open(uploaded_file).convert('RGB')
        st.image(image, caption="Uploaded Image", use_column_width=True)

        img = image.resize((160, 160))
        img_array = img_to_array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        prediction = st.session_state['model'].predict(img_array)[0][0]

        label = "Dog 🐶" if prediction > 0.5 else "Cat 🐱"
        confidence = prediction if prediction > 0.5 else 1 - prediction

        st.subheader(f"Prediction: {label}")
        st.write(f"Confidence: {confidence:.2%}")
else:
    st.warning("⚠️ Model not trained yet. Click the button above to train.")
