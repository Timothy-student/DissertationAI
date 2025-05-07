import gdown
import os

def download_models():
    print("Downloading model files...")
    
    # Create models directory if it doesn't exist
    if not os.path.exists('models'):
        os.makedirs('models')
    
    # Google Drive file IDs and their corresponding filenames
    model_files = {
        'vectorizer.pkl': '1SIV-YeKikXg_aVasxkDbfb5UpozRzhYy',  # Vectorizer model
        'ensemble_model.pkl': '1ReW_Equ658Ft_c3zWUlvcbPu879yiIaI'  # Ensemble model
    }
    
    for filename, file_id in model_files.items():
        output_path = os.path.join('models', filename)
        if not os.path.exists(output_path):
            url = f'https://drive.google.com/uc?id={file_id}'
            gdown.download(url, output_path, quiet=False)
            print(f"Downloaded {filename}")
        else:
            print(f"{filename} already exists, skipping download")

if __name__ == "__main__":
    download_models() 