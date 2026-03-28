import streamlit as st
import pandas as pd
from datetime import date
from utils import load_data, save_data, calculate_streak, generate_advice

st.set_page_config(page_title="AI Habit Tracker", layout="centered")

st.title("🧠 AI Habit Tracker + Advisor")

# Load data
df = load_data()

# ================= INPUT =================
st.subheader("➕ Add Habit Entry")

habit = st.text_input("Habit Name")
status = st.selectbox("Status", ["done", "missed"])

if st.button("Save"):
    if habit.strip() == "":
        st.warning("Please enter a habit name")
    else:
        new_data = pd.DataFrame([{
            "habit": habit,
            "status": status,
            "date": str(date.today())
        }])

        df = pd.concat([df, new_data], ignore_index=True)
        save_data(df)
        st.success("✅ Habit Saved!")

# ================= ANALYSIS =================
if not df.empty:
    st.subheader("📊 Analysis")

    total = len(df)
    done_count = len(df[df["status"] == "done"])
    completion_rate = done_count / total

    streak = calculate_streak(df)

    st.write(f"🔥 Streak: {streak}")
    st.write(f"📈 Completion Rate: {completion_rate:.2f}")

    # Advice
    advice = generate_advice(streak, completion_rate)

    st.subheader("🤖 AI Advice")
    st.info(advice)

    # Show data
    st.subheader("📋 History")
    st.dataframe(df)