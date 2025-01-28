# German -> Swedish Translator w/ TTS
## Translate text from German to Swedish and create a .mp3 file using Text To Speech to read aloud the translated text with it's spoken language.

This program was written by me, with the help of ChatGPT (primarily helped with the binary stuff) because I was unprepared for my German test. So, at 5am I wrote this program that does the following:

1. Reads input.txt
2. Parses each line, which it translates and converts to TTS.
3. Creates a .mp3 file for the first half of the translation (the german), and the second half (the swedish).
4. It adds a 2~ second silence and copies the binary from the swedish audio file to the german file.
5. Once every file is generated and combined, it combines all of them with the method above.
6. Optionally, it will loop the output.mp3 x times, incase you need the audio file the entire duration of the exam and cannot pause it.

## How To Use
Well it's fairly simple. 

1. Install all the libraries from ```requirements.txt```.
2. Import your translation. Use '-' as a seperator between German and Swedish (example in ```input.txt```).
3. Modify your desired loops. In ```main.py```, change the ```loop_audio_file(combined_file, final_output_file, num_loops=x)``` to any number you want.
4. Make sure the audio file is to your liking. There's a chance that your characters aren't recognizable by the TTS engine or the Translator.
