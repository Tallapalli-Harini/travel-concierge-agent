# worker_module.py
def enrich_itinerary(itinerary, user_input):
    """
    Enriches itinerary with transport, stay, and dining suggestions.
    """
    for day, activities in itinerary.items():
        activities.append("Hotel check-in")
        activities.append("Dinner at recommended restaurant")
        activities.append("Transport to next location if needed")
    return itinerary
