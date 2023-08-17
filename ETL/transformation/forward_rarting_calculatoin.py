import pandas as pd
import numpy as np

# ... (définition de la fonction calculate_player_forward_rating, coefficients_by_position, etc.)

# Charger le fichier CSV dans un DataFrame
df = pd.read_csv('players_1_to_500.csv')

# Convertir les colonnes pertinentes en numériques
# ... (comme dans le code précédent)

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
    
    export_path = '../Files/result/'
    file_name = 'top_5_forwards_stats.csv'
    top_5_players[selected_column].to_csv(export_path + file_name, index=False)

else:
    print("Aucun attaquant ne satisfait les critères de filtrage.")
