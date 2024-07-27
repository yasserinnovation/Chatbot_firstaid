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




# Function for generating LLM response
def generate_response(prompt_input):
    # Hugging Face Login
    #sign = Login(email, passwd)
    #cookies = sign.login()
    # Create ChatBot                        
    #chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
    return firstaidschatbot(prompt_input)

# User-provided prompt
if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)




# Generate a new response if last message is not from assistant
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = generate_response(prompt, ) 
            st.write(response) 
    message = {"role": "assistant", "content": response}
    st.session_state.messages.append(message)




