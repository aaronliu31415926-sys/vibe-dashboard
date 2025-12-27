import streamlit as st
import time
#基本設定（無 icon）
st.set_page_config(page_title="番茄鐘 25 分", layout="centered")
st.title("番茄鐘（25 分）")
st.caption("開始 → 倒數 25:00；可暫停或重置。")
YT = "https://www.youtube.com/embed?listType=playlist&list=OLAK5uy_kZnXbea4f7XrKfUq1Ibwa11JrqFa7BfJU"
#狀態初始化
DEFAULT_SECONDS = 25 * 60
if "remaining" not in st.session_state:
    st.session_state.remaining = DEFAULT_SECONDS
if "running" not in st.session_state:
    st.session_state.running = False
if "last_tick" not in st.session_state:
    st.session_state.last_tick = time.time()
#控制按鈕
c1, c2, c3 = st.columns(3)
with c1:
    if st.button("開始", use_container_width=True):
        st.session_state.running = True
        st.session_state.last_tick = time.time()
with c2:
    if st.button("暫停", use_container_width=True):
        st.session_state.running = False
with c3:
    if st.button("重置", use_container_width=True):
        st.session_state.running = False
        st.session_state.remaining = DEFAULT_SECONDS
#計時邏輯
if st.session_state.running and st.session_state.remaining > 0:
    now = time.time()
    elapsed = int(now - st.session_state.last_tick)
    if elapsed >= 1:
        st.session_state.remaining = max(0, st.session_state.remaining - elapsed)
        st.session_state.last_tick = now
if st.session_state.running and st.session_state.remaining > 0: st.sidebar.video(YT, autoplay=True, muted=False)
#顯示 mm:ss
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
#完成提示
if st.session_state.remaining == 0:
    st.success("時間到！休息一下吧～")
#自動刷新
if st.session_state.running and st.session_state.remaining > 0: time.sleep(1); st.rerun()