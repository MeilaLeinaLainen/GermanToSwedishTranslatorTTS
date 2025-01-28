from googletrans import Translator
from gtts import gTTS
import os

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def text_to_speech(text, lang, output_file):
    if text.strip():
        tts = gTTS(text, lang=lang)
        tts.save(output_file)
    else:
        print(f"Texten är tom för språket {lang}, ingen ljudfil skapades.")

def create_silence(duration_ms, sample_rate=22050, channels=1, sample_width=2):
    silence = b'\0' * (duration_ms * sample_rate * channels * sample_width // 1000)
    return silence

def combine_audio_files(audio_files, silence_duration_ms=1000):
    combined_audio_data = b''

    for file in audio_files:
        with open(file, 'rb') as f:
            audio_data = f.read()
            combined_audio_data += audio_data

        silence = create_silence(silence_duration_ms)
        combined_audio_data += silence

    output_file = 'final_output.mp3'
    with open(output_file, 'wb') as output:
        output.write(combined_audio_data)

    print(f"Sammanslagen ljudfil skapad: {output_file}")
    return output_file

def loop_audio_file(input_file, output_file, num_loops=2):
    with open(input_file, 'rb') as f:
        audio_data = f.read()

    repeated_audio_data = audio_data * num_loops

    with open(output_file, 'wb') as output:
        output.write(repeated_audio_data)

    print(f"Ljudfilen har loopats {num_loops} gånger och sparats som: {output_file}")

def process_line(line, output_file_prefix, line_number):
    if "-" in line:
        german_part, swedish_part = line.split("-", 1)
        german_part = german_part.strip()
        swedish_part = swedish_part.strip()

        german_audio_file = f"{output_file_prefix}_german_{line_number}.mp3"
        text_to_speech(german_part, lang='de', output_file=german_audio_file)

        swedish_audio_file = f"{output_file_prefix}_swedish_{line_number}.mp3"
        text_to_speech(swedish_part, lang='sv', output_file=swedish_audio_file)

        print(f"Ljudfil skapad för rad {line_number}: {german_audio_file} och {swedish_audio_file}")
        return german_audio_file, swedish_audio_file
    else:
        print(f"Rad '{line}' saknar bindestreck och hoppades över.")
        return None, None

def main():
    input_file = 'input.txt'
    output_file_prefix = 'output'

    text = read_file(input_file)
    lines = text.splitlines()
    audio_files = []

    for i, line in enumerate(lines, 1):
        german_audio_file, swedish_audio_file = process_line(line, output_file_prefix, i)
        if german_audio_file:
            audio_files.append(german_audio_file)
        if swedish_audio_file:
            audio_files.append(swedish_audio_file)

    combined_file = combine_audio_files(audio_files)

    for file in audio_files:
        os.remove(file)

    final_output_file = 'looped_final_output.mp3'
    loop_audio_file(combined_file, final_output_file, num_loops=8)

    print("Alla ljudfiler har slagits samman och loopats.")

if __name__ == '__main__':
    main()
