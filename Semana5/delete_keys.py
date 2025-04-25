soccer_teams = {
    "Real Madrid": "Spain",
    "All Nassar": "Saudit Arab",
    "Chelsea": "England",
    "Boca Juniors" : "Argentina",
    "Inter Miami": "USA",
}

remove_keys = ["Boca Juniors", "Inter Miami"]

for key in remove_keys:
    if key in soccer_teams:
        soccer_teams.pop(key)

print ( soccer_teams)