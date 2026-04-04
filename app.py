import os
import json
import logging
import uuid
import google.generativeai as genai
from flask import Flask, render_template, request, send_from_directory, flash, redirect, url_for, session, jsonify
from werkzeug.utils import secure_filename
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import traceback

# ================= LOGGING SETUP =================
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('plant_care_app.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.secret_key = 'your_secret_key_here_change_in_production'

# Configure Gemini API key
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

# ================= CONFIGURATION =================
UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
IMG_SIZE = (224, 224)
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB
CONFIDENCE_THRESHOLD = 30  # Minimum confidence percentage

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ================= GLOBAL VARIABLES =================
model = None
labels = None
model_loaded = False

# ================= UTILITY FUNCTIONS =================
def format_disease_name(disease):
    """
    Convert raw disease label to user-friendly format.
    Examples:
        "Pepper,_bell___Bacterial_spot" → "Pepper Bell - Bacterial Spot"
        "Tomato___Late_blight" → "Tomato - Late Blight"
        "Apple___healthy" → "Apple - Healthy"
    """
    if not disease:
        return "Unknown"
    
    try:
        # Split crop and disease by triple underscore
        if "___" in disease:
            crop, disease_part = disease.split("___", 1)
        else:
            crop = disease
            disease_part = "Unknown"
        
        # Clean and format crop name (replace underscores and commas with spaces)
        crop = crop.replace("_", " ").replace(",", "")
        
        # Clean and format disease part (replace underscores with spaces)
        disease_part = disease_part.replace("_", " ")
        
        # Capitalize each word appropriately
        crop = " ".join(word.capitalize() for word in crop.split())
        disease_part = " ".join(word.capitalize() for word in disease_part.split())
        
        # Combine with dash separator
        return f"{crop} - {disease_part}"
    
    except Exception as e:
        logger.warning(f"Error formatting disease name '{disease}': {str(e)}")
        return disease

def get_confidence_level(confidence):
    """
    Categorize confidence percentage into level and color.
    Returns: (level_text, color_class, message)
    """
    if confidence > 80:
        return "High", "success", "Reliable diagnosis"
    elif confidence >= 50:
        return "Medium", "warning", "Consider verification"
    else:
        return "Low", "danger", "Consult expert"

def allowed_file(filename):
    """Validate if file extension is allowed."""
    if not filename or '.' not in filename:
        return False
    ext = filename.rsplit('.', 1)[1].lower()
    return ext in ALLOWED_EXTENSIONS

def load_resources():
    """Load model and labels with error handling."""
    global model, labels, model_loaded
    
    try:
        if not os.path.exists("plant_model.h5"):
            logger.error("Model file 'plant_model.h5' not found.")
            return False
        
        model = load_model("plant_model.h5")
        logger.info("Model loaded successfully")
        
        if not os.path.exists("labels.json"):
            logger.error("Labels file 'labels.json' not found.")
            return False
        
        with open("labels.json", "r") as f:
            labels = json.load(f)
        
        if not isinstance(labels, dict):
            logger.error("Labels file format is invalid")
            return False
        
        logger.info(f"Labels loaded successfully. Found {len(labels)} classes")
        model_loaded = True
        return True
        
    except Exception as e:
        logger.error(f"Error loading resources: {str(e)}")
        logger.error(traceback.format_exc())
        return False

def cleanup_file(filepath):
    """Safely delete uploaded file."""
    try:
        if os.path.exists(filepath):
            os.remove(filepath)
            logger.info(f"Cleaned up file: {filepath}")
    except Exception as e:
        logger.warning(f"Could not delete file {filepath}: {str(e)}")

# ================= PREDICTION =================
def predict_disease(img_path):
    """
    Predict plant disease from image.
    Returns: (disease_name, confidence) or (None, None) on error
    """
    try:
        if not os.path.exists(img_path):
            logger.error(f"Image file not found: {img_path}")
            return None, None
        
        file_size = os.path.getsize(img_path)
        if file_size > MAX_FILE_SIZE or file_size == 0:
            logger.error(f"Invalid file size: {file_size}")
            return None, None
        
        if model is None or not model_loaded:
            logger.error("Model not loaded")
            return None, None
        
        img = image.load_img(img_path, target_size=IMG_SIZE)
        img_array = image.img_to_array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)
        
        prediction = model.predict(img_array, verbose=0)[0]
        class_index = np.argmax(prediction)
        confidence = float(np.max(prediction)) * 100
        
        if not (0 <= confidence <= 100):
            logger.error(f"Invalid confidence: {confidence}")
            return None, None
        
        disease_name = labels.get(str(class_index), "Unknown")
        
        logger.info(f"Prediction: {disease_name} ({confidence:.2f}%)")
        return disease_name, int(confidence)
        
    except Exception as e:
        logger.error(f"Prediction error: {str(e)}")
        logger.error(traceback.format_exc())
        return None, None

