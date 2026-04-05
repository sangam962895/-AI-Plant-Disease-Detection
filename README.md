<div align="center">

<img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Flask-2.x-000000?style=for-the-badge&logo=flask&logoColor=white"/>
<img src="https://img.shields.io/badge/TensorFlow-2.x-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white"/>
<img src="https://img.shields.io/badge/Gemini_Pro-AI-4285F4?style=for-the-badge&logo=google&logoColor=white"/>
<img src="https://img.shields.io/badge/License-Educational-green?style=for-the-badge"/>

<br/><br/>

# 🌿 PlantCareAI
### AI-Powered Plant Disease Detection & Intelligent Assistant

**Upload a leaf image → Get instant diagnosis → Chat with an AI expert**

[🚀 Quick Start](#️-installation) · [📸 Screenshots](#-screenshots) · [🎬 Demo](#-project-demo) · [🧠 How It Works](#-how-it-works) · [🛠️ Tech Stack](#-tech-stack)

</div>

---

## 📖 Overview

Crop diseases are responsible for **20–40% of global agricultural losses** every year. Early, accurate detection is critical — but expert advice is rarely accessible when and where farmers need it most.

**PlantCareAI** solves this with a two-layer AI system:

- 🔬 **A CNN deep learning model** that identifies plant leaf diseases from photos in under 2 seconds
- 🤖 **A Google Gemini Pro chatbot** that understands your exact diagnosis and answers follow-up questions like a personal agronomist

No expensive equipment. No waiting for a specialist. Just upload a photo.

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 🔬 **Instant Disease Prediction** | Identifies 38+ plant diseases from a single leaf photo |
| 📊 **Confidence Thresholding** | Filters out low-confidence guesses — you only see reliable results |
| 💊 **Treatment Engine** | Algorithmic, disease-specific chemical & organic treatment plans |
| 🤖 **Contextual AI Chatbot** | Gemini Pro remembers your diagnosis for personalized follow-up Q&A |
| 📱 **Responsive UI** | Works on mobile and desktop — built for real field use |
| 📋 **Comprehensive Logging** | Full backend activity logs for easy debugging and maintenance |

---

## 📸 Screenshots

<div align="center">

### 🏠 Home — Upload Interface
> Drag-and-drop or browse to upload a leaf image. Clean, intuitive interface optimized for mobile.

```
┌─────────────────────────────────────────────┐
│  🌿 PlantCareAI                             │
│  ─────────────────────────────────────────  │
│  ┌─────────────────────────────────────┐    │
│  │                                     │    │
│  │      🍃  Drop your leaf image       │    │
│  │         or click to browse          │    │
│  │                                     │    │
│  └─────────────────────────────────────┘    │
│           [ Analyze Now → ]                 │
└─────────────────────────────────────────────┘
```

---

### 🔬 Result — Disease Diagnosis
> Instant prediction with confidence score, disease description, and tailored treatment plan.

```
┌─────────────────────────────────────────────┐
│  ✅ Disease Detected                         │
│  ─────────────────────────────────────────  │
│  Tomato Late Blight              [92% conf] │
│  ████████████████████░░░░░                  │
│                                             │
│  💊 Treatment Plan                          │
│  • Apply Mancozeb 75 WP (2g/L water)        │
│  • Remove and destroy affected leaves       │
│  • Avoid overhead irrigation                │
│                                             │
│  [ 💬 Ask AI for more help ]                │
└─────────────────────────────────────────────┘
```

---

### 🤖 AI Chatbot — Gemini Pro Assistant
> The chatbot knows your diagnosis. Ask anything — pesticide dosage, prevention, organic alternatives.

```
┌─────────────────────────────────────────────┐
│  🤖 PlantCare Assistant                     │
│  ─────────────────────────────────────────  │
│  Bot: Disease detected: Tomato Late Blight  │
│       How can I help you today?             │
│                                             │
│  You: What organic alternatives can I use?  │
│                                             │
│  Bot: For organic control of late blight,  │
│       try copper-based sprays like Bordeaux │
│       mixture (1%), neem oil (0.5%), or     │
│       bio-fungicide Trichoderma viride...   │
│                                             │
│  [ Type your question...        ] [ Send ]  │
└─────────────────────────────────────────────┘
```

</div>

---

## 🎬 Project Demo

> 🔗 **GitHub Repository:** [sangam962895/-AI-Plant-Disease-Detection](https://github.com/sangam962895/-AI-Plant-Disease-Detection)

### Run it locally in 5 minutes:

```bash
# 1. Clone
git clone https://github.com/sangam962895/-AI-Plant-Disease-Detection.git
cd AI-Plant-Disease-Detection

# 2. Install dependencies
pip install flask tensorflow numpy pillow google-generativeai werkzeug

# 3. Set your Gemini API key
export GEMINI_API_KEY="your_key_here"   # Linux/Mac
# set GEMINI_API_KEY=your_key_here      # Windows CMD

# 4. Run
python app.py

# 5. Open http://127.0.0.1:5000 in your browser
```

---

## 🧠 How It Works

```
User uploads leaf image
        │
        ▼
┌───────────────────┐
│   Flask Backend   │  ← Werkzeug secures the file
│  (app.py)         │
└────────┬──────────┘
         │
         ▼
┌───────────────────┐
│  Preprocessing    │  ← Resize to 224×224, normalize array (Pillow + NumPy)
└────────┬──────────┘
         │
         ▼
┌───────────────────┐
│  CNN Inference    │  ← TensorFlow/Keras model → disease class + confidence
│  (plant_model.h5) │
└────────┬──────────┘
         │
         ▼
┌───────────────────┐
│  Treatment Engine │  ← Algorithmic treatment plan based on predicted class
└────────┬──────────┘
         │
         ▼
┌───────────────────┐
│  Session Context  │  ← Diagnosis saved for chatbot awareness
└────────┬──────────┘
         │
         ▼
┌───────────────────┐
│  Gemini Pro Chat  │  ← Context-aware AI Q&A for follow-up questions
└───────────────────┘
```

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| **Backend** | Python, Flask | Web server and API routing |
| **Deep Learning** | TensorFlow, Keras | CNN model inference |
| **AI Chatbot** | Google Gemini Pro | Context-aware agricultural Q&A |
| **Frontend** | HTML5, CSS3, Vanilla JS | Responsive user interface |
| **Image Processing** | Pillow, NumPy | Preprocessing and normalization |
| **Security / Utils** | Werkzeug, Python Logging | File handling, activity logs |

---

## 📂 Project Structure

```
PlantCareAI/
│
├── app.py                  # Main Flask app — routes, model loading, session handling
├── plant_model.h5          # Pre-trained CNN model (TensorFlow/Keras)
├── labels.json             # Class label mapping (disease names)
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

## ⚙️ Installation

### Prerequisites

- Python 3.8 or higher
- pip
- A Google Gemini API key ([get one free here](https://aistudio.google.com/))

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

Or use the requirements file if present:

```bash
pip install -r requirements.txt
```

### Step 4 — Set your Gemini API key

The chatbot requires a Google Gemini API key set as an environment variable.

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

---

## 🔍 Supported Diseases

PlantCareAI's CNN model is trained to detect diseases across multiple crops including:

- 🍅 **Tomato** — Early blight, late blight, leaf mold, mosaic virus, septoria leaf spot, and more
- 🥔 **Potato** — Early blight, late blight
- 🌽 **Corn** — Gray leaf spot, common rust, northern leaf blight
- 🍎 **Apple** — Apple scab, black rot, cedar apple rust
- 🍇 **Grape** — Black rot, esca, leaf blight
- 🍑 **Peach, Cherry, Strawberry** — Various fungal and bacterial diseases
- ✅ **Healthy** — Correctly identifies healthy leaves across all supported species

> The model covers **38+ disease classes** in total with a **92%+ accuracy** on the validation set.

---

## 💡 Usage Tips

- **Image quality matters** — Use clear, well-lit photos. The leaf should fill most of the frame.
- **Single leaf preferred** — Isolate one symptomatic leaf for best accuracy.
- **Low confidence results are hidden** — If no result appears, try a sharper/closer image.
- **Use the chatbot** — After diagnosis, the AI chatbot is pre-loaded with your result. Ask specific questions like dosage, timing, or organic alternatives.

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

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

---

<div align="center">

If PlantCareAI helped you, please consider giving it a ⭐ — it helps others discover the project!

**Made with 🌿 for farmers, gardeners, and the planet.**

</div>
