# this function calculate the forward rating according to his goal, shoot total and match played during one season
def calculate_player_forward_rating(player_data):
    position = player_data["player_type"]
    position_coefficients = coefficients_by_position.get(position, {"goal_coeff": 1, "shot_coeff": 0.1, "match_coeff": 0.5})

    goal_coeff = position_coefficients["goal_coeff"]
    shot_coeff = position_coefficients["shot_coeff"]
    match_coeff = position_coefficients["match_coeff"]

    raw_rating = ((player_data["player_goals"] * goal_coeff) + (player_data["player_shots_total"] * shot_coeff) + (player_data["player_match_played"] * match_coeff)) / (shot_coeff + match_coeff + goal_coeff)
    
    min_raw_rating = (0 * goal_coeff) + (0 * shot_coeff) + (0 * match_coeff)
    max_raw_rating = (10 * goal_coeff) + (100 * shot_coeff) + (90 * match_coeff)

    normalized_rating = (raw_rating - min_raw_rating) / (max_raw_rating - min_raw_rating) * 9 + 1
    
    if normalized_rating > 10:
        return 10
    else:
        return normalized_rating
coefficients_by_position = {
    "AC": {"goal_coeff": 5, "shot_coeff": 0.2, "match_coeff": 0.5},
}
df = pd.read_csv('players_1_to_500.csv')

# Convertir les colonnes pertinentes en numériques en traitant les valeurs non numériques
df['player_age'] = pd.to_numeric(df['player_age'], errors='coerce')
df['player_goals'] = pd.to_numeric(df['player_goals'], errors='coerce')
df['player_shots_total'] = pd.to_numeric(df['player_shots_total'], errors='coerce')
df['player_match_played'] = pd.to_numeric(df['player_match_played'], errors='coerce')

# Filtrer les attaquants selon les critères
filtered_forwards = df[
    (df['player_age'] >= 16) & (df['player_age'] <= 22) &
    (df['player_type'] == 'Forwards') &
    (df['player_goals'] > 0) &
    (df['player_match_played'] > 0)
]

# Vérifier si des données existent après le filtrage
if not filtered_forwards.empty:
    # Calculer les notations pour chaque attaquant en utilisant une boucle
    forward_ratings = []
    for index, row in filtered_forwards.iterrows():
        forward_rating = calculate_player_forward_rating(row)
        forward_ratings.append(forward_rating)
    
    # Ajouter les notations calculées dans une nouvelle colonne 'forward_rating'
    filtered_forwards['forward_rating'] = forward_ratings
    
    # Calculer le ratio pour chaque attaquant
    filtered_forwards['ratio'] = filtered_forwards['player_goals'] / filtered_forwards['player_match_played']
    
    # Supposons que vous ayez une colonne 'player_rating' contenant les notations de la fédération
    # Calculer la note finale en multipliant la notation que vous attribuez par la notation de la fédération
    filtered_forwards['final_rating'] = filtered_forwards['forward_rating'] + filtered_forwards['player_rating'] / 2
    
    # Trier les attaquants par note finale décroissante
    sorted_forwards = filtered_forwards.sort_values(by='final_rating', ascending=False)
    top_5_players = sorted_forwards.head(5)
    
    # Imprimer les attaquants triés avec leurs noms, âges, types, buts, matchs joués, notations et ratios
    print(top_5_players[['player_name', 'player_age', 'player_type', 'player_goals', 'player_match_played', 'forward_rating', 'player_rating', 'final_rating', 'ratio']])
    selected_column = ['player_name', 'player_image','player_country', 'player_age', 'player_type', 'player_goals', 'player_shots_total', 'player_match_played', 'forward_rating', 'player_rating', 'final_rating', 'ratio']
    top_5_players[selected_column].to_csv('top_5_forwards_stats.csv', index=False)

else:
    print("Aucun attaquant ne satisfait les critères de filtrage.")
