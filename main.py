import streamlit as st
from src.chatbot import firstaidschatbot
st.title('🎈 FirstAid chatbot')

# Store LLM generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "How may I help you?"}]


# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])






# User-provided prompt
if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)




# Generate a new response if last message is not from assistant
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = firstaidschatbot(f"{st.session_state.messages[-10:]}" ) 
            st.write(response) 
    message = {"role": "assistant", "content": response}
    st.session_state.messages.append(message)




