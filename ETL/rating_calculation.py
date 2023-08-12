def calculate_player_rating(player_data):
    position = player_data["player_type"]
    position_coefficients = coefficients_by_position.get(position, {"goal_coeff": 1, "shot_coeff": 1, "minute_coeff": 1})

    weighted_sum = sum(coeff * player_data.get(stat, 0) for stat, coeff in position_coefficients.items())
    total_coefficients = sum(position_coefficients.values())
    
    normalized_rating = weighted_sum / total_coefficients
    return normalized_rating

# Coefficients for each position
coefficients_by_position = {
    "AC": {"goal_coeff": 5, "shot_coeff": 0.1, "minute_coeff": 0.001},
    "MID": {"goal_coeff": 3, "shot_coeff": 0.05, "minute_coeff": 0.001},
    "DEF": {"goal_coeff": 1, "shot_coeff": 0.02, "minute_coeff": 0.001},
    # Add more positions and coefficients as needed
}

# Example player data
players_data = [
    {
        "player_type": "DEF",
        "goal_coeff": 5,
        "shot_coeff": 0.1,
        "minute_coeff": 0.001,
        "player_goals": 10,
        "player_shots_total": 50,
        "player_passes_accuracy": 0.85,
        "player_minute_played": 13400,
        "league_rating": 8.2
    },
    # Add more players here
]

# Calculate and print the rating for each player
for player_data in players_data:
    player_rating = calculate_player_rating(player_data)
    print(f"Player Type: {player_data['player_type']}, Player Rating: {player_rating:.2f}")
