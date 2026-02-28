# 🌿 AI Plant Disease Detection Web App

An Artificial Intelligence based web application that detects plant leaf diseases using Deep Learning and provides treatment suggestions.

The system allows a user (farmer / gardener / student) to upload a leaf image and instantly get:

* Disease Name
* Confidence Score
* Recommended Treatment

---

## 📖 Project Description

Plant diseases reduce agricultural productivity and crop quality. Farmers often cannot identify diseases at an early stage due to lack of expert knowledge.

This project solves the problem by using a **Deep Learning CNN model (MobileNetV2)** to automatically detect plant diseases from leaf images.

The model is integrated into a **Flask web application**, allowing real-time prediction through a simple user interface.

---

## ✨ Features

* Upload plant leaf image
* AI based disease prediction
* Confidence percentage display
* Uploaded image preview
* Dynamic treatment suggestion
* Modern responsive website UI

---

## 🧠 Technologies Used

| Category         | Technology                          |
| ---------------- | ----------------------------------- |
| Programming      | Python                              |
| Deep Learning    | TensorFlow, Keras                   |
| Model            | MobileNetV2 (Transfer Learning CNN) |
| Backend          | Flask                               |
| Frontend         | HTML, Tailwind CSS                  |
| Image Processing | Pillow, NumPy                       |
| Dataset          | PlantVillage Dataset (Kaggle)       |

---

## 🧪 Model Details

* Model Type: Convolutional Neural Network (CNN)
* Pretrained Architecture: **MobileNetV2**
* Input Image Size: **224 × 224 pixels**
* Training Platform: Kaggle GPU
* Dataset: PlantVillage (Augmented)

The model learns patterns like:

* leaf spots
* color changes
* fungal infection
* bacterial infection

---

## 📂 Project Structure

```
PlantCareAI/
│
├── app.py
├── plant_model.h5
├── labels.json
├── uploads/
│
├── templates/
│   ├── index.html
│   ├── result.html
│   ├── about.html
│   └── contact.html
│
└── static/
```

---

## ⚙️ Installation (Step by Step)

### 1. Clone the repository

```bash
git clone https://github.com/your-username/plant-disease-detection.git
cd plant-disease-detection
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / Mac**

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If requirements.txt is not available:

```bash
pip install flask tensorflow numpy pillow
```

---

### 4. Run the Application

```bash
python app.py
```

---

### 5. Open in Browser

```
http://127.0.0.1:5000
```

Upload a leaf image and get prediction.

---

## 🔍 How It Works

1. User uploads leaf image
2. Flask server receives image
3. Image resized to 224×224
4. Image normalized
5. CNN model predicts disease
6. Highest confidence class selected
7. Website shows result + treatment

---

## 📊 Output

The system displays:

* Uploaded Leaf Image
* Disease Name
* Confidence Percentage
* Treatment Recommendation

---

## 🚀 Future Scope

* Mobile application
* Camera live detection
* More crop datasets
* Cloud deployment
* Multilingual support

---

## 👨‍💻 Author

**Sangam Kumar**

---

## 📜 License

This project is created for educational and academic purposes.

---

⭐ If you found this useful, please give this repository a star!
