import streamlit as st
from audio_utils import record_audio, transcribe_audio, speak_text, clean_audio_files
from langchain_core.messages import HumanMessage, SystemMessage 
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os

load_dotenv()
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

llm = ChatGroq(model="Qwen-QWq-32b")

def chat_with_llm(user_input):
    prompt = ChatPromptTemplate.from_messages([
        ("system", ""),
        ("human", "{input}")
    ])
    messages = prompt.format_messages(input=user_input)
    response = llm(messages)
    content = response.content
    if "</think>" in content:
        content = content.split("</think>")[-1].strip()
    return content

st.set_page_config("🧠 GenAI Voice Assistant")
st.title("🧠 GenAI Voice Assistant (LangChain + Groq)")


# Initialize conversation round and chat history
if 'conversation_round' not in st.session_state:
    st.session_state.conversation_round = 0

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []


if st.button("🎙️ Start Conversation" if st.session_state.conversation_round == 0 else "🗣️ Continue Conversation"):
    clean_audio_files()

    with st.spinner("Recording..."):
        record_audio("input.wav", duration=10)
    st.success("✅ Recording complete!")

    # Playback input voice
    st.markdown("**🔊 Your Voice Input:**")
    st.audio("input.wav", format="audio/wav")

    with st.spinner("Transcribing..."):
        user_text = transcribe_audio("input.wav")
    st.markdown(f"**You:**")
    st.markdown(user_text)

    with st.spinner("Generating AI response..."):
        ai_response = chat_with_llm(user_text)
    # st.markdown(f"**🤖 AI:** {ai_response}")

    # Save to chat history
    st.session_state.chat_history.append({
        "user": user_text,
        "ai": ai_response,
        "user_audio": "input.wav",
        "ai_audio": "response.wav"
    })

    # TTS and play response
    audio_file = speak_text(ai_response)
    st.markdown("**🔊 AI Voice Response:**")
    st.audio(audio_file, format="audio/wav")
    st.markdown(f"**Assistant:**")
    st.markdown(ai_response)

    st.session_state.conversation_round += 1

if st.session_state.chat_history:
    st.markdown("### 🗃️ Conversation History")
    for i, entry in enumerate(st.session_state.chat_history):
        #st.markdown(f"**🧑 You:**")
        st.markdown(f"**You:**")
        st.markdown(entry['user'])
        st.markdown(f"**Assistant:**")
        #st.markdown(f"**🤖 AI:**")
        st.markdown(entry['ai'])


        st.markdown("---")



# if st.button("🎙️ Start Conversation" if st.session_state.conversation_round == 0 else "🗣️ Continue Conversation"):
#     clean_audio_files()

#     with st.spinner("Recording..."):
#         record_audio("input.wav", duration=10)
#     st.success("✅ Recording complete!")

#     with st.spinner("Transcribing..."):
#         user_text = transcribe_audio("input.wav")
#     st.markdown(f"**🧑 You:** {user_text}")

#     with st.spinner("Generating AI response..."):
#         ai_response = chat_with_llm(user_text)
#     st.markdown(f"**🤖 AI:** {ai_response}")

#     # Save to chat history
#     st.session_state.chat_history.append({"user": user_text, "ai": ai_response})

#     # TTS and play response
#     audio_file = speak_text(ai_response)
#     st.audio(audio_file, format="audio/wav")

#     st.session_state.conversation_round += 1

# if st.session_state.chat_history:
#     st.markdown("### 🗃️ Conversation History")
#     for i, entry in enumerate(st.session_state.chat_history):
#         st.markdown(f"**🧑 You:** {entry['user']}")
#         st.markdown(f"**🤖 AI:** {entry['ai']}")

#         st.markdown("---")
