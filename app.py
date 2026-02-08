# app.py
import streamlit as st

# Read data
with open("data.txt", "r") as file:
    text = file.read().lower()

words = text.split()

# Train logic
next_word = {}
for i in range(len(words) - 1):
    current = words[i]
    nxt = words[i + 1]

    if current not in next_word:
        next_word[current] = {}

    if nxt not in next_word[current]:
        next_word[current][nxt] = 1
    else:
        next_word[current][nxt] += 1


# UI
st.title("🧠 Next Word Predictor")
st.write("Enter a word and I will predict the next word!")

user_input = st.text_input("Enter a word:")

if st.button("Predict"):
    if user_input.lower() in next_word:
        prediction = max(next_word[user_input.lower()],
                         key=next_word[user_input.lower()].get)
        st.success(f"Predicted next word: **{prediction}**")
    else:
        st.error("Sorry, I don't know what comes next ")