# ================= TREATMENT DATABASE =================
def get_treatment(disease):
    """Get treatment recommendations with intelligent keyword matching."""
    # Hardcoded treatments for specific diseases
    specific_treatments = {
        "Tomato___Late_blight": "Apply copper-based fungicide. Remove infected leaves. Avoid overhead watering.",
        "Tomato___Early_blight": "Use Mancozeb fungicide. Remove affected leaves. Ensure air circulation.",
        "Tomato___healthy": "Your tomato plant is healthy! Maintain regular watering and sunlight.",
    }
    
    # Check for specific match first
    if disease in specific_treatments:
        return specific_treatments[disease]
    
    # Dynamic keyword-based treatment
    disease_lower = str(disease).lower()
    
    if "healthy" in disease_lower:
        return "Your plant is healthy! Continue regular watering, adequate sunlight, and monitor for pest activity."
    
    if "blight" in disease_lower:
        return "Apply copper or fungicide treatment. Remove infected leaves immediately. Improve air circulation. Avoid overhead watering."
    
    if "yellow" in disease_lower or "chlorosis" in disease_lower:
        return "Yellow leaves indicate nutrient deficiency or overwatering. Check soil moisture, ensure proper drainage, and apply balanced fertilizer if needed."
    
    if "spot" in disease_lower or "leaf_spot" in disease_lower:
        return "Fungal leaf spots detected. Remove affected leaves, apply fungicide, and improve air circulation by pruning dense areas."
    
    if "wilt" in disease_lower:
        return "Wilting indicates root or water issues. Check soil drainage, adjust watering schedule, and ensure roots are healthy."
    
    if "rust" in disease_lower:
        return "Apply sulfur or copper-based fungicide. Remove diseased leaves. Increase air circulation and reduce leaf wetness."
    
    if "mold" in disease_lower or "powdery" in disease_lower:
        return "Spray with fungicide or neem oil. Increase air circulation. Remove severely affected leaves. Avoid overhead watering."
    
    if "pest" in disease_lower or "mite" in disease_lower or "insect" in disease_lower:
        return "Apply insecticidal soap or neem oil. Isolate affected plant. Spray underside of leaves thoroughly. Repeat treatment if needed."
    
    # Fallback for unknown diseases
    return "Consult an agriculture expert for specific treatment. Isolate the plant to prevent spread. Document symptoms for diagnosis."

