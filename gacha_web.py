import streamlit as st
from PIL import Image
import math

st.set_page_config(page_title="スタレ ガチャ計算ツール", layout="centered")

# 背景画像設定（CSSで）
def set_bg(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
    encoded = f"data:image/png;base64,{data.hex()}"
    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{data.encode('base64').decode()}");
            background-size: cover;
        }}
        </style>
    """, unsafe_allow_html=True)

# set_bg("images/background.jpg")  # ← このCSS背景は上手くいかない時があるためコメントアウト中

st.title("⭐スタレ ガチャ計算ツール⭐")

st.subheader("現在の所持石数・チケット")
col1, col2 = st.columns(2)
with col1:
    current_石 = st.number_input("石（個）", min_value=0, value=0)
with col2:
    current_券 = st.number_input("券（枚）", min_value=0, value=0)

st.markdown("---")
st.subheader("入手予定項目")

col1, col2, col3 = st.columns(3)
with col1:
    庭 = st.checkbox("庭")
with col2:
    女児 = st.checkbox("女児")
with col3:
    末日 = st.checkbox("末日")

st.markdown("### 石系入力")
月パス = st.number_input("月パス（日分）", min_value=0, value=0)
デイリー = st.number_input("デイリー（日分）", min_value=0, value=0)
模擬宇宙 = st.number_input("模擬宇宙（週分）", min_value=0, value=0)

st.markdown("---")
st.subheader("その他獲得予定")

予定券 = st.number_input("獲得予定チケット（枚）", min_value=0, value=0)
予定石 = st.number_input("獲得予定石（個）", min_value=0, value=0)
星芒 = st.number_input("星芒交換（現在数）", min_value=0, value=0)

メモ = st.text_area("メモ（任意）")

# 計算
if st.button("決定！"):
    入手石 = 0
    if 庭: 入手石 += 800
    if 女児: 入手石 += 800
    if 末日: 入手石 += 800
    入手石 += 月パス * 90 + デイリー * 60 + 模擬宇宙 * 225 + 予定石

    result1 = (current_石 + 入手石) // 160 + current_券 + 予定券 + (星芒 // 20)
    result2 = result1 + (result1 // 10)

    st.success(f"✅ 合計：{result1}連")
    st.info(f"✨ 合計（星芒込）：約{result2}連")
