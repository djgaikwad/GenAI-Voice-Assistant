import sounddevice as sd
import soundfile as sf
import speech_recognition as sr
import pyttsx3
import os
import glob
import tempfile

# def clean_audio_files():
#     for pattern in ["input.wav", "response.wav"]:
#         for file in glob.glob(pattern):
#             try:
#                 os.remove(file)
#             except Exception as e:
#                 print(f"Error deleting {file}: {e}")

def clean_audio_files():
    for pattern in ["input.wav", "response.wav"]:
        for file in glob.glob(pattern):
            if os.path.isfile(file):
                try:
                    os.remove(file)
                except Exception as e:
                    print(f"Error deleting {file}: {e}")


def record_audio(filename="input.wav", duration=5, samplerate=44100):
    print("🎙️ Recording... Speak now!")
    try:
        audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1)
        sd.wait()
        sf.write(filename, audio, samplerate)
        print(f"✅ Saved to {filename}")
    except Exception as e:
        print(f"Recording error: {e}")

def transcribe_audio(filename="input.wav"):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return "Sorry, could not understand audio."
    except sr.RequestError as e:
        return f"STT request error: {e}"

def speak_text(text, filename="response.wav"):
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.setProperty("volume", 1.0)


    engine.save_to_file(text, filename)
    engine.runAndWait()
    return filename