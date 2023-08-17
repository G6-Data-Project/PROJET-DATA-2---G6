import pandas as pd

# Cette fonction calcule la note d'un défenseur en fonction de ses performances et de sa position
def calculate_defender_rating(player_data, position):
    position_coefficients = {
        "Defenders": {
            "tackles_coeff": 4,
            "interceptions_coeff": 5,
            "clearances_coeff": 3,
            "player_duels_won_coeff": 4,
            "passes_accuracy_coeff": 2
        },
        "Defenders": {
            "tackles_coeff": 3,
            "interceptions_coeff": 4,
            "accurate_crosses_coeff": 4,
            "passes_accuracy_coeff": 3,
            "distance_covered_coeff": 2,
            "player_duels_won_coeff": 2
        }
    }

    coefficients = position_coefficients[position]

    raw_rating = (player_data["player_tackles"] * coefficients["tackles_coeff"]) + \
                 (player_data["player_interceptions"] * coefficients["interceptions_coeff"]) + \
                 (player_data.get("player_clearances", 0) * coefficients.get("clearances_coeff", 0)) + \
                 (player_data.get("player_accurate_crosses", 0) * coefficients.get("accurate_crosses_coeff", 0)) + \
                 (player_data["player_passes_accuracy"] * coefficients["passes_accuracy_coeff"]) + \
                 (player_data.get("player_distance_covered", 0) * coefficients.get("distance_covered_coeff", 0)) + \
                 (player_data["player_duels_won"] * coefficients["player_duels_won_coeff"])

    min_raw_rating = sum([0] + [0 for coeff in coefficients.values() if coeff != 0])
    max_raw_rating = sum([100 * coeff for coeff in coefficients.values() if coeff != 0])

    normalized_rating = (raw_rating - min_raw_rating) / (max_raw_rating - min_raw_rating) * 9 + 1

    if normalized_rating > 10:
        return 10
    else:
        return normalized_rating

# Charger le fichier CSV dans un DataFrame
df = pd.read_csv('players_1_to_500.csv')

# Filtrer les défenseurs selon les critères
filtered_defenders = df[
    (df['player_age'] >= 16) & (df['player_age'] <= 22) &
    (df['player_type'] == 'Defenders') &
    (df['player_match_played'] > 0)
]

# Vérifier si des données existent après le filtrage
if not filtered_defenders.empty:
    # Calculer les notations pour chaque défenseur en utilisant une boucle
    defender_ratings = []
    for index, row in filtered_defenders.iterrows():
        defender_rating = calculate_defender_rating(row, row['player_type'])
        defender_ratings.append(defender_rating)
    
    # Ajouter les notations calculées dans une nouvelle colonne 'defender_rating'
    filtered_defenders['defender_rating'] = defender_ratings
    
    # Calculer le ratio pour chaque défenseur
    filtered_defenders['ratio'] = filtered_defenders['player_tackles'] / filtered_defenders['player_match_played']
    
    # Supposons que vous ayez une colonne 'player_rating' contenant les notations de la fédération
    # Calculer la note finale en multipliant la notation que vous attribuez par la notation de la fédération
    filtered_defenders['final_rating'] = filtered_defenders['defender_rating'] + filtered_defenders['player_rating'] / 2
    
    # Trier les défenseurs par note finale décroissante
    sorted_defenders = filtered_defenders.sort_values(by='final_rating', ascending=False)
    top_5_players = sorted_defenders.head(5)
    
    # Afficher les défenseurs triés avec leurs noms, âges, types, tackles, matchs joués, notations et ratios
    selected_columns = ['player_name', 'player_age', 'player_type', 'player_tackles', 'player_match_played', 'defender_rating', 'player_rating', 'final_rating', 'ratio']
    print(top_5_players[selected_columns])
    
    # Exporter les statistiques des défenseurs dans un fichier CSV
    file_name = 'top_defenders_stats.csv'
    top_5_players[selected_columns].to_csv(file_name, index=False)
else:
    print("Aucun défenseur ne satisfait les critères de filtrage.")
