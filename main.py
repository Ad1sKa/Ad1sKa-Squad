import streamlit as st
import os
import requests
from datetime import datetime

# --- 1. НАСТРОЙКИ И ДАННЫЕ (ОТРЕДАКТИРУЙ ЭТО) ---
BOT_TOKEN = "8714620396:AAGRsWh-vcDEzWE4GqE19d8zUy4znnHYRho"
GROUP_CHAT_ID = "-5268681894"
MASTER_PASSWORD = "342z50f9dcrtxj6-mk87" # Твой секретный ключ Архитектора

st.set_page_config(page_title="Ad1sKa Squad HQ", page_icon="🛡️")

# --- 2. СТИЛИЗАЦИЯ (ЗОЛОТО НА ЧЕРНОМ) ---
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #ffffff; }
    h1 { color: #FFD700; text-align: center; font-family: 'Arial Black'; text-shadow: 2px 2px #000; }
    .stButton>button { width: 100%; border-radius: 10px; border: 1px solid #FFD700; background-color: #1a1a1a; color: white; transition: 0.3s; }
    .stButton>button:hover { background-color: #FFD700; color: black; }
    .css-10trblm { color: #FFD700; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. ТАЙМЕР ЕДИНСТВА ---
start_date = datetime(2026, 3, 14) # Дата основания
delta = datetime.now() - start_date

st.title("AD1SKA SQUAD HQ")
st.markdown(f"<h3 style='text-align: center; color: #00FF00;'>🛡️ МЫ ЕДИНЫ: {delta.days} ДНЕЙ</h3>", unsafe_allow_html=True)
st.divider()

# --- 4. ПАНЕЛЬ АРХИТЕКТОРА (В БОКОВОЙ ПАНЕЛИ) ---
st.sidebar.header("🔐 ДОСТУП АРХИТЕКТОРА")
input_pass = st.sidebar.text_input("Введите секретный ключ", type="password")

if input_pass == MASTER_PASSWORD:
    st.sidebar.success("Доступ разрешен!")
    if st.sidebar.button("🚨 ОТПРАВИТЬ SOS В ГРУППУ"):
        text = "🚨 ВНИМАНИЕ! АРХИТЕКТОР ОБЪЯВИЛ ОБЩИЙ СБОР! 🚨\nВСЕМ УЧАСТНИКАМ AD1SKA SQUAD СРОЧНО ВЫЙТИ НА СВЯЗЬ!"
        url = f"https://api.telegram.org{BOT_TOKEN}/sendMessage"
        try:
            res = requests.post(url, data={"chat_id": GROUP_CHAT_ID, "text": text})
            if res.status_code == 200:
                st.sidebar.snow()
                st.sidebar.success("Сигнал успешно отправлен в Telegram!")
            else:
                st.sidebar.error(f"Ошибка: {res.status_code}. Проверь токен и ID группы.")
        except Exception as e:
            st.sidebar.error(f"Сбой связи: {e}")
else:
    if input_pass:
        st.sidebar.error("Неверный ключ!")

# --- 5. ЦИФРОВОЙ АРХИВ (ДОКУМЕНТЫ) ---
st.subheader("📁 ВЕРХОВНЫЙ АРХИВ")
files = {
    "📜 ДЕКЛАРАЦИЯ": "декларация о независимости.txt",
    "⚖️ КОДЕКС И ПРАВИЛА": "кодекс поведения и правила.txt",
    "🛡️ ВЕРХОВНЫЕ ЗАКОНЫ": "свод законов.txt",
    "📄 ОБЩАЯ ХАРТИЯ": "хартия.txt"
}

col1, col2 = st.columns(2)
for i, (name, path) in enumerate(files.items()):
    with (col1 if i % 2 == 0 else col2):
        if st.button(name):
            if os.path.exists(path):
                with open(path, "r", encoding="utf-8") as f:
                    st.info(f.read())
            else:
                st.error(f"Файл '{path}' не найден в репозитории.")

# --- 6. ЗОЛОТОЙ СОСТАВ ---
st.divider()
st.subheader("👥 БРАТСТВО СКВАДА")
squad_members = [
    {"role": "👑 Архитектор (Основатель)", "nick": "Ad1sKa"},
    {"role": "🛡️ Участник", "nick": "Тут_твой_друг_1"},
    {"role": "🛡️ Участник", "nick": "Тут_твой_друг_2"}
]

for member in squad_members:
    st.markdown(f"**{member['role']}**: `{member['nick']}`")

# --- 7. ПЛЕЕР ГИМНА ---
st.divider()
st.subheader("🎵 ГИМН КОМАНДЫ")
if os.path.exists("гимн.mp3"):
    st.audio("гимн.mp3")
else:
    st.caption("Файл гимн.mp3 не найден")

st.divider()
st.caption("© 2026 Ad1sKa Squad. Система защищена кодом Архитектора.")
