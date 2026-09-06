import streamlit as st
import google.generativeai as genai

# Configure Streamlit page
st.set_page_config(page_title="AI Roadmap Generator", page_icon="🗺️")

st.title("🗺️ AI Roadmap Generator")
st.write("Enter your current skills and your goal, and I'll build a custom roadmap for you.")

# Sidebar for API Key
api_key = st.sidebar.text_input("Enter your Gemini API Key", type="password")

# User inputs
current_skills = st.text_input("What are your current skills? (e.g., Python, basic HTML)")
goal = st.text_input("What is your goal? (e.g., Become a Backend Developer)")

if st.button("Generate Roadmap"):
    if not api_key:
        st.error("Please enter your Gemini API key in the sidebar.")
    elif not current_skills or not goal:
        st.warning("Please fill in both fields.")
    else:
        try:
            # Configure Gemini
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            prompt = f"""
            Create a structured learning roadmap for someone who currently knows: {current_skills}.
            They want to achieve this goal: {goal}.
            Provide the roadmap in a week-by-week format with clear actionable steps, 
            resources to look for, and key milestones. Keep it encouraging and technical.
            """
            
            with st.spinner("Generating your roadmap..."):
                response = model.generate_content(prompt)
                st.markdown("### Your Custom Roadmap")
                st.write(response.text)
                
        except Exception as e:
            st.error(f"An error occurred: {e}")

st.sidebar.info("Get your API key from [Google AI Studio](https://aistudio.google.com/)")
