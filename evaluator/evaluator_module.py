# evaluator_module.py
def evaluate_itinerary(itinerary, user_input):
    """
    Evaluates itinerary for budget and time conflicts.
    Returns final itinerary and budget status.
    """
    total_budget = user_input.get("budget", 0)
    # Mock cost: assume 200 per day
    estimated_cost = len(itinerary) * 200
    budget_ok = estimated_cost <= total_budget

    # Mock time conflict check
    conflicts = False

    return {
        "itinerary": itinerary,
        "budget_ok": budget_ok,
        "conflicts": conflicts,
        "estimated_cost": estimated_cost
    }
