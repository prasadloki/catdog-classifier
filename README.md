
# 🐱🐶 Cats vs Dogs Classifier (Streamlit App)

A simple and interactive web application built using **Streamlit** that classifies uploaded images as either **Cat** or **Dog** using a machine learning model.

---

## 🚀 Features

- Upload any image of a cat or a dog  
- Get instant predictions with confidence percentage  
- Simple and clean UI using Streamlit  
- Powered by a pretrained machine learning model  

---

## 📂 Project Structure

```
cats_vs_dogs_streamlit.py    # Main Streamlit app
README.md                    # Project overview
requirements.txt             # Python dependencies
```

---

## 📦 Requirements

Install the required packages using:

```bash
pip install -r requirements.txt
```

Example `requirements.txt` content:

```
streamlit
tensorflow
numpy
Pillow
```

---

## ▶️ How to Run the App

1. Clone the repository:

```bash
git clone https://github.com/prasadloki/catdog-classifier.git
cd catdog-classifier
```

2. Run the Streamlit app:

```bash
streamlit run catdog-classifier.py
```

3. The app will open in your browser at `http://localhost:8501`

---

## 🧠 Model Info

- The app uses a pretrained model saved as `model.h5`
- Make sure `model.h5` is present in the same directory as the script
- Model is loaded using TensorFlow/Keras and performs binary classification (cat vs dog)

---

## 📸 Sample Prediction Output

After uploading an image, you'll get output like:

```
Prediction: Dog
Confidence: 93.1%
```

---

## 🙋‍♂️ Author

**Prasad Bodduboina**

- GitHub: [@prasadloki](https://github.com/prasadloki)
- LinkedIn: https://www.linkedin.com/in/prasad421/  
- Email: bodduboinaprasad@gmail.com

---

## 🛠 Tech Stack

- Python
- Streamlit
- TensorFlow / Keras
- NumPy
- PIL (Python Imaging Library)

---

