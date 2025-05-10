import streamlit as st
import cohere

# Initialize the Cohere client
co = cohere.Client('qjgBfmYonpwhjFsICmNvdVCL4idkxCaSJvt7qYMJ')  # Replace with your real API key

st.set_page_config(page_title="Weekend Planner", page_icon="🗓️")
st.title("🗓️ Weekend Planner")
st.write("Let me help you plan your weekend! 🎉")

# Chat input
user_input = st.text_input("Ask me anything about your weekend plans:")

if user_input:
    try:
        response = co.chat(
            message=user_input,
            model="command-r-plus",  # or "command-r"
            temperature=0.7,
            max_tokens=300,
        )
        st.markdown("### 📅 Weekend Planner Suggestion:")
        st.success(response.text.strip())
    except Exception as e:
        st.error(f"❌ Error: {e}")
