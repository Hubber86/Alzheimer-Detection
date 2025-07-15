## 🧠 AI Brain Imaging for Early Neurodegenerative Disease Detection

[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
![GitHub Repo stars](https://img.shields.io/github/stars/Hubber86/Alzheimer-Detection?style=social)
![GitHub forks](https://img.shields.io/github/forks/Hubber86/Alzheimer-Detection?style=social)
![GitHub last commit](https://img.shields.io/github/last-commit/Hubber86/Alzheimer-Detection)

> A Flask-based web application for early detection of Alzheimer’s disease using deep learning on brain MRI scans. The system classifies the uploaded image into Alzheimer’s stages using CNN, SVM, and transfer learning models like VGG16 and InceptionV3.

---

## 📍 Project Info

- 🎓 **Academic Year**: 2023–2024  
- 🏫 **Department**: Electronics and Computer Engineering  
- 🏢 **College**: PES’s Modern College of Engineering, Shivajinagar, Pune  
- 👨‍🎓 **Student**: Prajwal Bhimrao Kalashetty (B190315026)
## This application is designed to assist healthcare professionals and individuals by providing early detection of neurodegenerative diseases using artificial intelligence.

---

## 🎯 Objectives

- Create a deep learning-based system for Alzheimer’s detection using MRI scans.
- Provide a user-friendly interface for image upload and model prediction.
- Integrate multiple models (CNN, SVM, VGG16, Inception) for performance comparison.
- Assist doctors and individuals in early diagnosis and awareness.

---

## 🧰 Technologies & Frameworks 🧪

| Category         | Tools / Technologies                      |
|------------------|-------------------------------------------|
| 👨‍💻 Programming Language | Python 3.11+                            |
| 🌐 Web Framework  | Flask, HTML, CSS, Bootstrap               |
| 🧠 AI Frameworks  | TensorFlow, scikit-learn, joblib          |
| 🖼️ Image Processing | Pillow, NumPy                             |
| 📊 Visualization   | Matplotlib                               |
| ☁️ Deployment      | Vercel (Frontend), Heroku (Backend)       |
| 💻 IDEs           | VS Code, Jupyter Notebook                 |

---

## 🧠 Models Used
| Model              | Description                                                     | Icon |
| ------------------ | --------------------------------------------------------------- | ---- |
| **🧮 CNN**         | Custom Convolutional Neural Network for MRI classification      | 🧠   |
| **📊 SVM**         | Traditional Support Vector Machine for high-accuracy prediction | 💡   |
| **🎯 VGG16**       | Pretrained deep CNN architecture with 16 layers                 | 🧱   |
| **🔍 InceptionV3** | Deep CNN with multi-scale feature extraction                    | 🔎   |
| **🧱 ResNet50**    | 50-layer Residual Network, avoids vanishing gradients           | 🏗️  |

These models were trained and/or fine-tuned on the Alzheimer’s MRI dataset to detect disease stages like Mild Demented, Moderate Demented, Non-Demented, and Very Mild Demented.

---
## ⚙️ Technologies, Languages & Tools

### 🖥️ Languages
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

### 🌐 Frameworks & Libraries
![Flask](https://img.shields.io/badge/Flask-black?style=for-the-badge&logo=flask)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy)
![Pillow](https://img.shields.io/badge/Pillow-3656A6?style=for-the-badge&logo=python&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-006699?style=for-the-badge&logo=matplotlib&logoColor=white)
![Jinja2](https://img.shields.io/badge/Jinja2-B41717?style=for-the-badge&logo=jinja&logoColor=white)

### 🎨 Frontend
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)

### 🧠 ML Models
![CNN](https://img.shields.io/badge/CNN-Custom-brightgreen?style=for-the-badge)
![SVM](https://img.shields.io/badge/SVM-Support%20Vector%20Machine-blue?style=for-the-badge)
![VGG16](https://img.shields.io/badge/VGG16-Transfer%20Learning-orange?style=for-the-badge)
![InceptionV3](https://img.shields.io/badge/InceptionV3-GoogLeNet-blueviolet?style=for-the-badge)
![ResNet50](https://img.shields.io/badge/ResNet50-Deep%20Residual%20Network-red?style=for-the-badge)

### 🛠️ IDEs & Tools
![VS Code](https://img.shields.io/badge/VSCode-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github)

### 🚀 Deployment
![Vercel](https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white)
![Heroku](https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white)

---

## 📂 Project Structure

```
Alzheimer-Detection/
├── app.py
├── requirements.txt
├── vercel.json
├── models/
├── static/
├── templates/
│   └── layout/
├── .gitignore
├── README.md
└── LICENSE
```

---

## 🚀 Demo Workflow

1. **Upload** a brain MRI scan (`.jpg` or `.png` format).
2. The **backend** processes the image using a **pre-trained deep learning model**.
3. The model predicts one of the following classes:
   - `NonDemented`
   - `VeryMildDemented`
   - `MildDemented`
   - `ModerateDemented`
4. The **predicted class** and **confidence score** are displayed instantly on the UI.
5. The image is automatically **saved** to a directory corresponding to the predicted class.

---

## 📊 Model Accuracy Comparison

| Model                    | Accuracy (%) |
|--------------------------|--------------|
| SVM                      | **99.06**     |
| CNN1Model.h5             | 92.54         |
| Combined Model (joblib)  | ~90.8         |
| DenseNet121              | 78.68         |
| InceptionV3              | 85.87         |
| ResNet50                 | 88.67         |
| VGG16                    | 62.48         |

📊 *See: `accuracy_comparison.png` for visual chart.*

---

## 🌐 Deployment Notes

- Vercel (for frontend only) may not support heavy backend inference.
- Recommended full-stack setup:
  - **Frontend** ➝ Vercel
  - **Backend (Flask)** ➝ Heroku / Render / Railway

---

## 🚀 Installation (Local Development)
1. Clone the repo:

git clone https://github.com/Hubber86/Alzheimer-Detection.git
cd Alzheimer-Detection

2. Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies:

pip install -r requirements.txt

4. Run the Flask app:

python app.py

---

## 📌 References
Alzheimer's MRI Dataset - Kaggle
TensorFlow Documentation
scikit-learn Documentation
Flask Documentations

---

## 🎓 Education

- 🧑‍🎓 **B.E. in Electronics & Computer Engineering**  
  *P.E.S Modern College of Engineering, Pune*

---

## 🧠 Research & Publications

📘 *AI-Powered Brain Imaging for Early Neurodegenerative Disease Detection*  
Presented at **MITADTSoCiCon 2024 | IEEE Indexed**  
**Authors**: Prajwal B Kalashetty, Avdhut R Punekar, Sourav H Lokhande, Hemalata Nawale

- 🔗 [Semantic Scholar](https://www.semanticscholar.org/author/Prajwal-Bhimrao-Kalashetty/2309514769)  
- 🔗 [ResearchGate](https://www.researchgate.net/publication/381936844_AI-Powered_Brain_Imaging_for_Early_Neurodegenerative_Disease_Detection)  
- 🔗 [IEEE Xplore](https://ieeexplore.ieee.org/author/551042883560161)

---

## ⚖️ License

This project is licensed under the **MIT License**.  
📄 [View License »](LICENSE)

```text
MIT License © 2025 Prajwal Bhimrao Kalashetty
```

---

## 📈 GitHub Stats

![Prajwal's GitHub stats](https://github-readme-stats.vercel.app/api?username=Hubber86&show_icons=true&theme=radical)

---

> 💬 For questions, suggestions, or collaborations, feel free to connect via GitHub.

---
