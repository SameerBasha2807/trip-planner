import streamlit as st
from datetime import datetime

# IMPORTANT import
from trip_planner.crew import TripPlanner

st.set_page_config(page_title="AI Trip Planner", layout="wide")

st.title("🌍 AI Trip Planner Dashboard")

# ─────────────────────────────
# SIDEBAR INPUTS
# ─────────────────────────────
with st.sidebar:
    st.header("Trip Details")

    topic = st.text_input("Topic", "AI LLMs")

    run_button = st.button("🚀 Run Crew")

# ─────────────────────────────
# MAIN EXECUTION
# ─────────────────────────────
if run_button:

    inputs = {
        "topic": topic,
        "current_year": str(datetime.now().year)
    }

    with st.spinner("Running AI crew..."):
        result = TripPlanner().crew().kickoff(inputs=inputs)

    # ─────────────────────────────
    # OUTPUT DISPLAY
    # ─────────────────────────────
    st.subheader("📄 Output")
    st.write(result)

    st.success("✅ Execution Complete")