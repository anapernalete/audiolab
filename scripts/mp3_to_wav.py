import os
from dotenv import load_dotenv
from pydub import AudioSegment

# Load mp3 file

# Load environment variables from .env file
load_dotenv()

# Loop through all mp3 files in the input folder
def convert_mp3towav(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    
    for filename in os.listdir(input_folder):
        if filename.endswith(".mp3"):
            mp3_path = os.path.join(input_folder, filename)
            wav_path = os.path.join(output_folder, filename.replace(".mp3", ".wav"))
        
            # Convert mp3 to WAV
            audio = AudioSegment.from_mp3(mp3_path)
            audio.export(wav_path, format="wav")
            
            print(f"Converted {filename} to {wav_path}")

# Read paths from environment variables
input_folder = os.getenv("INPUT_FOLDER")
output_folder = os.getenv("OUTPUT_FOLDER")

convert_mp3towav(input_folder, output_folder)