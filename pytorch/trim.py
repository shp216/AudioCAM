import os
import subprocess

def extract_audio_from_mp4(input_folder, output_folder):
    """
    Extract audio (as WAV) from all MP4 files in a folder.

    Args:
        input_folder (str): Path to the folder containing MP4 files.
        output_folder (str): Path to the folder where extracted WAV files will be saved.
    """
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Iterate through all MP4 files in the input folder
    for file_name in os.listdir(input_folder):
        if file_name.endswith(".mp4"):
            input_path = os.path.join(input_folder, file_name)
            output_file_name = os.path.splitext(file_name)[0] + ".wav"
            output_path = os.path.join(output_folder, output_file_name)

            # Use ffmpeg to extract audio
            command = [
                "ffmpeg",
                "-i", input_path,   # Input MP4 file
                "-vn",              # Disable video
                "-acodec", "pcm_s16le",  # WAV format
                "-ar", "16000",   # Set sample rate to 16kHz
                output_path          # Output WAV file
            ]

            try:
                print(f"Extracting audio from {file_name}...")
                subprocess.run(command, check=True)
                print(f"Saved WAV file to {output_path}")
            except subprocess.CalledProcessError as e:
                print(f"Failed to process {file_name}: {e}")
                


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--input_folder', type=str, required=True, help="Path to the folder containing MP4 files.")
    parser.add_argument('--output_folder', type=str, required=True, help="Path to the folder to save extracted WAV files.")

    args = parser.parse_args()

    extract_audio_from_mp4(args.input_folder, args.output_folder)
