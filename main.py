import streamlit as st
import os
from datetime import datetime

# 1. НАСТРОЙКИ СТРАНИЦЫ
st.set_page_config(page_title="Ad1sKa Squad HQ", page_icon="🛡️")

# Стилизация (Золото на черном)
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #ffffff; }
    h1 { color: #FFD700; text-align: center; font-family: 'Arial Black'; }
    .stButton>button { width: 100%; border-radius: 10px; border: 1px solid #FFD700; background-color: #1a1a1a; color: white; }
    .css-10trblm { color: #FFD700; } /* Цвет текста в инфо-боксах */
    </style>
    """, unsafe_allow_html=True)

# 2. ТАЙМЕР ЕДИНСТВА (Пункт 5)
# Укажи здесь дату основания команды (Год, Месяц, День)
start_date = datetime(2026, 3, 14) 
now = datetime.now()
delta = now - start_date

st.title("AD1SKA SQUAD HQ")
st.markdown(f"<h3 style='text-align: center; color: #00FF00;'>🛡️ МЫ ЕДИНЫ: {delta.days} ДНЕЙ</h3>", unsafe_allow_html=True)

# 3. ДОКУМЕНТЫ (Твой архив)
st.subheader("📁 ОФИЦИАЛЬНЫЙ АРХИВ")
files = {
    "📜 ДЕКЛАРАЦИЯ": "декларация о независимости.txt",
    "⚖️ КОДЕКС И ПРАВИЛА": "кодекс поведения и правила.txt",
    "🛡️ ВЕРХОВНЫЕ ЗАКОНЫ": "свод законов.txt",
    "📄 ОБЩАЯ ХАРТИЯ": "хартия.txt",
    "🎵 ГИМН СКВАДА": "гимн.txt"
}

col1, col2 = st.columns(2)
for i, (name, path) in enumerate(files.items()):
    with (col1 if i % 2 == 0 else col2):
        if st.button(name):
            if os.path.exists(path):
                with open(path, "r", encoding="utf-8") as f:
                    st.info(f.read())
            else:
                st.error("Файл не найден")

# 4. ГОЛОСОВАНИЕ (Пункт 3)
st.divider()
st.subheader("🗳️ ОБЩЕЕ ГОЛОСОВАНИЕ")
topic = "Куда двигаем сегодня?" # Можно менять прямо в коде
options = ["🍟 Шаурма", "🍕 Пицца", "🎮 Компьютерный клуб", "🏃 Просто движ"]
vote = st.radio(topic, options)
if st.button("ПОДТВЕРДИТЬ ГОЛОС"):
    st.success(f"Твой голос за '{vote}' учтен! (Демократия в действии)")

# 5. СОСТАВ КОМАНДЫ (Пункт 1)
st.divider()
st.subheader("👥 ЗОЛОТОЙ СОСТАВ")
# Список участников (Добавляй своих пацанов сюда)
squad = {
    "Архитектор (Основатель)": "Ad1sKa",
    "Участник #2": "Тут будет ник",
    "Участник #3": "Тут будет ник",
    "Участник #4": "Тут будет ник"
}

for role, nick in squad.items():
    st.markdown(f"**{role}**: `{nick}`")

# 6. ГИМН И SOS
st.divider()
if os.path.exists("гимн.mp3"):
    st.audio("гимн.mp3")

if st.button("🚨 СИГНАЛ СБОРА (SOS)", type="primary"):
    st.snow()
    st.warning("ВНИМАНИЕ! ВСЕМ УЧАСТНИКАМ ВЫЙТИ НА СВЯЗЬ!")
