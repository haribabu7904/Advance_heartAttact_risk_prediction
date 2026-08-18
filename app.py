import streamlit as st
import pandas as pd
from src.utils import load_models

# =========================================================
# ⚙️ Page Config
# =========================================================
st.set_page_config(
    page_title="❤️ Heart Attack Risk Predictor",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# 🎨 Background Styling
# =========================================================
def add_bg_image(image_url: str):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{image_url}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

def add_bg_video(video_url: str):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: none;
        }}
        video.stVideoBackground {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            object-fit: cover;
            z-index: -1;
            opacity: 0.3;
            filter: brightness(0.6) contrast(1.2);
        }}
        </style>
        <video autoplay loop muted playsinline class="stVideoBackground">
            <source src="{video_url}" type="video/mp4">
        </video>
        """,
        unsafe_allow_html=True
    )

# =========================================================
# 🔐 Authentication
# =========================================================
USER_CREDENTIALS = {"admin": "admin123", "doctor": "doctor123"}

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

# =========================================================
# 🧠 Load Model
# =========================================================
try:
    model, scaler = load_models()
except Exception as e:
    model, scaler = None, None
    st.error(f"⚠️ Model not loaded: {e}")


# 🔑 💫 Ultra-Professional Login Page (Refined Design)
# =========================================================
def login_page():
    # Heartbeat video background
    add_bg_video("https://ak.picdn.net/shutterstock/videos/3641247839/preview/stock-footage-loop-animation-d-heart-beating-neon-pulse.mp4")

    # ================== Custom CSS ==================
    st.markdown("""
        <style>
        /* Full-page style reset */
        .main {
            padding: 0;
            margin: 0;
            overflow: hidden !important;
        }

       
      

        @keyframes slideFadeIn {
            from {opacity: 0; transform: translate(-50%, -45%);}
            to {opacity: 1; transform: translate(-50%, -50%);}
        }

        /* Title with gradient glow */
        .login-title {
            font-size: 28px;
            font-weight: 800;
            background: linear-gradient(90deg, #ff3366, #ff6699, #ff99cc);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 0 0 25px rgba(255, 51, 102, 0.5);
            letter-spacing: 1px;
            margin-bottom: 35px;
            animation: glowPulse 2s infinite alternate;
        }

        @keyframes glowPulse {
            from { text-shadow: 0 0 15px #ff3366; }
            to { text-shadow: 0 0 30px #ff99cc; }
        }

        /* Input box styling */
        .stTextInput input {
            border-radius: 10px;
            border: none !important;
            background: rgba(255,255,255,0.95);
            color: #000;
            font-size: 15px;
            height: 45px !important;
            box-shadow: 0 0 15px rgba(255, 51, 102, 0.3);
            
            transition: 0.3s ease-in-out;
        }
        .stTextInput input:focus {
            box-shadow: 0 0 25px rgba(255, 51, 102, 0.7);
        }

        /* Centered login button */
        .login-btn-container {
            display: flex;
            justify-content: center;
            margin-top: 25px;
        }

      .stButton > button {
            background-color: #ff3366 !important;
            color: white !important;
            border: none;
            border-radius: 12px;
            font-size: 16px;
            font-weight: bold;
            padding: 8px 20px;
            transition: all 0.3s ease;
        }
        .stButton > button:hover {
            background-color: #ff6699 !important;
            transform: scale(1.05);
        }

        /* Footer */
        .footer-text {
            margin-top: 30px;
            color: #f5f5f5;
            font-size: 12px;
            opacity: 0.9;
            text-align: center;
            letter-spacing: 0.5px;
        }

        /* Hide Streamlit's default UI */
        header, footer, .stSidebar {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)

    # ================== Login Card ==================
    st.markdown("<div class='login-container'>", unsafe_allow_html=True)
    st.markdown("<div class='login-title'>💓 Heart Attack Risk Predictor</div>", unsafe_allow_html=True)

    username = st.text_input("👤 Username", placeholder="Enter your username")
    password = st.text_input("🔑 Password", type="password", placeholder="Enter your password")

    st.markdown("<div class='login-btn-container'>", unsafe_allow_html=True)
    login_button = st.button("Login", key="login_btn")
    st.markdown("</div>", unsafe_allow_html=True)

    if login_button:
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            st.session_state["logged_in"] = True
            st.success("✅ Login successful! Redirecting...")
            st.rerun()
        else:
            st.error("❌ Invalid username or password")

  
# =========================================================
# 💓 Prediction Page (Unchanged)
# =========================================================
def prediction_page():
    add_bg_image("https://t3.ftcdn.net/jpg/07/13/57/84/360_F_713578474_ntazf68jlruzS5pim40YnpObO73AaYGM.jpg")
    st.markdown("""
        <style>
        .main { overflow: hidden !important; }
        h1, h2, h3, p, label {
            color: #ffffff !important;
            text-shadow: 0 0 12px #ff3366, 0 0 24px #ff6699;
        }
        .stTextInput input, .stNumberInput input, .stSelectbox select {
            height: 35px !important;
            font-size: 14px !important;
            background-color: rgba(255,255,255,0.9) !important;
            color: #000 !important;
            border: 1px solid #ff3366 !important;
            border-radius: 8px;
        }
        .stButton > button {
            background-color: #ff3366 !important;
            color: white !important;
            border: none;
            border-radius: 12px;
            font-size: 16px;
            font-weight: bold;
            padding: 8px 20px;
            transition: all 0.3s ease;
        }
        .stButton > button:hover {
            background-color: #ff6699 !important;
            transform: scale(1.05);
        }
        .logout-container {
            position: fixed;
            top: 15px;
            right: 25px;
            z-index: 10000;
        }
        .logout-container button {
            background-color: rgba(255,51,102,0.9);
            color: white;
            border: none;
            border-radius: 8px;
            padding: 8px 16px;
            font-weight: 600;
            font-size: 15px;
            cursor: pointer;
            box-shadow: 0 0 10px rgba(255, 51, 102, 0.6);
        }
        .logout-container button:hover {
            background-color: rgba(255,80,120,1);
        }
       
        @keyframes fadeIn { from {opacity: 0;} to {opacity: 1;} }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="logout-container">', unsafe_allow_html=True)
    if st.button("🚪 Logout"):
        st.session_state["logged_in"] = False
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<h1 style='text-align:center;'>💓 Heart Attack Risk Prediction</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; font-size:16px;'>Enter patient details below to assess heart attack risk instantly.</p>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("Age", 1, 120, 55)
        sex_display = st.selectbox("Sex", ["Male", "Female"])
        sex = 1 if sex_display == "Male" else 0
        cp = st.number_input("Chest Pain Type (0–3)", 0, 3, 1)
        trestbps = st.number_input("Resting BP", 50, 250, 130)
        chol = st.number_input("Cholesterol (mg/dl)", 50, 600, 250)
        fbs = st.selectbox("Fasting Sugar >120 mg/dl", [0, 1])
    with col2:
        restecg = st.number_input("Resting ECG (0–2)", 0, 2, 1)
        thalach = st.number_input("Max Heart Rate", 50, 250, 150)
        exang = st.selectbox("Exercise Angina", [0, 1])
        oldpeak = st.number_input("ST Depression", 0.0, 10.0, 1.0, 0.1)
        slope = st.number_input("Slope (0–2)", 0, 2, 1)
        ca = st.number_input("Major Vessels (0–3)", 0, 3, 0)
        thal = st.number_input("Thal (0=normal,1=fixed,2=reversible)", 0, 2, 1)

    st.markdown("---")

    if st.button("🔍 Predict Risk"):
        if model is None or scaler is None:
            st.error("⚠️ Model not loaded. Please check model file.")
        else:
            data = pd.DataFrame([[age, sex, cp, trestbps, chol, fbs, restecg,
                                   thalach, exang, oldpeak, slope, ca, thal]],
                                columns=['age', 'sex', 'cp', 'trestbps', 'chol',
                                         'fbs', 'restecg', 'thalach', 'exang',
                                         'oldpeak', 'slope', 'ca', 'thal'])
            data_scaled = scaler.transform(data)
            pred = model.predict(data_scaled)[0]
            try:
                proba = model.predict_proba(data_scaled)[0][1]
            except Exception:
                proba = None

            st.markdown('<div class="prediction-card">', unsafe_allow_html=True)
            if pred == 1:
                st.error(f"🚨 **High Risk of Heart Attack!** (Probability: {proba:.2f})" if proba else "🚨 **High Risk of Heart Attack!**")
            else:
                st.success(f"💚 **Low Risk of Heart Attack** (Probability: {proba:.2f})" if proba else "💚 **Low Risk of Heart Attack**")
            st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# 🚀 Main App
# =========================================================
def main():
    if st.session_state["logged_in"]:
        prediction_page()
    else:
        login_page()

if __name__ == "__main__":
    main()
