# planner_module.py
def generate_itinerary(user_input):
    """
    Generates a basic itinerary based on user input.
    Returns a dictionary with day-wise activities.
    """
    days = user_input.get("days", 2)
    itinerary = {}
    for day in range(1, days + 1):
        itinerary[f"Day {day}"] = [
            f"Visit main attractions in {user_input.get('destination', 'Paris')}",
            "Lunch at local cafe",
            "Evening walk / sightseeing"
        ]
    return itinerary
