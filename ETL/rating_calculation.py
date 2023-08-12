import numpy as np
from numpy.linalg import inv

# Exemple de données fictives sous forme de dictionnaire
players_data = [
    {
        "player_type": "AC",
        "player_goals": 10,
        "player_shots_total": 50,
        "player_passes_accuracy": 0.85,
        "league_rating": 8.2
    },
    # ... autres joueurs
]

# Liste de statistiques que vous voulez inclure dans la matrice X
selected_stats = ["player_goals", "player_shots_total"]

# Initialisation de la matrice X et du vecteur y
X = []
y = []

for player in players_data:
    player_stats = [player[stat] for stat in selected_stats]
    X.append(player_stats)
    y.append(player["league_rating"])

# Convertissez les listes en tableaux NumPy
X = np.array(X)
y = np.array(y)

# Calcul des coefficients à l'aide de la méthode des moindres carrés
X_transpose = np.transpose(X)
coefficients = np.dot(np.dot(inv(np.dot(X_transpose, X)), X_transpose), y)

print("Coefficients:", coefficients)

# Ajustez les coefficients pour donner plus de poids aux buts et tirs
adjusted_coefficients = coefficients.copy()
adjusted_coefficients[0] *= 2  # Exemple : double le coefficient pour les buts
adjusted_coefficients[1] *= 1.5  # Exemple : augmente le coefficient pour les tirs

print("Adjusted Coefficients:", adjusted_coefficients)

# Calcul des notes pour chaque joueur en utilisant les coefficients ajustés
for player in players_data:
    player_stats = np.array([player[stat] for stat in selected_stats])
    predicted_note = np.dot(adjusted_coefficients, player_stats)
    
    # Applique une transformation logistique pour éviter les valeurs négatives
    predicted_note = 1 / (1 + np.exp(-predicted_note))
    
    # Applique une transformation linéaire pour ramener la note dans l'intervalle [1, 10]
    predicted_note = 1 + (predicted_note * 9)
    
    # Limite la note entre 1 et 10, avec une correction pour s'assurer que cela reste dans l'intervalle
    predicted_note = max(1, min(10, predicted_note))
    
    player["predicted_note"] = predicted_note

print(players_data)
