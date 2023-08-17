import pandas as pd
import numpy as np

# Cette fonction calcule la note d'un milieu de terrain en fonction de ses performances
def calculate_midfielder_rating(player_data):
    position_coefficients = {
        "player_key_passes": 3,
        "player_passes_accuracy": 2,
        "player_passes": 0.1,
        "player_assists": 2
    }

    key_passes_coeff = position_coefficients["player_key_passes"]
    passes_accuracy_coeff = position_coefficients["player_passes_accuracy"]
    passes_coeff = position_coefficients["player_passes"]
    assists_coeff = position_coefficients["player_assists"]

    raw_rating = (player_data["player_key_passes"] * key_passes_coeff) + \
                 (player_data["player_passes_accuracy"] * passes_accuracy_coeff) + \
                 (player_data["player_passes"] * passes_coeff) + \
                 (player_data["player_assists"] * assists_coeff) / \
                 (key_passes_coeff + passes_accuracy_coeff + passes_coeff + assists_coeff)
    
    min_raw_rating = (0 * key_passes_coeff) + \
                     (0 * passes_accuracy_coeff) + \
                     (0 * passes_coeff) + \
                     (0 * assists_coeff)
    
    max_raw_rating = (100 * key_passes_coeff) + \
                     (1 * passes_accuracy_coeff) + \
                     (100 * passes_coeff) + \
                     (100 * assists_coeff)
    
    normalized_rating = (raw_rating - min_raw_rating) / (max_raw_rating - min_raw_rating) * 9 + 1
    if normalized_rating > 10:
        return 10
    else:
        return normalized_rating

# Charger le fichier CSV dans un DataFrame
df = pd.read_csv('players_1_to_500.csv')

# Filtrer les milieux de terrain selon les critères
filtered_midfielders = df[
    (df['player_age'] >= 16) & (df['player_age'] <= 22) &
    (df['player_type'] == 'Midfielders') &
    (df['player_assists'] > 0)
]

# Vérifier si des données existent après le filtrage
if not filtered_midfielders.empty:
    # Calculer les notations pour chaque milieu de terrain en utilisant une boucle
    midfielder_ratings = []
    for index, row in filtered_midfielders.iterrows():
        midfielder_rating = calculate_midfielder_rating(row)
        midfielder_ratings.append(midfielder_rating)
    
    # Ajouter les notations calculées dans une nouvelle colonne 'midfielder_rating'
    filtered_midfielders['midfielder_rating'] = midfielder_ratings
    
    filtered_midfielders['ratio'] = filtered_forwards['player_assists'] / filtered_forwards['player_match_played']
    
    # Supposons que vous ayez une colonne 'player_rating' contenant les notations de la fédération
    # Calculer la note finale en multipliant la notation que vous attribuez par la notation de la fédération
    filtered_midfielders['final_rating'] = filtered_midfielders['midfielder_rating'] + filtered_midfielders['player_rating'] / 2
    
    # Trier les milieux de terrain par note décroissante
    sorted_midfielders = filtered_midfielders.sort_values(by='midfielder_rating', ascending=False)
    
    # Sélectionner les colonnes pertinentes pour l'exportation
    selected_columns = ['player_name', 'player_image', 'player_country', 'player_age', 'player_type', 'player_assists', 'player_match_played', 'midfielder_rating' , 'player_rating', 'ratio', 'final_rating']
    
    # Afficher les 5 meilleurs milieux de terrain
    top_5_midfielders = sorted_midfielders.head(5)
    print(top_5_midfielders[selected_columns])
    
    # Exporter les statistiques des 5 meilleurs milieux de terrain dans un fichier CSV
    top_5_midfielders[selected_columns].to_csv('top_5_mid_stats.csv', index=False)
else:
    print("Aucun milieu de terrain ne satisfait les critères de filtrage.")
