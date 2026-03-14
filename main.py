import streamlit as st
import os
from datetime import datetime
import urllib.parse

# --- 1. НАСТРОЙКИ ---
MASTER_PASSWORD = "342z50f9dcrtxj6-mk87" 
# Ссылка на твою группу (возьми её в настройках группы, типа t.me/joinchat/...)
GROUP_LINK = "https://t.me/ad1skasquad" 

st.set_page_config(page_title="Ad1sKa Squad HQ", page_icon="🛡️")

# Стилизация
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #ffffff; }
    h1 { color: #FFD700; text-align: center; font-family: 'Arial Black'; }
    .stButton>button { width: 100%; border-radius: 10px; border: 1px solid #FFD700; background-color: #1a1a1a; color: white; height: 3em; }
    .sos-link { display: block; width: 100%; text-align: center; background-color: #CC0000; color: white; padding: 15px; border-radius: 10px; text-decoration: none; font-weight: bold; font-size: 20px; }
    </style>
    """, unsafe_allow_html=True)

# Таймер
start_date = datetime(2026, 3, 14) 
delta = datetime.now() - start_date
st.title("AD1SKA SQUAD HQ")
st.markdown(f"<h3 style='text-align: center; color: #00FF00;'>🛡️ ВМЕСТЕ: {delta.days} ДНЕЙ</h3>", unsafe_allow_html=True)
st.divider()

# --- 2. ПАНЕЛЬ АРХИТЕКТОРА ---
st.sidebar.header("🔐 ПАНЕЛЬ УПРАВЛЕНИЯ")
input_pass = st.sidebar.text_input("Введите ключ Архитектора", type="password")

if input_pass == MASTER_PASSWORD:
    st.sidebar.success("Доступ разрешен!")
    st.subheader("🚨 ЭКСТРЕННЫЙ ВЫЗОВ")
    
    # Готовим текст сообщения
    raw_text = "🚨 ВНИМАНИЕ! АРХИТЕКТОР ОБЪЯВИЛ ОБЩИЙ СБОР! ВСЕМ БЫТЬ НА СВЯЗИ! 🚨"
    encoded_text = urllib.parse.quote(raw_text)
    
    # Создаем прямую ссылку для шаринга в Telegram
    # Эта ссылка откроет выбор чата или конкретный чат с вписанным текстом
    share_url = f"https://t.me{GROUP_LINK}&text={encoded_text}"
    
    st.markdown(f'<a href="{share_url}" target="_blank" class="sos-link">📢 ЗАПУСТИТЬ SOS В ГРУППУ</a>', unsafe_allow_html=True)
    st.caption("При нажатии откроется Telegram: выбери группу Squad и нажми отправить.")
else:
    if input_pass:
        st.sidebar.error("Неверный ключ!")

# --- 3. АРХИВ ДОКУМЕНТОВ ---
st.subheader("📁 ВЕРХОВНЫЙ АРХИВ")
files = {
    "📜 ДЕКЛАРАЦИЯ": "декларация о независимости.txt",
    "⚖️ КОДЕКС": "кодекс поведения и правила.txt",
    "🛡️ ЗАКОНЫ": "свод законов.txt",
    "📄 ХАРТИЯ": "хартия.txt"
}

col1, col2 = st.columns(2)
for i, (name, path) in enumerate(files.items()):
    with (col1 if i % 2 == 0 else col2):
        if st.button(name):
            if os.path.exists(path):
                with open(path, "r", encoding="utf-8") as f:
                    st.info(f.read())

# --- 4. ГИМН ---
if os.path.exists("гимн.mp3"):
    st.divider()
    st.audio("гимн.mp3")

st.divider()
st.caption("© 2026 Ad1sKa Squad. Все права защищены.")
