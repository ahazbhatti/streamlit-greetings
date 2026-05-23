import streamlit as st
from datetime import datetime
import time

st.set_page_config(
    page_title="Greetings",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS styling
st.markdown("""
    <style>
        .main {
            padding-top: 2rem;
        }
        .greeting-container {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 3rem;
            border-radius: 20px;
            text-align: center;
            box-shadow: 0 8px 32px 0 rgba(102, 126, 234, 0.3);
        }
        .greeting-title {
            color: #ffffff;
            font-size: 3.5rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        }
        .greeting-subtitle {
            color: #e0e0ff;
            font-size: 1.8rem;
            font-weight: 300;
            margin-bottom: 2rem;
        }
        .info-box {
            background: rgba(255, 255, 255, 0.1);
            border-left: 4px solid #fff;
            padding: 1.5rem;
            border-radius: 8px;
            margin-top: 2rem;
            color: #ffffff;
            font-size: 1.1rem;
        }
    </style>
""", unsafe_allow_html=True)

# Get current greeting based on time
hour = datetime.now().hour
if hour < 12:
    time_greeting = "Good Morning"
    emoji = "🌅"
elif hour < 18:
    time_greeting = "Good Afternoon"
    emoji = "☀️"
else:
    time_greeting = "Good Evening"
    emoji = "🌙"

# Main greeting container
st.markdown(f"""
    <div class="greeting-container">
        <div class="greeting-title">{emoji} {time_greeting}! 👋</div>
        <div class="greeting-subtitle">Hello Ahaz</div>
        <div class="info-box">
            Welcome to your Streamlit greetings page! ✨
        </div>
    </div>
""", unsafe_allow_html=True)

# Additional content
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Welcome Status", value="Ready ✅")

time_placeholder = col2.empty()

with col3:
    st.metric(label="Date", value=datetime.now().strftime("%b %d"))

st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #666;'>
        <p>Built with ❤️ using Streamlit</p>
    </div>
""", unsafe_allow_html=True)

# Update the clock continuously
while True:
    time_placeholder.metric(label="Time", value=datetime.now().strftime("%H:%M:%S"))
    time.sleep(1)
