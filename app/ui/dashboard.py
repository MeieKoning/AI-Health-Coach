import streamlit as st
from app.data.tracker import Tracker

def show_dashboard():
    st.title("🏋️‍♀️ AI Health Coach Dashboard")
    tracker = Tracker()
    logs = tracker.get_logs()

    st.subheader("📊 Habit Logs")
    for timestamp, entry in logs.items():
        st.markdown(f"- **{timestamp}**: {entry}")

    st.subheader("📈 Summary")
    if logs:
        goals = [v["goal"] for v in logs.values() if "goal" in v]
        st.write(f"Total goals logged: {len(goals)}")
        st.write(f"Most recent goal: {goals[-1]}")

if __name__ == "__main__":
    show_dashboard()