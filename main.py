import streamlit as st # ★ for creating the web interface
import pandas as pd # ✦ for data manipulation
import datetime # ⌛ for handling the dates
import csv # ✎ for reading and writing csv files.
import os # ⚙ for file operation.

# ◆ make a constant variable first
MOOD_FILE = "mood_log.csv"

# ▶ here we will make 2 function, 1 will save the data in mood_log.csv and 2nd will read the data from mood_log.csv file.

# ◉ 1 function for read data.
def load_mood_data(): # ► this function is performing the job to get the data from the file mood_log.csv
    if not os.path.exists(MOOD_FILE): # ◻ here we are using os module path to tell him that if the MOOD_FILE does not exists and not is already build in function
        return pd.DataFrame(columns=["Date", "Mood"]) # ◈ then make 2 colunm in mood_log.csv file
    return pd.read_csv(MOOD_FILE) # ◪ pd.read_csv will help to read the data.

# ◉ 2 function for save the data.
def save_moode_data(date, mood):
    with open(MOOD_FILE, "a") as file: # ◉ with help us to connect with mood_log.csv file & "a" is append means add the data

        writer = csv.writer(file) # ◈ make a vadriable of write and add csv.write to add the row in file.

        writer.writerow([date, mood]) # ◉ writing the mood and date into the file.

# ✦ Mood Tracker App
st.title("✦ 🌈**Mood Tracker** 😊✦")

today = datetime.date.today()

st.subheader("◆ **How are you Feeling today ?**")

# ▶ Mood selection
mood = st.selectbox("◆ **Select your mood**", ["Happy", "Sad", "Angry", "Neutral"])

if st.button("★ **Log Mood**"):

    save_moode_data(today, mood)

    st.success("✔ Mood Logged Successfully! ✦")


data = load_mood_data()
# ◉ this condition is saying that if data is not empty in the file then 
if not data.empty:

    st.subheader("◆ **Mood Trends Over Time**")

    # ◻ Convert date strings to datetime Objects
    data["Date"] = pd.to_datetime(data["Date"])

    # ◉ Count frequency of each mood
    # ◪ mood counts work here for that if user mood on some day same like 2 days happy and 3 days angry 1 day neutral.
    # ◆ .groupby is checking the frequency i.e how many time user moods was same on which days. 
    # ◈ it will provide the detail that in 3 different dates user mood was sad & 2 different dates user mood was happy. it will create the group date wise. 
    mood_counts = data.groupby("Mood").count()["Date"]

    # ◪ Display bar chart of mood frequencies i.e it will show the data in bar chart
    st.bar_chart(mood_counts)

    # ❤ Build with love by Asharib Ali
    st.write("❤️ **Build with love by [Kashif Hanif](https://github.com/KashifHanif628)**")
