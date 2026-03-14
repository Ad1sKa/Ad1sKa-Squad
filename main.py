import streamlit as st
import os
import requests
from datetime import datetime

# --- 1. НАСТРОЙКИ ---
MASTER_PASSWORD = "342z50f9dcrtxj6-mk87" 
GROUP_CHAT_ID = "-1003816680156"
# Прямой токен
BOT_TOKEN = "8714620396:AAGRsWh-vcDEzWE4GqE19d8zUy4znnHYRho"

st.set_page_config(page_title="Ad1sKa Squad HQ", page_icon="🛡️")

# --- 2. СТИЛЬ ---
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #ffffff; }
    h1 { color: #FFD700; text-align: center; font-family: 'Arial Black'; }
    .stButton>button { width: 100%; border-radius: 10px; border: 1px solid #FFD700; background-color: #1a1a1a; color: white; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. ШАПКА ---
start_date = datetime(2026, 3, 14) 
delta = datetime.now() - start_date
st.title("AD1SKA SQUAD HQ")
st.markdown(f"<h3 style='text-align: center; color: #00FF00;'>🛡️ ВМЕСТЕ: {delta.days} ДНЕЙ</h3>", unsafe_allow_html=True)
st.divider()

# --- 4. SOS ПАНЕЛЬ ---
st.sidebar.header("🔐 ПАНЕЛЬ АРХИТЕКТОРА")
input_pass = st.sidebar.text_input("Ключ доступа", type="password")

if input_pass == MASTER_PASSWORD:
    st.sidebar.success("Доступ разрешен!")
    if st.sidebar.button("🚨 ЗАПУСТИТЬ SOS"):
        msg = f"🚨 ВНИМАНИЕ! АРХИТЕКТОР ОБЪЯВИЛ ОБЩИЙ СБОР! 🚨\nВРЕМЯ: {datetime.now().strftime('%H:%M:%S')}"
        url = f"https://api.telegram.org{BOT_TOKEN}/sendMessage"
        
        try:
            # Делаем запрос с таймаутом, чтобы не зависало
            res = requests.post(url, data={"chat_id": GROUP_CHAT_ID, "text": msg}, timeout=10)
            
            if res.status_code == 200:
                st.sidebar.snow()
                st.sidebar.success("СИГНАЛ УШЕЛ В ЧАТ!")
            else:
                st.sidebar.error(f"Ошибка Telegram: {res.status_code}")
                st.sidebar.write(res.text) # Покажет точную причину (например, бот не админ)
        except Exception as e:
            st.sidebar.error(f"Ошибка сети: {e}")
else:
    if input_pass:
        st.sidebar.error("Неверный ключ")

# --- 5. ДОКУМЕНТЫ ---
st.subheader("📁 АРХИВ")
files = {
    "📜 ДЕКЛАРАЦИЯ": "декларация о независимости.txt",
    "⚖️ КОДЕКС": "кодекс поведения и правила.txt",
    "🛡️ ЗАКОНЫ": "свод законов.txt",
    "📄 ХАРТИЯ": "хартия.txt"
}
cols = st.columns(2)
for i, (name, path) in enumerate(files.items()):
    with cols[i % 2]:
        if st.button(name):
            if os.path.exists(path):
                with open(path, "r", encoding="utf-8") as f: st.info(f.read())

# --- 6. ГИМН ---
if os.path.exists("гимн.mp3"):
    st.divider()
    st.audio("гимн.mp3")

st.caption("© 2026 Ad1sKa Squad HQ")
