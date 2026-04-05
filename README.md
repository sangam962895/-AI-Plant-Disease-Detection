<div align="center">

<img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Flask-2.x-000000?style=for-the-badge&logo=flask&logoColor=white"/>
<img src="https://img.shields.io/badge/TensorFlow-2.x-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white"/>
<img src="https://img.shields.io/badge/Gemini_Pro-AI-4285F4?style=for-the-badge&logo=google&logoColor=white"/>
<img src="https://img.shields.io/badge/License-Educational-brightgreen?style=for-the-badge"/>

<br/><br/>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=28&pause=1000&color=2D9A4E&center=true&vCenter=true&width=600&lines=🌿+PlantCareAI;AI+Plant+Disease+Detection;Upload+→+Diagnose+→+Treat" alt="Typing SVG" />

### AI-Powered Plant Disease Detection & Intelligent Assistant

**Upload a leaf image → Get instant diagnosis → Chat with an AI expert**

<br/>

[🚀 Quick Start](#-quick-start) &nbsp;·&nbsp; [📸 Screenshots](#-screenshots) &nbsp;·&nbsp; [🎬 Demo](#-demo) &nbsp;·&nbsp; [🧠 How It Works](#-how-it-works) &nbsp;·&nbsp; [🛠️ Tech Stack](#️-tech-stack)

<br/>

</div>

---

## 📖 Overview

Crop diseases are responsible for **20–40% of global agricultural losses** every year. Early, accurate detection is critical — but expert advice is rarely accessible when and where farmers need it most.

**PlantCareAI** solves this with a two-layer AI system:

- 🔬 **A CNN deep learning model** trained on 40+ plant diseases, delivering results in under 1 second with 95%+ accuracy
- 🤖 **A Google Gemini Pro chatbot** that understands your exact diagnosis and answers follow-up questions like a personal agronomist — 24/7, no waiting

No expensive equipment. No expert appointments. Just upload a photo.

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 📤 **Easy Upload** | Drag & drop or click to upload — PNG, JPG, JPEG, GIF, WebP (max 10MB) |
| 🔬 **AI Analysis** | Advanced CNN model detects 40+ plant diseases with confidence scoring |
| 💊 **Treatment Guide** | Expert-approved, disease-specific chemical & organic treatment plans |
| 🤖 **Smart Chatbot** | Gemini Pro remembers your diagnosis for personalized follow-up Q&A |
| 📊 **History Tracking** | Track plant health over time with detailed diagnosis history |
| 📱 **Mobile Ready** | Fully responsive — works on desktop, tablet, and mobile for field use |
| ⚡ **95%+ Accuracy** | Trained on millions of leaf images, results in under 1 second |
| 🌐 **24/7 Available** | Access anytime, anywhere online |

---

## 🎬 Demo

> 🎥 **Watch the full project demo on YouTube:**

<div align="center">

[![PlantCareAI Demo](https://img.youtube.com/vi/sQQ6Sm6ZxMI/maxresdefault.jpg)](https://youtu.be/sQQ6Sm6ZxMI?si=6lcI1Hj1F83yg00K)

**▶️ [Click to Watch Demo on YouTube](https://youtu.be/sQQ6Sm6ZxMI?si=6lcI1Hj1F83yg00K)**

</div>

---

## 📸 Screenshots

### 🏠 Home — Upload Interface
> Hero section with "Detect Plant Diseases Instantly" banner, file upload form supporting PNG/JPG/JPEG/GIF/WebP up to 10MB, and the Analyze Plant button.

<img src="https://github.com/user-attachments/assets/d955bebc-1dfc-4de5-9b21-6f448e678881" alt="Home Page" width="100%"/>

---

### 🔬 Analysis Results — Disease Detected
> Instant diagnosis card showing the uploaded leaf image, detected disease name, confidence level bar (99%), and treatment recommendations.

<img src="https://github.com/user-attachments/assets/ac209415-891e-4cf5-942a-7420ccd1d4fe" alt="Analysis Results" width="100%"/>

---

### 🤖 Results + AI Chatbot Panel Open
> The result page with the AI Plant Assistant chatbot panel open — quick action buttons (Check plant disease, Show treatment, Plant care tips, Use last result) and the Gemini-powered chat interface pre-loaded with the current diagnosis.

<img src="https://github.com/user-attachments/assets/c96d230d-5c9f-480f-b427-02e9acc49ad9" alt="Result with Chatbot" width="100%"/>

---

### 💬 AI Chatbot — Context-Aware Conversation
> Zoomed-in chatbot panel showing a real conversation. The bot knows the current disease (Strawberry – Leaf Scorch) and provides tailored treatment advice in response to user queries.

<img src="https://github.com/user-attachments/assets/2fba0538-4ba4-4c70-aa11-ac92e5962ce7" alt="Chatbot Conversation" width="40%"/>

---

### ℹ️ About Page — Hero Banner
> "About AI Plant Doctor — Smart farming powered by artificial intelligence to protect your crops."

<img src="https://github.com/user-attachments/assets/cb19a1ac-8f7e-45cd-a91c-ee19ee43337c" alt="About Page" width="100%"/>

---

### 📋 Project Overview Section
> Key highlights: Instant Detection, 95%+ Accuracy, Expert Guidance, 24/7 Available — alongside the Agricultural Innovation card.

<img src="https://github.com/user-attachments/assets/c39c1901-57d0-4eeb-ae19-38d3b0e5401d" alt="Project Overview" width="100%"/>

---

### 🧠 How The AI Model Works
> Step-by-step pipeline: Image Upload → Image Processing → AI Prediction → Results & Treatment, with CNN explainer.

<img src="https://github.com/user-attachments/assets/c915febd-42c4-41a4-9cec-fae38134b075" alt="How It Works" width="100%"/>

---

### ⚡ Our Features Grid
> Six feature cards: Easy Upload, AI Analysis, Treatment Guide, Smart Chatbot, History Tracking, Mobile Ready.

<img src="https://github.com/user-attachments/assets/df7abca0-37c9-4ceb-a74f-a031a2ca977a" alt="Features" width="100%"/>

---

### 🛠️ Technology Stack
> Python, Flask, TensorFlow, CNN Model, Bootstrap, NumPy, PIL, Cloud Ready — with live stats: 95%+ accuracy, 40+ diseases, <1s analysis, 24/7 available.

<img src="https://github.com/user-attachments/assets/6d8aa5fd-fc18-4e4b-93b0-e5d8a445dde0" alt="Tech Stack" width="100%"/>

---

## 🧠 How It Works

```
  User uploads leaf image
          │
          ▼
  ┌─────────────────────┐
  │    Flask Backend     │  ←  Werkzeug secures & validates the file
  │      (app.py)        │
  └──────────┬──────────┘
             │
             ▼
  ┌─────────────────────┐
  │    Preprocessing     │  ←  Resize to 224×224px, normalize array
  │  (Pillow + NumPy)    │
  └──────────┬──────────┘
             │
             ▼
  ┌─────────────────────┐
  │    CNN Inference     │  ←  TensorFlow/Keras model predicts
  │  (plant_model.h5)   │      disease class + confidence score
  └──────────┬──────────┘
             │
             ▼
  ┌─────────────────────┐
  │   Treatment Engine   │  ←  Algorithmic treatment plan
  │                      │      tailored to predicted disease
  └──────────┬──────────┘
             │
             ▼
  ┌─────────────────────┐
  │   Session Context    │  ←  Diagnosis saved for chatbot awareness
  └──────────┬──────────┘
             │
             ▼
  ┌─────────────────────┐
  │  Gemini Pro Chatbot  │  ←  Context-aware AI Q&A for follow-ups
  └─────────────────────┘
```

The model was trained on **40+ disease classes** across multiple crops and achieves **95%+ accuracy** on the validation set. Low-confidence predictions are filtered out automatically — you only see results the model is certain about.

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| **Backend** | Python 3.8+, Flask | Web server and API routing |
| **Deep Learning** | TensorFlow 2.x, Keras | CNN model inference (`plant_model.h5`) |
| **AI Chatbot** | Google Gemini Pro | Context-aware agricultural Q&A |
| **Frontend** | HTML5, CSS3, Bootstrap, Vanilla JS | Responsive user interface |
| **Image Processing** | Pillow (PIL), NumPy | Preprocessing and normalization |
| **Security / Utils** | Werkzeug, Python Logging | File handling, activity logs |
| **Deployment** | Cloud Ready | Deploy anywhere — Heroku, Render, VPS |

---

## 📂 Project Structure

```
PlantCareAI/
│
├── app.py                  # Main Flask app — routes, model loading, session handling
├── plant_model.h5          # Pre-trained CNN model (TensorFlow/Keras)
├── labels.json             # Class label mapping (disease names → index)
├── requirements.txt        # Python dependencies
├── plant_care_app.log      # Runtime activity log (auto-generated)
│
├── uploads/                # Temporary storage for uploaded images (auto-cleaned)
│
├── templates/
│   ├── index.html          # Upload interface (home page)
│   ├── result.html         # Diagnosis results page
│   ├── about.html          # About the project
│   ├── contact.html        # Contact info
│   └── _chatbot.html       # Reusable AI chatbot UI component
│
└── static/
    ├── style.css           # Global styles and animations
    └── chat.js             # Gemini chatbot JavaScript logic
```

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip
- A Google Gemini API key — [get one free here](https://aistudio.google.com/)

### Step 1 — Clone the repository

```bash
git clone https://github.com/sangam962895/-AI-Plant-Disease-Detection.git
cd AI-Plant-Disease-Detection
```

### Step 2 — Create a virtual environment (recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / Mac
python3 -m venv venv
source venv/bin/activate
```

### Step 3 — Install dependencies

```bash
pip install flask tensorflow numpy pillow google-generativeai werkzeug
```

Or use the requirements file:

```bash
pip install -r requirements.txt
```

### Step 4 — Set your Gemini API key

```bash
# Linux / Mac
export GEMINI_API_KEY="your_gemini_api_key_here"

# Windows (Command Prompt)
set GEMINI_API_KEY=your_gemini_api_key_here

# Windows (PowerShell)
$env:GEMINI_API_KEY="your_gemini_api_key_here"
```

### Step 5 — Run the application

```bash
python app.py
```

### Step 6 — Open in browser

```
http://127.0.0.1:5000
```

> 🎯 That's it! Upload a leaf image and get your first diagnosis in seconds.

---

## 🌿 Supported Diseases

The CNN model detects **40+ disease classes** across major crops:

| Crop | Diseases Detected |
|---|---|
| 🍅 **Tomato** | Early blight, late blight, leaf mold, mosaic virus, septoria leaf spot, bacterial spot, target spot, yellow leaf curl virus |
| 🥔 **Potato** | Early blight, late blight |
| 🌽 **Corn (Maize)** | Gray leaf spot, common rust, northern leaf blight |
| 🍎 **Apple** | Apple scab, black rot, cedar apple rust |
| 🍇 **Grape** | Black rot, esca (black measles), leaf blight |
| 🍑 **Peach** | Bacterial spot |
| 🍒 **Cherry** | Powdery mildew |
| 🍓 **Strawberry** | Leaf scorch |
| 🌶️ **Pepper** | Bacterial spot |
| ✅ **Healthy** | Correctly identifies healthy leaves for all supported species |

---

## 💡 Usage Tips

- **Image quality matters** — Use clear, well-lit photos. The leaf should fill most of the frame.
- **Single leaf preferred** — Isolate one symptomatic leaf for best accuracy.
- **Low confidence = no result** — If no result appears, try a sharper or closer image.
- **Use the chatbot** — After diagnosis, the AI Plant Assistant is pre-loaded with your result. Ask specific questions like dosage, timing, or organic alternatives.
- **Supported formats** — PNG, JPG, JPEG, GIF, WebP up to 10MB.

---

## 🤝 Contributing

Contributions are welcome! Here's how:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m 'Add: your feature description'`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Open a Pull Request

---

## 📜 License

This project is created for **educational, agricultural, and academic purposes**.
Feel free to use, modify, and build upon it with attribution.

---

## 👨‍💻 Author

**Sangam Kumar**
🔗 [GitHub Profile](https://github.com/sangam962895)
▶️ [YouTube Demo](https://youtu.be/sQQ6Sm6ZxMI?si=6lcI1Hj1F83yg00K)

---

<div align="center">

### ⭐ If PlantCareAI helped you, please give it a star — it helps others discover the project!

**Made with 🌿 for farmers, gardeners, and the planet.**

</div>
