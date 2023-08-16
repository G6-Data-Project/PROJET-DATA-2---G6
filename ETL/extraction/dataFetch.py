import requests
import csv
import os


start_league_id = 1
end_league_id = 450
api_key = "ff59da0b57691fd4b8c7b19768cccbca0f2b1fba43a305c16c6e1071f4ea15f0"

all_teams = []


for league_id in range(start_league_id, end_league_id + 1):
    url = f"https://apiv3.apifootball.com/?action=get_teams&league_id={league_id}&APIkey={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        teams = response.json()
        all_teams.extend(teams)


csv_file_path = os.path.join( "Files" , 'players_test.csv')


if not os.path.exists(csv_file_path):
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = [
            'player_key', 'player_id', 'player_image', 'player_name', 'player_number',
            'player_country', 'player_type', 'player_age', 'player_match_played',
            'player_goals', 'player_yellow_cards', 'player_red_cards',
            'player_injured', 'player_substitute_out', 'player_substitutes_on_bench',
            'player_assists', 'player_is_captain', 'player_shots_total',
            'player_goals_conceded', 'player_fouls_committed', 'player_tackles',
            'player_blocks', 'player_crosses_total', 'player_interceptions',
            'player_clearances', 'player_dispossesed', 'player_saves',
            'player_inside_box_saves', 'player_duels_total', 'player_duels_won',
            'player_dribble_attempts', 'player_dribble_succ', 'player_pen_comm',
            'player_pen_won', 'player_pen_scored', 'player_pen_missed',
            'player_passes', 'player_passes_accuracy', 'player_key_passes',
            'player_woordworks', 'player_rating','player_birthdate'
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()


existing_players = set()
with open(csv_file_path, 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        existing_players.add(row['player_key'])

with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = [
        'player_key', 'player_id', 'player_image', 'player_name', 'player_number',
            'player_country', 'player_type', 'player_age', 'player_match_played',
            'player_goals', 'player_yellow_cards', 'player_red_cards',
            'player_injured', 'player_substitute_out', 'player_substitutes_on_bench',
            'player_assists', 'player_is_captain', 'player_shots_total',
            'player_goals_conceded', 'player_fouls_committed', 'player_tackles',
            'player_blocks', 'player_crosses_total', 'player_interceptions',
            'player_clearances', 'player_dispossesed', 'player_saves',
            'player_inside_box_saves', 'player_duels_total', 'player_duels_won',
            'player_dribble_attempts', 'player_dribble_succ', 'player_pen_comm',
            'player_pen_won', 'player_pen_scored', 'player_pen_missed',
            'player_passes', 'player_passes_accuracy', 'player_key_passes',
            'player_woordworks', 'player_rating','player_birthdate'
    ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for team in all_teams:
        players = team["players"]

        for player in players:
            player_key = player['player_key']
            if player_key not in existing_players:
                player = {k: v if v != "" else 0 for k, v in player.items()}
                writer.writerow(player)
                existing_players.add(player_key)
