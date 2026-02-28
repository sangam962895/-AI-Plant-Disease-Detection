import os
import json
import numpy as np
from flask import Flask, render_template, request, send_from_directory
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

app = Flask(__name__)

# ================= UPLOAD FOLDER =================
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ================= LOAD MODEL =================
model = load_model("plant_model.h5")

# ================= LOAD LABELS =================
with open("labels.json", "r") as f:
    labels = json.load(f)

IMG_SIZE = (224, 224)

# ================= PREDICTION =================
def predict_disease(img_path):
    img = image.load_img(img_path, target_size=IMG_SIZE)
    img_array = image.img_to_array(img)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)[0]

    class_index = np.argmax(prediction)
    confidence = float(np.max(prediction)) * 100

    disease_name = labels[str(class_index)]

    return disease_name, round(confidence, 2)

# ================= TREATMENT DATABASE =================
def get_treatment(disease):

    treatments = {

        "Tomato___Late_blight":
        "Apply copper based fungicide. Remove infected leaves. Avoid overhead watering and keep plant dry.",

        "Tomato___Early_blight":
        "Use Mancozeb fungicide and remove affected leaves. Ensure good air circulation.",

        "Potato___Early_blight":
        "Apply fungicide weekly and avoid leaf wetness. Remove infected plant debris.",

        "Apple___Apple_scab":
        "Spray sulfur fungicide weekly and prune affected branches.",

        "Corn___Common_rust":
        "Use resistant corn varieties and apply fungicide if infection spreads.",

        "Healthy":
        "Your plant is healthy 🌿. Maintain proper watering and sunlight."
    }

    return treatments.get(disease, "No specific treatment available. Please consult an agriculture expert.")

# ================= HOME =================
@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        file = request.files["file"]

        if file and file.filename != "":

            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)

            disease, confidence = predict_disease(filepath)
            treatment = get_treatment(disease)

            return render_template(
                "result.html",
                disease=disease,
                confidence=confidence,
                treatment=treatment,
                img_path="/uploads/" + file.filename
            )

    return render_template("index.html")

# ================= SERVE UPLOADED IMAGE =================
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

# ================= OTHER PAGES =================
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

# ================= RUN =================
if __name__ == "__main__":
    app.run(debug=True)