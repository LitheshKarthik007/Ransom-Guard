# RansomGuard

## Intelligent Machine Learning-Based Ransomware Detection and Early Threat Prevention System

RansomGuard is a machine-learning-based prototype for detecting potential ransomware activity from memory-forensic/system feature data.

The system uses a trained Random Forest classifier to classify feature data as **Benign** or **Ransomware**. It also provides a confidence value, risk level, early threat alert, and recommended response actions.

> **Important:** The current prototype works with a CSV containing the 55 numerical features expected by the trained model. It does not directly analyze a `.raw` memory dump or perform automatic system isolation. Direct memory-forensic integration and automated prevention are planned as future enhancements.

---

## Features

- Upload a forensic feature CSV through a Streamlit web interface
- Validate the required 55 ML features
- Check for invalid or missing values
- Use a trained Random Forest model for prediction
- Display:
  - Prediction
  - Confidence
  - Risk level
- Generate an early threat alert for high-risk ransomware predictions
- Provide safe recommended response actions
- Simple and student-friendly dashboard interface

---

## Project Structure

```text
RansomGuard/
│
├── models/
│   └── ransomguard_model.pkl
│
├── app.py
├── predict.py
├── ransomegaurd.py
├── test_prediction.py
├── style.css
├── Obfuscated-MalMem2022.csv
├── RansomGuard_Benign_Sample.csv
├── requirements.txt
└── README.md
```

### File Description

| File | Purpose |
|---|---|
| `ransomegaurd.py` | Trains and evaluates the Random Forest model |
| `predict.py` | Loads the trained model and handles prediction, confidence, and risk calculation |
| `app.py` | Streamlit application and user interface |
| `test_prediction.py` | Tests the model with benign and ransomware samples |
| `style.css` | Styling for the Streamlit interface |
| `models/ransomguard_model.pkl` | Saved trained Random Forest model |
| `Obfuscated-MalMem2022.csv` | Dataset used for model training |
| `RansomGuard_Benign_Sample.csv` | Example benign feature CSV for testing |
| `requirements.txt` | Required Python packages |

---

## Machine Learning Workflow

```text
MalMem2022 Dataset
        ↓
Select Benign and Ransomware Samples
        ↓
Extract 55 Numerical Features
        ↓
Train/Test Split
        ↓
Random Forest Classifier
        ↓
Model Evaluation
        ↓
Save Trained Model
        ↓
Streamlit Application
        ↓
Upload Feature CSV
        ↓
Prediction + Confidence
        ↓
Risk Assessment
        ↓
Early Threat Alert
```

---

## Dataset Processing

The original dataset contains benign and multiple malware categories.

For the current ransomware detection task:

- Rows with `Category = Benign` are treated as **Benign**
- Rows whose `Category` contains `Ransomware` are treated as **Ransomware**
- Other malware categories are excluded from the binary ransomware classification task
- `Category` and the original `Class` columns are not used as model input
- The model uses the resulting **55 numerical features**

---

## Requirements

- Python 3.10 or newer
- Windows, Linux, or macOS
- Required Python packages listed in `requirements.txt`

---

## Installation

Open a terminal inside the RansomGuard folder.

### 1. Create a virtual environment (recommended)

```bash
python -m venv venv
```

### 2. Activate the environment on Windows

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

---

## Running the Project

### Train the model

If you need to train the model again:

```bash
python ransomegaurd.py
```

The trained model will be saved as:

```text
models/ransomguard_model.pkl
```

### Test the model

```bash
python test_prediction.py
```

### Run the Streamlit application

```bash
python -m streamlit run app.py
```

The application will open in your browser.

---

## Using the Application

1. Open RansomGuard.
2. Upload a CSV containing the required 55 features.
3. RansomGuard validates the uploaded file.
4. Click **Detect Threat**.
5. The trained Random Forest model analyzes the samples.
6. The application displays:
   - Prediction
   - Confidence
   - Risk Level
7. If ransomware activity is detected with high risk, an early threat alert and recommended response actions are shown.

### Example Test File

The project includes:

```text
RansomGuard_Benign_Sample.csv
```

This file contains one benign sample with the 55 features required by the model.

---

## Risk Levels

| Risk | Meaning |
|---|---|
| LOW | No immediate ransomware threat detected |
| MEDIUM | Suspicious activity detected; further investigation recommended |
| HIGH | Potential ransomware activity detected; early threat alert triggered |

The current prototype uses the model confidence to determine the ransomware risk level.

---

## Important Limitation

RansomGuard is a machine-learning research/prototype system.

The current version:

- Does not directly read a Windows `.raw` memory dump
- Does not automatically extract the 55 features from raw memory
- Does not automatically kill processes
- Does not automatically disconnect the system from the network
- Does not guarantee real-world ransomware detection

The model's performance is based on the dataset used for training and testing.

---

## Future Scope

### 1. Automated Memory Forensics

Integrate tools such as Volatility to directly analyze Windows memory dump files and automatically extract relevant forensic features.

```text
Memory Dump (.raw)
        ↓
Memory Forensics
        ↓
Feature Extraction
        ↓
55 Features
        ↓
RansomGuard Model
```

### 2. Real-Time Monitoring

Extend the system to continuously monitor system activity and detect suspicious behaviour earlier.

### 3. Automated Prevention

A future version can provide controlled automated containment actions for high-confidence threats, such as network isolation and restricting suspicious activity.

### 4. Intelligent Recovery

Integrate secure backup and recovery mechanisms to help restore affected systems after a confirmed ransomware incident.

---

## Project Goal

The goal of RansomGuard is to demonstrate how machine learning can be used with memory-forensic/system-level features to identify patterns associated with ransomware activity and provide an early warning before further damage occurs.

