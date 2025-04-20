# 🧠 GenAI Voice Assistant (LangChain + Groq + Streamlit)

A conversational **voice assistant** built using **LangChain**, **Groq's Qwen LLM**, **Streamlit**, and audio processing tools. The assistant enables natural spoken interaction with an AI agent — record your voice, transcribe it, generate a response, and hear the AI speak back!

---

## 🎯 Features

- 🎙️ **Voice Input**: Record your voice using your mic.
- 🗣️ **Speech-to-Text**: Transcribe using Google's STT (SpeechRecognition).
- 🧠 **LLM Response**: Generates responses with Groq's Qwen LLM via LangChain.
- 🔊 **Voice Output**: AI speaks back using offline TTS (pyttsx3).
- 🔁 **Multi-Turn Chat**: Maintains chat history with both audio and text per turn.
- 🧹 **Auto-Cleanup**: Automatically deletes temp audio files after each round.
- 🖥️ **Interactive UI**: Web app powered by Streamlit.

---

## 🚀 Tech Stack

- [LangChain](https://www.langchain.com/) + [Groq](https://groq.com/) — for LLM communication
- [Streamlit](https://streamlit.io/) — for frontend UI
- [Google STT](https://pypi.org/project/SpeechRecognition/) — for speech-to-text
- [pyttsx3](https://pypi.org/project/pyttsx3/) — for offline text-to-speech
- [sounddevice](https://pypi.org/project/sounddevice/) + [soundfile](https://pypi.org/project/SoundFile/) — for audio recording/playback

---

## 🛠️ Setup Instructions

1. **Clone the Repository**

```bash
git clone https://github.com/djgaikwad/GenAI-Voice-Assistant.git
cd GenAI-Voice-Assistant
```

2. **Create Virtual Environment and Install Dependencies**

```bash
python -m venv venv
# Activate environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

3. **Add Your API Keys to a `.env` File**

```
LANGCHAIN_API_KEY=your_langchain_key
GROQ_API_KEY=your_groq_key
```

4. **Run the App**

```bash
streamlit run app.py
```

---

## 📁 File Structure

```
├── app.py              # Main Streamlit app
├── audio_utils.py      # Audio handling (record, transcribe, TTS, clean)
├── .env                # API keys (excluded from Git)
├── requirements.txt    # Project dependencies
```

---

## 📌 Use Cases

- 🎧 Personal voice-based AI assistant
- 🧑‍🦽 Accessibility-focused voice interfaces
- 🛎️ Customer service assistant prototype
- 🧾 Conversational AI for kiosks, devices, and voice-first apps

---

## 🙌 Credits

Built by [Dhananjay Gaikwad](https://linkedin.com/in/djgaikwad)  
Powered by Groq, LangChain, and Streamlit
