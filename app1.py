from flask import Flask, render_template, request, jsonify, redirect, url_for, flash, session, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import joblib
from sklearn.metrics import classification_report, accuracy_score
from PIL import Image , UnidentifiedImageError
import numpy as np
import os
import datetime
import random
import string
from hashlib import sha256
from io import BytesIO
import re

app = Flask(__name__)
app.config['SECRET_KEY'] = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'mysql+pymysql://root:root@localhost:3306/alzheimer')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'uploads')  # Add this line to configure UPLOAD_FOLDER
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100), nullable=False)
    dob = db.Column(db.Date, nullable=True)
    contact = db.Column(db.String(15), nullable=True)
    gender = db.Column(db.String(10), nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    confirm_password = db.Column(db.String(60), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class_labels = ["MildDemented", "ModerateDemented", "NonDemented", "VeryMildDemented"]
model_filename = 'svm_model.joblib'
model_path = os.path.join('models', model_filename)
loaded_model_svm = joblib.load(model_path)  # Ensure that this is the only place where 'model' is defined

ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def is_mri_image(img):
    try:
        # Check if the image mode is either grayscale ('L') or RGB ('RGB')
        if img.mode == 'L' or img.mode == 'RGB':
            # Check if the image size is either (176, 208) or (496, 248)
            if img.size == (176, 208) or img.size == (496, 248):
                return True
        return False
    except Exception as e:
        return False
    
def predict_alzheimer(img_path):
    try:
        img = Image.open(img_path)

        if not is_mri_image(img):
            return None, "Uploaded image is not an MRI image"


        # Convert the image to RGB if it's not already in RGB format
        img = img.convert("RGB")

        # Preprocess the image
        img = img.resize((128, 128))
        img_array = np.array(img)

        # Ensure that the image array has the correct number of pixels
        if img_array.shape != (128, 128, 3):
            return None, "Invalid image dimensions"

        # Flatten the image
        img_array_flat = img_array.flatten()

        # Reshape the flattened image array to match SVM input shape
        img_array_flat = img_array_flat[:16384]  # Keep only the first 16384 features
        img_array_flat = img_array_flat.reshape(1, -1)

        # Make predictions with the SVM model
        predictions = loaded_model_svm.predict(img_array_flat)

        # Convert the predicted label index to the corresponding class label
        predicted_class_label = class_labels[predictions[0]]

        # Return predictions as a numpy array
        return predictions, None
    except Exception as e:
        return None, str(e)
    
@app.context_processor
def inject_user():
    return dict(current_user=current_user)

@app.route('/favicon.ico')
def favicon():
    return url_for('static', filename='images/favicon.ico')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/model')
def model():
    return render_template('model.html')

@app.route('/visualization')
def visualization():
    # Your view logic for visualization goes here
    return render_template('visualization.html')

@app.route('/about')
def about():
    return render_template('about.html')

def generate_random_string(length=16):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        fullname = request.form['fullname']
        dob = datetime.datetime.strptime(request.form['dob'], '%Y-%m-%d').date() if request.form['dob'] else None
        contact = request.form['contact']
        gender = request.form['gender']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            flash('Passwords do not match. Please try again.', 'danger')
            return redirect(url_for('register'))

        if User.query.filter_by(email=email).first():
            flash('Email is already registered. Please use a different email.', 'danger')
            return redirect(url_for('register'))

        hashed_password = generate_password_hash(password)

        new_user = User(fullname=fullname, dob=dob, contact=contact, gender=gender, email=email, password=hashed_password, confirm_password=confirm_password)
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            login_user(user, remember=True)
            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid email or password. Please try again.', 'danger')

    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/predict', methods=['POST'])
@login_required
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    if file:
        try:
            img = Image.open(BytesIO(file.read()))

            if not is_mri_image(img):
                return jsonify({'error': 'Uploaded image is not an MRI image'})
        except Exception as e:
            return jsonify({'error': 'Cannot identify image file'})

        original_filename = file.filename
        img_path = os.path.join(app.config['UPLOAD_FOLDER'], original_filename)

        if not allowed_file(original_filename):
            return jsonify({'error': 'Unsupported file format'})

        img.save(img_path)

        predictions, error_message = predict_alzheimer(img_path)

        if error_message:
            return jsonify({'error': error_message})

        predicted_class_index = int(np.argmax(predictions, axis=-1))

        print("Shape of predictions:", predictions.shape)  # Add this line for debugging
        print("Predictions array:", predictions)  # Print the predictions array for debugging
        print("Predicted class index:", predicted_class_index)  # Print the predicted class index for debugging

        if isinstance(predictions, (list, np.ndarray)) and 0 <= predicted_class_index < len(predictions):
            confidence_score = float(predictions[predicted_class_index])

            session['result'] = {'class_label': class_labels[predicted_class_index], 'confidence': confidence_score}
            session['uploaded_image'] = original_filename

            return redirect(url_for('performance'))
        else:
            return jsonify({'error': 'Invalid predictions or predicted class index'})


@app.route('/performance')
@login_required
def performance():
    if 'result' not in session or 'uploaded_image' not in session:
        flash('Please upload an image first.', 'warning')
        return redirect(url_for('index'))

    return render_template('performance.html', result=session['result'])

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.app_context().push()
    db.create_all()
    app.run(debug=True)
