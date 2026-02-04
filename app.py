import streamlit as st
import json

from planner.planner_module import generate_itinerary
from worker.worker_module import enrich_itinerary
from evaluator.evaluator_module import evaluate_itinerary

# --- Load user data safely ---
try:
    with open("data/trips.json", "r", encoding="utf-8") as f:
        data = json.load(f)
except FileNotFoundError:
    st.warning("trips.json not found. Using default user preferences.")
    data = {}
except json.JSONDecodeError:
    st.warning("trips.json is empty or invalid. Using default user preferences.")
    data = {}

# Default user preferences
default_user_input = {
    "destination": "Paris",
    "days": 2,
    "budget": 500,
    "travel_style": "economy",
    "food_preferences": ["vegetarian"]
}

user_input = data.get("user_preferences", default_user_input)

# --- Streamlit UI ---
st.title("🌍 Travel Concierge Agent")

st.subheader("Enter Your Travel Preferences")
destination = st.text_input("Destination", user_input.get("destination", "Paris"))
days = st.number_input("Number of Days", min_value=1, max_value=30, value=user_input.get("days", 2))
budget = st.number_input("Budget ($)", min_value=0, value=user_input.get("budget", 500))
travel_style = st.selectbox("Travel Style", ["economy", "luxury", "adventure", "relaxed"], index=0)

if st.button("Generate Itinerary"):
    # Update user input
    user_input.update({
        "destination": destination,
        "days": days,
        "budget": budget,
        "travel_style": travel_style
    })

    # --- Multi-Agent Workflow ---
    itinerary = generate_itinerary(user_input)
    itinerary = enrich_itinerary(itinerary, user_input)
    result = evaluate_itinerary(itinerary, user_input)

    # --- Display Results ---
    st.subheader("📝 Final Itinerary")
    for day, activities in result["itinerary"].items():
        st.markdown(f"**{day}:**")
        for act in activities:
            st.markdown(f"- {act}")
        st.markdown("---")

    st.write(f"💰 Estimated Cost: ${result['estimated_cost']}")
    st.write(f"✅ Budget OK? {'Yes' if result['budget_ok'] else 'No'}")
    st.write(f"⏱ Conflicts? {'Yes' if result['conflicts'] else 'No'}")
