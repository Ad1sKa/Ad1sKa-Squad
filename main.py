import streamlit as st
import os

# Настройка страницы
st.set_page_config(page_title="Ad1sKa Squad HQ", page_icon="🛡️")

# Стилизация под золото и черный цвет
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    h1 { color: #FFD700; text-align: center; }
    .stButton>button { width: 100%; border-radius: 10px; border: 1px solid #FFD700; background-color: #1a1a1a; color: white; height: 3em; }
    </style>
    """, unsafe_allow_html=True)

st.title("AD1SKA SQUAD HQ")
st.write("● СИСТЕМА УПРАВЛЕНИЯ АКТИВНА")

# Список файлов
files = {
    "📜 ДЕКЛАРАЦИЯ": "декларация о независимости.txt",
    "⚖️ КОДЕКС И ПРАВИЛА": "кодекс поведения и правила.txt",
    "🛡️ ВЕРХОВНЫЕ ЗАКОНЫ": "свод законов.txt",
    "📄 ОБЩАЯ ХАРТИЯ": "хартия.txt",
    "🎵 ГИМН СКВАДА": "гимн.txt"
}

# Кнопки документов
for name, path in files.items():
    if st.button(name):
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                st.info(f.read())
        else:
            st.error(f"Файл {path} не найден!")

# Плеер Гимна
st.divider()
st.subheader("🎵 ГИМН КОМАНДЫ")
if os.path.exists("гимн.mp3"):
    st.audio("гимн.mp3")
else:
    st.warning("Файл гимн.mp3 не загружен")

# Кнопка SOS
if st.button("🚨 СИГНАЛ СБОРА (SOS)", type="primary"):
    st.snow() # Визуальный эффект
    st.warning("ВНИМАНИЕ! СИГНАЛ SOS ЗАПУЩЕН!")
