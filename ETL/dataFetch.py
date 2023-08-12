import requests
import csv

start_league_id = 1
end_league_id = 5
apy_key = "ff59da0b57691fd4b8c7b19768cccbca0f2b1fba43a305c16c6e1071f4ea15f0"

all_teams = []

for league_id in range(start_league_id, end_league_id + 1):
    url = f"https://apiv3.apifootball.com/?action=get_teams&league_id={league_id}&APIkey={apy_key}"
    response = requests.get(url)

    if response.status_code == 200:
        teams = response.json()

    with open('players.csv', 'w', newline='', encoding='utf-8') as csvfile:
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


        for team in teams:
            players = team["players"]

            for player in players:
                player = {k: v if v != "" else "Indisponible" for k, v in player.items()}
                writer.writerow(player)
