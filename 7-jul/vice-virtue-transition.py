# Vice-Virtue Transition (VVT) Background Job

# AY note 6/29 started as a chat re: self checkins, but maybe for moral code checkins for agents

# Define a dictionary of vice-virtue transitions with a baseline score of 0
VVT_dict = {
    "Impulsiveness": {"Virtue": "Stewardship", "Score": 0},
    "Procrastination": {"Virtue": "Initiative", "Score": 0},
    "Perfectionism": {"Virtue": "Excellence", "Score": 0},
    "Apathy": {"Virtue": "Empathy", "Score": 0},
    "Resentment": {"Virtue": "Forgiveness", "Score": 0},
    "Fear": {"Virtue": "Courage", "Score": 0},
    "Insecurity": {"Virtue": "Confidence", "Score": 0},
    "Intolerance": {"Virtue": "Acceptance", "Score": 0},
    "Greed": {"Virtue": "Generosity", "Score": 0},
    "Complacency": {"Virtue": "Ambition", "Score": 0},
    "Indecisiveness": {"Virtue": "Decisiveness", "Score": 0},
    "Envy": {"Virtue": "Contentment", "Score": 0},
    "Defensiveness": {"Virtue": "Openness", "Score": 0},
    "Disorganization": {"Virtue": "Orderliness", "Score": 0},
    "Impatience": {"Virtue": "Patience", "Score": 0},
    "Laziness": {"Virtue": "Diligence", "Score": 0}
}


def VVT_check_in():
    """
    Function for a regular check-in with VVT commitments. 

    Iterate through each vice-virtue pair, reflect on progress and adjust actions as needed.
    """
    for vice, data in VVT_dict.items():
        print(f"Reflecting on transition from {vice} to {data['Virtue']}.")

        # Reflect on progress
        progress = input("How have I embodied the virtue over the vice in recent times?")

        # Update the score based on the progress
        score_update = input("On a scale of 1-10, how much progress have I made since the last check-in?")
        data['Score'] += int(score_update)

        # Check for a new baseline and adjust if necessary
        if data['Score'] >= 10:
            print("Congratulations on reaching a new milestone!")
            data['Score'] = 0  # Reset the score for the next level of growth

        action_plan = input("What actions can I take to further this transition?")
