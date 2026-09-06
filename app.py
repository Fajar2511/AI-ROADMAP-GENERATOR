
import streamlit as st
from google import genai
from google.genai import types

# Configure Streamlit page
st.set_page_config(
    page_title="AI Roadmap Generator",
    page_icon="🗺️",
    layout="centered"
)

# Get Gemini API Key from Streamlit Secrets
api_key = st.secrets["GEMINI_API_KEY"]


# Title
st.title("🗺️ AI Roadmap Generator")

st.write(
    "Enter your current skills and your goal, "
    "and I'll build a custom learning roadmap for you."
)


# User Inputs
current_skills = st.text_input(
    "What are your current skills?",
    placeholder="e.g., Python, HTML, CSS"
)

goal = st.text_input(
    "What is your goal?",
    placeholder="e.g., Become a Backend Developer"
)


# Generate Roadmap
if st.button("🚀 Generate Roadmap"):

    # Validation
    if not current_skills:
        st.warning("Please enter your current skills.")

    elif not goal:
        st.warning("Please enter your goal.")

    else:

        try:

            # Create Gemini Client
            client = genai.Client(
                api_key=api_key
            )

            # Prompt
            prompt = f"""
You are an expert career mentor and technical instructor.

Create a personalized learning roadmap.

Current Skills:
{current_skills}

Goal:
{goal}

Create a structured roadmap with:

1. Overview of the learning journey
2. Week-by-week learning plan
3. Topics to learn each week
4. Practical projects
5. Recommended resources to explore
6. Important milestones
7. Skills the learner should have at the end

Make the roadmap:

- Beginner-friendly
- Clear and structured
- Practical
- Actionable
- Encouraging

Use Markdown formatting with headings, bullet points,
and numbered lists.
"""

            with st.spinner("🤖 Generating your personalized roadmap..."):

                response = client.models.generate_content(

                    model="gemini-3.6-flash",

                    contents=prompt,

                    config=types.GenerateContentConfig(
                        temperature=0.7,
                        max_output_tokens=4000
                    )
                )

            # Display Result
            st.success("Roadmap generated successfully!")

            st.markdown("## 🗺️ Your Custom Learning Roadmap")

            st.markdown(response.text)


        except Exception as e:

            st.error("❌ An error occurred.")

            st.exception(e)


