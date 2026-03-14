import streamlit as st
import os
from datetime import datetime
import urllib.parse

# --- 1. НАСТРОЙКИ ---
# Твой пароль для доступа к кнопке SOS
MASTER_PASSWORD = "342z50f9dcrtxj6-mk87" 
# Ссылка на твою публичную группу
GROUP_LINK = "https://t.me/ad1skasquad" 

st.set_page_config(page_title="Ad1sKa Squad HQ", page_icon="🛡️")

# Стилизация (Золото на черном)
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #ffffff; }
    h1 { color: #FFD700; text-align: center; font-family: 'Arial Black'; text-shadow: 2px 2px #000; }
    .stButton>button { width: 100%; border-radius: 10px; border: 1px solid #FFD700; background-color: #1a1a1a; color: white; transition: 0.3s; }
    .stButton>button:hover { background-color: #FFD700; color: black; }
    .sos-link { 
        display: block; width: 100%; text-align: center; background-color: #CC0000; 
        color: white !important; padding: 15px; border-radius: 10px; 
        text-decoration: none; font-weight: bold; font-size: 20px; border: 2px solid #FFD700; 
    }
    .sos-link:hover { background-color: #FF0000; box-shadow: 0px 0px 15px #FFD700; }
    </style>
    """, unsafe_allow_html=True)

# Таймер единства
start_date = datetime(2026, 3, 14) 
delta = datetime.now() - start_date

st.title("AD1SKA SQUAD HQ")
st.markdown(f"<h3 style='text-align: center; color: #00FF00;'>🛡️ ВМЕСТЕ: {delta.days} ДНЕЙ</h3>", unsafe_allow_html=True)
st.divider()

# --- 2. ПАНЕЛЬ АРХИТЕКТОРА ---
st.sidebar.header("🔐 ПАНЕЛЬ УПРАВЛЕНИЯ")
input_pass = st.sidebar.text_input("Ключ Архитектора", type="password")

if input_pass == MASTER_PASSWORD:
    st.sidebar.success("Доступ разрешен!")
    st.subheader("🚨 ЭКСТРЕННЫЙ ВЫЗОВ")
    
    # Текст сообщения
    msg = "🚨 ВНИМАНИЕ! АРХИТЕКТОР ОБЪЯВИЛ ОБЩИЙ СБОР! ВСЕМ БЫТЬ НА СВЯЗИ! 🚨"
    encoded_msg = urllib.parse.quote(msg)
    
    # ПРЯМАЯ ССЫЛКА НА ГРУППУ С ТЕКСТОМ
    # Эта ссылка откроет конкретно твою группу и подставит текст
    share_url = f"https://t.me{GROUP_LINK}&text={encoded_msg}"
    
    st.markdown(f'<a href="{share_url}" target="_blank" class="sos-link">📢 ЗАПУСТИТЬ SOS В ГРУППУ</a>', unsafe_allow_html=True)
    st.caption("Нажми на кнопку -> Откроется Telegram -> Нажми 'Отправить' в группе.")
else:
    if input_pass:
        st.sidebar.error("Неверный ключ!")

# --- 3. ВЕРХОВНЫЙ АРХИВ ---
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
            else:
                st.error(f"Файл {path} не найден")

# --- 4. ЗОЛОТОЙ СОСТАВ ---
st.divider()
st.subheader("👥 БРАТСТВО СКВАДА")
squad_members = [
    {"role": "👑 Архитектор", "nick": "Ad1sKa"},
    {"role": "🛡️ Участник", "nick": "Твой_Друг_1"},
    {"role": "🛡️ Участник", "nick": "Твой_Друг_2"}
]
for member in squad_members:
    st.markdown(f"**{member['role']}**: `{member['nick']}`")

# --- 5. ГИМН ---
if os.path.exists("гимн.mp3"):
    st.divider()
    st.subheader("🎵 ГИМН КОМАНДЫ")
    st.audio("гимн.mp3")

st.divider()
st.caption("© 2026 Ad1sKa Squad. Система защищена.")
