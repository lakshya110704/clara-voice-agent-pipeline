import whisper
import os

AUDIO_FOLDER = "Sample Data"
OUTPUT_FOLDER = "dataset"

model = whisper.load_model("base")

def transcribe_all():
    print("Scanning for audio files...")

    for file in os.listdir(AUDIO_FOLDER):
        if file.endswith(".m4a") or file.endswith(".mp3") or file.endswith(".wav"):
            audio_path = os.path.join(AUDIO_FOLDER, file)

            output_name = file.split(".")[0] + "_transcript.txt"
            output_path = os.path.join(OUTPUT_FOLDER, output_name)

            print(f"\nTranscribing: {audio_path}")

            result = model.transcribe(audio_path)
            transcript = result["text"]

            with open(output_path, "w") as f:
                f.write(transcript)

            print(f"Saved transcript → {output_path}")

if __name__ == "__main__":
    transcribe_all()