def rule_based_chatbot(message):
    """Fallback rule-based chatbot if AI API fails or not configured."""
    user_message = str(message).strip().lower()
    
    last_pred = session.get('last_prediction')
    
    if not last_pred:
        # No prediction - ask to upload image
        if any(term in user_message for term in ['treatment', 'help', 'cure', 'fix', 'solution', 'recommend', 'what should i do']):
            return 'Please upload an image first so I can diagnose your plant and provide specific treatment.'
        return 'Please upload a plant image for diagnosis first.'

    # We have a prediction - be STRICTLY context-based
    disease = last_pred.get('disease', '')
    treatment = last_pred.get('treatment', '')
    
    # Check if question is related to the detected disease
    disease_keywords = str(disease).lower().split()
    treatment_keywords = ['treatment', 'cure', 'fix', 'help', 'solution', 'recommend', 'what should', 'how to']
    
    is_related = (
        any(keyword in user_message for keyword in disease_keywords) or
        any(keyword in user_message for keyword in treatment_keywords) or
        any(term in user_message for term in ['disease', 'plant', 'symptom', 'problem', 'issue'])
    )
    
    if not is_related:
        return f"Please ask questions related to the detected disease: {disease}"

    # Provide context-specific responses
    if any(word in user_message for word in ['treatment', 'cure', 'fix', 'help', 'solution', 'recommend']):
        return f"For {disease}: {treatment}"
    
    if any(word in user_message for word in ['symptom', 'sign', 'what is']):
        return f"The detected disease is {disease}. Symptoms include the issues shown in your uploaded image."
    
    if any(word in user_message for word in ['prevent', 'avoid', 'stop']):
        return f"To prevent {disease}: Maintain proper air circulation, avoid overhead watering, and regularly inspect plants for early signs."
    
    # Default context response
    return f"For {disease}: {treatment}"


def generate_ai_response(message, context=None):
    """Use Gemini SDK to generate plant-focused chatbot response with strict domain enforcement."""
    user_message = str(message or '').strip()

    # Check if we have a last prediction
    last_pred = context.get('last_prediction') if context else None
    
    if not last_pred:
        system_instruction = (
            "You are an AI Plant Assistant. This is a new session. "
            "You have no previous context. If the user has not provided an image or symptoms, "
            "reply exactly with:\n\n"
            "Welcome! 🌱\nUpload a plant image or describe the problem to get started."
        )
    else:
        # We have a prediction - let the AI dynamically respond based on it
        disease = last_pred.get('disease', '')
        treatment = last_pred.get('treatment', '')
        confidence = last_pred.get('confidence', 0)
        
        system_instruction = (
            "You are a professional agricultural expert for Indian farmers.\n"
            f"Context: The user recently diagnosed a plant with '{disease}' "
            f"(Confidence: {confidence}%). Default recommended treatment: {treatment}.\n\n"
            "Rules for your response:\n"
            "1. Read the 'User Query'. If it specifies a format (e.g., '🌱 Overview: ...'), FOLLOW that exact format completely.\n"
            "2. If it's a general question, answer specifically and contextually.\n"
            "3. DO NOT repeat the exact same response every time. Adapt to what the user asks.\n"
            "4. Keep wording simple, practical, and farmer-friendly.\n"
            "5. If they ask an unrelated non-agricultural question, politely guide them back to agriculture."
        )

    prompt = f"{system_instruction}\n\nUser Query: {user_message}"

    try:
        gemini_key = os.getenv('GEMINI_API_KEY')
        if not gemini_key:
            logger.warning('GEMINI_API_KEY not set, falling back to rule-based chatbot')
            return rule_based_chatbot(message)

        genai.configure(api_key=gemini_key)
        model = genai.GenerativeModel('gemini-pro')

        # FIX: The original code was throwing an exception because it used model.generate instead of model.generate_content
        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(
                temperature=0.3,
                max_output_tokens=400,
            )
        )

        ai_text = str(response.text).strip()
        if not ai_text:
            raise ValueError('Empty response from Gemini')

        return ai_text

    except Exception as e:
        logger.warning(f"AI API failed ({str(e)}), falling back to rule-based chatbot")
        return rule_based_chatbot(message)


def handle_chatbot(message):
    """Handle chatbot using AI, fallback to the rule-based logic."""
    context = {'last_prediction': session.get('last_prediction')} if session.get('last_prediction') else {}
    logger.info(f"Chatbot context retrieved: {context}")
    return generate_ai_response(message, context)

# ================= ROUTES =================
@app.route("/")
def home():
    """Home page."""
    return render_template("index.html")

@app.route("/about")
def about():
    """About page."""
    return render_template("about.html")

@app.route("/contact")
def contact():
    """Contact page."""
    return render_template("contact.html")

