import pandas as pd

def load_data():
    try:
        return pd.read_csv("habits.csv")
    except:
        return pd.DataFrame(columns=["habit", "status", "date"])


def save_data(df):
    df.to_csv("habits.csv", index=False)


def calculate_streak(df):
    streak = 0
    statuses = df["status"].tolist()

    for status in reversed(statuses):
        if status == "done":
            streak += 1
        else:
            break

    return streak


def generate_advice(streak, completion_rate):
    if streak >= 5:
        return "🔥 Excellent consistency! Try increasing your goal level."
    elif completion_rate < 0.5:
        return "⚠️ You're missing often. Start with smaller, achievable goals."
    else:
        return "👍 Good progress! Stay consistent and build momentum."