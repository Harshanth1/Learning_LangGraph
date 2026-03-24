# import streamlit as st
# from transformers import Pipeline

# from chat_bot import ChatBot

# mybot=ChatBot()
# workflow=mybot()

# # set uping Streamlit app UI
# st.title("ChatBot with LangGraph")
# st.write("Ask me any question, and I will try to answer it!")

# # INput text box for the question
# question=st.text_input("Enter Your Question here:")

# input={"messages":[question]}

# # Button to get the ansswer
# if st.button("Get Answer"):
#     if input:
#         response=workflow.invoke(input)
#         st.write("**Answer:**", response['messages'][-1].content)
#     else:
#         st.warning("Please enter a question to get an answer.")

# # Additional styling 
# st.markdown("---")
# st.caption("This chatbot is powered by LangGraph and Qwen3-32b model. It can also use tools to fetch real-time information.")

import streamlit as st
import uuid
from chat_bot import ChatBot

# ---------------- Page Config ----------------
st.set_page_config(page_title="AI ChatBot", layout="wide")

# ---------------- Custom Styling ----------------
st.markdown("""
<style>
    .stChatMessage {
        padding: 12px;
        border-radius: 12px;
        margin-bottom: 12px;
    }
</style>
""", unsafe_allow_html=True)

# ---------------- Initialize ----------------
if "bot" not in st.session_state:
    st.session_state.bot = ChatBot()

if "threads" not in st.session_state:
    st.session_state.threads = {}

if "current_thread" not in st.session_state:
    thread_id = str(uuid.uuid4())
    st.session_state.current_thread = thread_id
    st.session_state.threads[thread_id] = []

if "is_streaming" not in st.session_state:
    st.session_state.is_streaming = False

bot = st.session_state.bot
thread_id = st.session_state.current_thread

# ---------------- Sidebar ----------------
with st.sidebar:
    st.markdown("## 💬 Chats")

    # New Chat
    if st.button("➕ New Chat", use_container_width=True):
        new_id = str(uuid.uuid4())
        st.session_state.current_thread = new_id
        st.session_state.threads[new_id] = []
        st.rerun()

    st.markdown("---")

    # Chat list with titles
    for tid, messages in st.session_state.threads.items():
        title = "New Chat"

        for role, msg in messages:
            if role == "user":
                title = msg[:30]
                break

        if st.button(title, key=tid, use_container_width=True):
            st.session_state.current_thread = tid
            st.rerun()

# ---------------- Header ----------------
st.title("🤖 AI ChatBot with Memory and Web Search")

# ---------------- Chat Display ----------------
messages = st.session_state.threads[thread_id]

for i, (role, msg) in enumerate(messages):
    # Prevent duplicate rendering of streaming message
    if i == len(messages) - 1 and role == "assistant" and st.session_state.is_streaming:
        continue

    if role == "user":
        with st.chat_message("user", avatar="🧑"):
            st.markdown(msg)
    else:
        with st.chat_message("assistant", avatar="🤖"):
            st.markdown(msg)

# ---------------- Input ----------------
user_input = st.chat_input("Type your message...")

if user_input:
    # Start streaming
    st.session_state.is_streaming = True

    # Save user message
    st.session_state.threads[thread_id].append(("user", user_input))

    # Show user message
    with st.chat_message("user", avatar="🧑"):
        st.markdown(user_input)

    # Assistant response
    with st.chat_message("assistant", avatar="🤖"):
        placeholder = st.empty()
        placeholder.markdown("⏳ Thinking...")

        full_response = ""

        # Stream response
        for event in bot.stream([user_input], thread_id):
            messages = event["messages"]
            last_msg = messages[-1]

            if hasattr(last_msg, "content") and last_msg.content:
                full_response = last_msg.content
                placeholder.markdown(full_response)

    # Stop streaming
    st.session_state.is_streaming = False

    # Save response
    st.session_state.threads[thread_id].append(("assistant", full_response))

# ---------------- Footer ----------------
st.markdown("---")
st.caption("LangGraph + Qwen3-32B • Memory • Streaming • Clean UI")