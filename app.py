import streamlit as st
import json
import os

st.set_page_config(page_title="2/5講義復習クイズ")

# URLのパラメータを取得（例: ?file=questions15-21.json）
query_params = st.query_params
default_file = query_params.get("file", "questions15-21.json") # 指定がなければこれをデフォルトに

if os.path.exists(default_file):
    with open(default_file, 'r', encoding='utf-8') as f:
        quizzes = json.load(f)
    
    st.title("📖 2/5講義復習クイズ")

    for i, q in enumerate(quizzes):
        q_id = q.get('id', i + 1)
        st.subheader(f"Q{q_id}. {q['question']}")
        user_choice = st.radio("選択肢を選んでください", q['options'], key=f"q{q_id}")
        
        if st.button(f"Q{q_id}の答え合わせ", key=f"btn{q_id}"):
            correct_index = q['answer'] - 1 
            if q['options'].index(user_choice) == correct_index:
                st.success("✨ 正解です！")
            else:
                st.error(f"❌ 正解は: {q['options'][correct_index]}")
            if 'explanation' in q:
                st.info(f"💡 解説: {q['explanation']}")
        st.markdown("---")
else:
    st.error(f"指定された問題ファイル '{default_file}' が見つかりません。")