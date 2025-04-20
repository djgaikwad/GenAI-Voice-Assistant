# 🧠 GenAI Voice Assistant (LangChain + Groq + Streamlit)

A conversational **voice assistant** built using **LangChain**, **Groq's Qwen LLM**, **Streamlit**, and audio processing tools. The assistant enables natural spoken interaction with an AI agent — record your voice, transcribe it, generate a response, and hear the AI speak back!

---

## 🎯 Features

- 🎙️ **Voice Input**: Record your voice and transcribe using Google's STT API.
- 🧠 **LLM Response**: Uses Groq's Qwen LLM via LangChain to generate context-aware replies.
- 🔊 **Voice Output**: Hear the AI's response using offline TTS (pyttsx3).
- 🔁 **Multi-Turn Chat**: Maintain chat history across turns with both audio & text.
- 🧹 **Auto-Cleanup**: Deletes temporary audio files after every round for better memory usage.
- 🖥️ **Interactive UI**: Built with Streamlit for a seamless web interface.

---

## 🚀 Tech Stack

- **LangChain** + **Groq** (LLM interaction)
- **Streamlit** (Frontend UI)
- **Google STT (SpeechRecognition)** for voice transcription
- **pyttsx3** for text-to-speech (offline)
- **sounddevice**, **soundfile** for audio recording

---

## 🛠️ Setup

1. Clone the repository:

```bash
git clone https://github.com/djgaikwad/GenAI-Voice-Assistant.git
cd GenAI-Voice-Assistant

2. Create virtual environment and install dependencies:

python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt

3. Add your .env file with keys:

LANGCHAIN_API_KEY=your_langchain_key
GROQ_API_KEY=your_groq_key

4. Run the Streamlit app:

streamlit run app.py

# File Structure