@app.route('/uploads/<filename>')
def display_image(filename):
    """Serve uploaded images."""
    return send_from_directory(UPLOAD_FOLDER, filename)

@app.route("/predict", methods=["POST"])
def predict():
    """Handle image upload and prediction."""
    try:
        if not model_loaded:
            flash('Model not loaded. Please try again later.', 'error')
            return redirect(url_for('home'))
        
        if 'file' not in request.files:
            flash('No file provided.', 'warning')
            return redirect(url_for('home'))
        
        file = request.files['file']
        if not file or file.filename == "":
            flash('No file selected.', 'warning')
            return redirect(url_for('home'))
        
        if not allowed_file(file.filename):
            flash('Invalid file type.', 'error')
            return redirect(url_for('home'))
        
        filename = secure_filename(file.filename)
        unique_filename = f"{uuid.uuid4().hex}_{filename}"
        filepath = os.path.join(UPLOAD_FOLDER, unique_filename)
        
        file.seek(0, os.SEEK_END)
        file_size = file.tell()
        file.seek(0)
        
        if file_size > MAX_FILE_SIZE or file_size == 0:
            flash('Invalid file size.', 'error')
            return redirect(url_for('home'))
        
        file.save(filepath)
        
        disease, confidence = predict_disease(filepath)
        
        if disease is None:
            cleanup_file(filepath)
            flash('Error processing image.', 'error')
            return redirect(url_for('home'))
        
        if confidence < CONFIDENCE_THRESHOLD:
            cleanup_file(filepath)
            flash(f'Low confidence ({confidence}%). Please provide a clearer image.', 'warning')
            return redirect(url_for('home'))
        
        treatment = get_treatment(disease)
        
        # Format disease name for display
        formatted_disease = format_disease_name(disease)
        
        # Get confidence categorization
        confidence_level, confidence_color, confidence_message = get_confidence_level(confidence)
        
        # Store in session for chatbot context
        session['last_prediction'] = {
            'disease': formatted_disease,
            'raw_disease': disease,
            'confidence': confidence,
            'treatment': treatment
        }
        
        logger.info(f"Session last_prediction set: disease={formatted_disease}, confidence={confidence}%, treatment={treatment}")
        
        return render_template("result.html", 
                             disease=formatted_disease, 
                             confidence=confidence,
                             confidence_level=confidence_level,
                             confidence_color=confidence_color,
                             confidence_message=confidence_message,
                             treatment=treatment, 
                             img_path=f"/uploads/{unique_filename}")
        
    except Exception as e:
        cleanup_file(filepath) if 'filepath' in locals() else None
        logger.error(f"Error in predict: {str(e)}")
        flash('Unexpected error.', 'error')
        return redirect(url_for('home'))

@app.route("/reset")
def reset_context():
    """Reset chatbot context by clearing last prediction."""
    session.pop('last_prediction', None)
    return redirect(url_for('home'))

@app.route('/chat', methods=['POST'])
def chat():
    """AI chatbot for plant disease queries."""
    try:
        data = request.get_json(force=True, silent=True)
        if not data or 'message' not in data or not str(data.get('message')).strip():
            return jsonify({'reply': 'Please provide a valid message in JSON.'}), 400
        
        reply = handle_chatbot(data.get('message'))
        return jsonify({'reply': reply}), 200
        
    except Exception as e:
        logger.error(f"Chat error: {str(e)}")
        return jsonify({'reply': 'Error occurred'}), 500

# ================= ERROR HANDLERS =================
@app.errorhandler(404)
def not_found(error):
    return render_template('index.html'), 404

@app.errorhandler(500)
def internal_error(error):
    flash('Server error occurred.', 'error')
    return render_template('index.html'), 500

# ================= INITIALIZATION =================
@app.before_request
def before_request():
    if not model_loaded:
        load_resources()

if __name__ == "__main__":
    if not load_resources():
        logger.critical("Failed to load resources. Exiting.")
        exit(1)
    
    logger.info("Application started successfully.")
    app.run(debug=True, host='0.0.0.0', port=5000)