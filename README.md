# AI Text Detection App

This is a Streamlit application that can detect whether a given text is AI-generated or human-written using machine learning.

## Features

- Text input interface
- Real-time AI/Human text classification
- Clean and simple user interface

## Setup

1. Clone the repository:
```bash
git clone https://github.com/Timothy-student/DissertationAI.git
cd DissertationAI
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:
- Windows:
```bash
.\venv\Scripts\activate
```
- Unix/MacOS:
```bash
source venv/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Download the model files:
```bash
python download_models.py
```

## Usage

1. Run the Streamlit app:
```bash
streamlit run app.py
```

2. Open your browser and navigate to `http://localhost:8501`

3. Enter text in the input box and click "Detect" to get the prediction

## Requirements

- Python 3.x
- Streamlit
- scikit-learn
- pandas
- numpy
- gdown

## Model Files

The model files (`vectorizer.pkl` and `ensemble_model.pkl`) are hosted on Google Drive due to their large size. They will be automatically downloaded when you run `download_models.py`. If you encounter any issues with the automatic download, you can manually download them from:

- [vectorizer.pkl](https://drive.google.com/file/d/1SIV-YeKikXg_aVasxkDbfb5UpozRzhYy/view?usp=drive_link)
- [ensemble_model.pkl](https://drive.google.com/file/d/1ReW_Equ658Ft_c3zWUlvcbPu879yiIaI/view?usp=drive_link)

After manual download, place the files in the `models` directory. 