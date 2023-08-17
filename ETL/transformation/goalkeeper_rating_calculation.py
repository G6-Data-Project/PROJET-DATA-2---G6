import pandas as pd

# Cette fonction calcule la note d'un gardien de but en fonction de ses performances
def calculate_goalkeeper_rating(player_data):
    position_coefficients = {
        "saves_coeff": 4,
        "save_percentage_coeff": 3,
        "clean_sheets_coeff": 5,
        "aerial_duels_won_coeff": 2,
        "passes_success_coeff": 2
    }

    coefficients = position_coefficients

    raw_rating = 0
    for stat, coeff in coefficients.items():
        if stat in player_data:
            raw_rating += player_data[stat] * coeff

    min_raw_rating = sum([0] + [0 for coeff in coefficients.values() if coeff != 0])
    max_raw_rating = sum([100 * coeff for coeff in coefficients.values() if coeff != 0])

    normalized_rating = (raw_rating - min_raw_rating) / (max_raw_rating - min_raw_rating) * 9 + 1

    if normalized_rating > 10:
        return 10
    else:
        return normalized_rating

# Charger le fichier CSV dans un DataFrame
df = pd.read_csv('votre_fichier.csv')

# Filtrer les gardiens de but selon les critères
filtered_goalkeepers = df[
    (df['player_age'] >= 16) & (df['player_age'] <= 22) &
    (df['player_type'] == 'Goalkeeper') &
    (df['player_match_played'] > 0)
]

# Vérifier si des données existent après le filtrage
if not filtered_goalkeepers.empty:
    # Calculer les notations pour chaque gardien de but en utilisant une boucle
    goalkeeper_ratings = []
    for index, row in filtered_goalkeepers.iterrows():
        goalkeeper_data = {
            "saves": row['player_saves'],
            "save_percentage": row['player_save_percentage'],
            "clean_sheets": row['player_clean_sheets'],
            "aerial_duels_won": row['player_aerial_duels_won'],
            "passes_success": row['player_passes_success']
        }
        goalkeeper_rating = calculate_goalkeeper_rating(goalkeeper_data)
        goalkeeper_ratings.append(goalkeeper_rating)
    
    # Ajouter les notations calculées dans une nouvelle colonne 'goalkeeper_rating'
    filtered_goalkeepers['goalkeeper_rating'] = goalkeeper_ratings
    
    # Supposons que vous ayez une colonne 'player_rating' contenant les notations de la fédération
    # Calculer la note finale en multipliant la notation que vous attribuez par la notation de la fédération
    filtered_goalkeepers['final_rating'] = filtered_goalkeepers['goalkeeper_rating'] + filtered_goalkeepers['player_rating'] / 2
    
    # Trier les gardiens de but par note finale décroissante
    sorted_goalkeepers = filtered_goalkeepers.sort_values(by='final_rating', ascending=False)
    top_5_players = sorted_goalkeepers.head(5)
    
    # Afficher les gardiens de but triés avec leurs noms, âges, types, saves, matchs joués, notations et ratios
    selected_columns = ['player_name', 'player_age', 'player_type', 'player_saves', 'player_match_played', 'goalkeeper_rating', 'player_rating', 'final_rating']
    print(top_5_players[selected_columns])
    
    # Exporter les statistiques des gardiens de but dans un fichier CSV
    file_name = 'top_goalkeepers_stats.csv'
    top_5_players[selected_columns].to_csv(file_name, index=False)
else:
    print("Aucun gardien de but ne satisfait les critères de filtrage.")
