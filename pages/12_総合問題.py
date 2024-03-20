import streamlit as st

from modules.no_1 import main as no_1
from modules.no_2 import main as no_2
from modules.no_3 import main as no_3

# 問題リスト
questions = {
    "1": "問題1",
    "2": "問題2",
    "3": "問題3",
}

# リストボックスの表示
selected_question = st.selectbox("問題を選択してください", list(questions.keys()))


# 選択した問題の表示
match selected_question:
    case "1":
        no_1()
    case "2":
        no_2()
    case "3":
        no_3()
