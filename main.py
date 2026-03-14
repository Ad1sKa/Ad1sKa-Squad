import streamlit as st
import os
from datetime import datetime

# --- 1. НАСТРОЙКИ ---
MASTER_PASSWORD = "342z50f9dcrtxj6-mk87" 

st.set_page_config(page_title="Ad1sKa Squad", page_icon="🛡️")

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
        text-decoration: none; font-weight: bold; font-size: 22px; border: 2px solid #FFD700; 
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
input_pass = st.sidebar.text_input("Введите ключ Архитектора", type="password")

if input_pass == MASTER_PASSWORD:
    st.sidebar.success("Доступ разрешен!")
    st.subheader("🚨 ЭКСТРЕННЫЙ ВЫЗОВ")
    
    # ЖЕЛЕЗОБЕТОННАЯ ССЫЛКА БЕЗ СЛОЖНЫХ КОДИРОВОК
    # Она просто открывает группу. Текст напишешь сам за секунду.
    st.markdown('<a href="https://t.me" target="_blank" class="sos-link">📢 ПЕРЕЙТИ В ГРУППУ И ДАТЬ SOS</a>', unsafe_allow_html=True)
    st.caption("Нажми на кнопку, тебя перекинет в группу @ad1skasquad. Напиши 'SOS' и все!")
else:
    if input_pass:
        st.sidebar.error("Неверный ключ!")

# --- 3. ВЕРХОВНЫЙ АРХИВ ---
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
                st.error(f"Файл {path} не найден")

# --- 4. ЗОЛОТОЙ СОСТАВ ---
st.divider()
st.subheader("👥 БРАТСТВО СКВАДА")
squad_members = [
    {"role": "👑 Архитектор (Основатель)", "nick": "Ad1sKa"},
    {"role": "🛡️ Участник", "nick": "Ник_1"},
    {"role": "🛡️ Участник", "nick": "Ник_2"}
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
