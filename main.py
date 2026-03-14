import streamlit as st
import os
from datetime import datetime

# 1. НАСТРОЙКИ СТРАНИЦЫ
st.set_page_config(page_title="Ad1sKa Squad HQ", page_icon="🛡️")

# Стилизация под золото и темную сталь
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #ffffff; }
    h1 { color: #FFD700; text-align: center; font-family: 'Arial Black'; text-shadow: 2px 2px #000; }
    .stButton>button { width: 100%; border-radius: 10px; border: 1px solid #FFD700; background-color: #1a1a1a; color: white; transition: 0.3s; }
    .stButton>button:hover { background-color: #FFD700; color: black; border: 1px solid white; }
    </style>
    """, unsafe_allow_html=True)

# 2. ТАЙМЕР ЕДИНСТВА
# Укажи дату основания (Год, Месяц, День)
start_date = datetime(2026, 3, 14) 
now = datetime.now()
delta = now - start_date

st.title("AD1SKA SQUAD HQ")
st.markdown(f"<h3 style='text-align: center; color: #00FF00;'>🛡️ ВМЕСТЕ УЖЕ: {delta.days} ДНЕЙ</h3>", unsafe_allow_html=True)
st.divider()

# 3. ЦИФРОВОЙ АРХИВ (Документы)
st.subheader("📁 ВЕРХОВНЫЙ АРХИВ")
files = {
    "📜 ДЕКЛАРАЦИЯ": "декларация о независимости.txt",
    "⚖️ КОДЕКС И ПРАВИЛА": "кодекс поведения и правила.txt",
    "🛡️ ВЕРХОВНЫЕ ЗАКОНЫ": "свод законов.txt",
    "📄 ОБЩАЯ ХАРТИЯ": "хартия.txt"
}

# Размещаем кнопки в два столбика
col1, col2 = st.columns(2)
for i, (name, path) in enumerate(files.items()):
    with (col1 if i % 2 == 0 else col2):
        if st.button(name):
            if os.path.exists(path):
                with open(path, "r", encoding="utf-8") as f:
                    st.info(f.read())
            else:
                st.error("Файл не найден")

# 4. ЗОЛОТОЙ СОСТАВ
st.divider()
st.subheader("👥 БРАТСТВО СКВАДА")
# Список участников — впиши ники своих пацанов здесь
squad_members = [
    {"role": "👑 Архитектор (Основатель)", "nick": "Ad1sKa"},
    {"role": "🛡️ Участник", "nick": "Ник_1"},
    {"role": "🛡️ Участник", "nick": "Ник_2"},
    {"role": "🛡️ Участник", "nick": "Ник_3"}
]

for member in squad_members:
    st.markdown(f"**{member['role']}**: `{member['nick']}`")

# 5. ГИМН И СИГНАЛ SOS
st.divider()
st.subheader("🎵 ГИМН КОМАНДЫ")
if os.path.exists("гимн.mp3"):
    st.audio("гимн.mp3")

if st.button("🚨 ЗАПУСТИТЬ ОБЩИЙ СБОР (SOS)", type="primary"):
    st.snow()
    st.warning("ВНИМАНИЕ! ВСЕМ УЧАСТНИКАМ AD1SKA SQUAD НЕМЕДЛЕННО ВЫЙТИ НА СВЯЗЬ!")
