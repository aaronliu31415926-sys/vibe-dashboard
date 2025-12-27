import streamlit as st
import time
from datetime import date

# 基本設定
st.set_page_config(page_title="番茄鐘 25 分", page_icon="🍅", layout="centered")
st.title("🍅 番茄鐘（25 分）")
st.caption("開始 → 倒數 25:00；可暫停或重置。")
 
# 狀態初始化
DEFAULT_SECONDS = 25 * 60  # 25 分鐘
if "remaining" not in st.session_state:
    st.session_state.remaining = DEFAULT_SECONDS
if "running" not in st.session_state:
    st.session_state.running = False
if "last_tick" not in st.session_state:
    st.session_state.last_tick = time.time()
 
# 控制按鈕
c1, c2, c3 = st.columns(3)
with c1:
    if st.button("▶️ 開始", use_container_width=True):
        st.session_state.running = True
    elapsed = int(now - st.session_state.last_tick)        st.session_state.last_tick = time.time()
    if elapsed >= 1:
        st.session_state.remaining = max(0, st.session_state.remaining - elapsed)
        st.session_state.last_tick = now
 
# 顯示 mm:ss
minutes = st.session_state.remaining // 60
seconds = st.session_state.remaining % 60
st.markdown(
    f"""
    <div style="font-size:80px; font-weight:700; text-align:center;">
        {minutes:02d}:{seconds:02d}
    </div>
    """,
    unsafe_allow_html=True
)
 
# 完成提示
if st.session_state.remaining == 0:
    st.success("⏰ 時間到！辛苦了，休息一下吧～")
 
# 自動刷新
if st.session_state.running and st.session_state.remaining > 0:
    st.experimental_rerun()
``
with c2:
    if st.button("⏸️ 暫停", use_container_width=True):
        st.session_state.running = False
with c3:
    if st.button("🔄 重置", use_container_width=True):
        st.session_state.running = False
        st.session_state.remaining = DEFAULT_SECONDS
 
# 計時邏輯
if st.session_state.running and st.session_state.remaining > 0:
    now = time.time()