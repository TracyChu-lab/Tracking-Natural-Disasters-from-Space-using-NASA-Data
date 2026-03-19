import streamlit as st

st.title("Wildfire Insights Quiz")

score = 0

q1 = st.radio(
    "Which state had the highest average wildfire magnitude in EONET?",
    ["California", "Nebraska", "Oregon", "Montana"],
    key="q1"
)

if st.button("Check Answer for Q1"):
    if q1 == "Nebraska":
        st.success("Correct! Nebraska had the highest average burned area in the EONET state analysis.")
    else:
        st.error("Not quite. The correct answer is Nebraska.")

q2 = st.radio(
    "Did wildfire detections occur more often during the day or at night in FIRMS?",
    ["Daytime", "Nighttime"],
    key="q2"
)

if st.button("Check Answer for Q2"):
    if q2 == "Daytime":
        st.success("Correct! Around 83% of detections were during the daytime.")
    else:
        st.error("Not quite. The correct answer is Daytime.")

q3 = st.radio(
    "Which relationship was stronger in your analysis?",
    ["Temperature vs Fire Count", "Temperature vs FRP"],
    key="q3"
)

if st.button("Check Answer for Q3"):
    if q3 == "Temperature vs FRP":
        st.success("Correct! Temperature had a stronger correlation with FRP than with fire count.")
    else:
        st.error("Not quite. Temperature vs FRP was stronger.")