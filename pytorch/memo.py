import numpy as np

# Create a random array 'a' with shape (4, 8)
a = np.random.rand(4, 8)

# Select the first column of 'a' as 'b'
b = a[:, 0]

# Print 'a' and 'b'
print("Array a:\n", a)
print("\nArray b (first column of a):\n", b)

# import os
# from moviepy.editor import VideoFileClip

# def extract_audio_from_mp4(mp4_folder, wav_folder):
#     """
#     폴더에 있는 mp4 파일에서 wav 파일을 추출하여 저장.

#     Args:
#         mp4_folder (str): mp4 파일이 저장된 폴더 경로.
#         wav_folder (str): 추출된 wav 파일을 저장할 폴더 경로.
#     """
#     # wav 폴더가 없으면 생성
#     os.makedirs(wav_folder, exist_ok=True)

#     # mp4 폴더에서 모든 파일을 읽기
#     for filename in os.listdir(mp4_folder):
#         if filename.endswith('.mp4'):
#             mp4_path = os.path.join(mp4_folder, filename)
#             wav_path = os.path.join(wav_folder, os.path.splitext(filename)[0] + '.wav')
            
#             # mp4 파일에서 오디오 추출
#             try:
#                 print(f"Processing: {mp4_path}")
#                 video = VideoFileClip(mp4_path)
#                 video.audio.write_audiofile(wav_path, codec='pcm_s16le')  # WAV로 저장
#                 print(f"Saved: {wav_path}")
#             except Exception as e:
#                 print(f"Failed to process {mp4_path}: {e}")

# # 예제 사용법
# mp4_folder = "./vggsound_sparse_5s"  # mp4 파일이 있는 폴더 경로
# wav_folder = "./vggsound_sparse_5s_wav"  # wav 파일을 저장할 폴더 경로

# extract_audio_from_mp4(mp4_folder, wav_folder)



import os
from pydub import AudioSegment
from concurrent.futures import ProcessPoolExecutor

# 입력 폴더와 출력 폴더 설정
input_folder = "./resources/Audiosync"  # 원본 오디오 파일 폴더
output_folder = "./Audiosync_trimmed"  # 잘린 오디오 저장 폴더
os.makedirs(output_folder, exist_ok=True)

# 자를 길이 설정 (단위: milliseconds)
trim_length = 3200  # 3.2초
half_trim_length = trim_length // 2  # 중간 위치 계산

def trim_audio(file_path, output_path):
    try:
        # 오디오 파일 불러오기
        audio = AudioSegment.from_file(file_path)

        # 오디오 길이 (ms 단위)
        duration = len(audio)
        if duration < trim_length:
            print(f"Skipping {file_path}: Duration is less than 3.2 seconds")
            return

        # 중간 부분에서 3.2초 자르기
        start_time = (duration // 2) - half_trim_length
        end_time = start_time + trim_length
        trimmed_audio = audio[start_time:end_time]

        # 잘린 오디오 저장
        trimmed_audio.export(output_path, format="wav")
        print(f"Trimmed: {file_path}")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

def process_file(file_name):
    if file_name.endswith(".wav"):
        input_path = os.path.join(input_folder, file_name)
        output_path = os.path.join(output_folder, file_name)
        trim_audio(input_path, output_path)

# 모든 파일 가져오기
audio_files = [f for f in os.listdir(input_folder) if f.endswith(".wav")]

# 병렬 처리
with ProcessPoolExecutor() as executor:
    executor.map(process_file, audio_files)

print("All audio files have been trimmed.")
