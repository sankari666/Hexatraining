#Capstone Project-2
#1
with open('players.csv', 'r') as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)

#2
for row in reader:
    print(row)

#3
count=0
for row in reader:
        count += 1
print(count)

#4
highest_player = ""
highest_runs = 0
for row in reader:
        runs = int(row['Runs'])
        if runs > highest_runs:
            highest_runs = runs
            highest_player = row['Player']
print(highest_player)
print(highest_runs)

#5
lowest_player = ""
lowest_runs = float('inf')
 for row in reader:
        runs = int(row['Runs'])
        if runs < lowest_runs:
            lowest_runs = runs
            lowest_player = row['Player']
print(lowest_player)
print(lowest_runs)

#6
total_runs = 0
total_players = 0
for row in reader:
        total_runs += int(row['Runs'])
        total_players += 1
average_runs = total_runs / total_players
print(average_runs)

#7
for row in reader:
        if int(row['Runs']) > 600:
            print(row['Player'], "-", row['Runs'])

#8
for row in reader:
        if int(row['Runs']) < 500:
            print(row['Player'], "-", row['Runs'])

#9
team_count = {}
for row in reader:
        team = row['Team']
        team_count[team] = team_count.get(team, 0) + 1
print(team_count)

#10
team_runs = {}
for row in reader:
        team = row['Team']
        runs = int(row['Runs'])
        team_runs[team] = team_runs.get(team, 0) + runs
print(team_runs)

#11
team_runs = {}
for row in reader:
        team = row['Team']
        runs = int(row['Runs'])
        team_runs[team] = team_runs.get(team, 0) + runs
top_team = max(team_runs, key=team_runs.get)
print(top_team)
print(team_runs[top_team])

#12
team_runs = {}
for row in reader:
        team = row['Team']
        runs = int(row['Runs'])
        team_runs[team] = team_runs.get(team, 0) + runs
low_team = min(team_runs, key=team_runs.get)
print(low_team)
print(team_runs[low_team])

#13
max_fours = 0
player_name = ""
for row in reader:
        fours = int(row['Fours'])
        if fours > max_fours:
            max_fours = fours
            player_name = row['Player']
print(player_name)
print(max_fours)

#14
max_sixes = 0
player_name = ""
for row in reader:
        sixes = int(row['Sixes'])
        if sixes > max_sixes:
            max_sixes = sixes
            player_name = row['Player']
print(player_name)
print(max_sixes)

#15
total_fours = 0
for row in reader:
        total_fours += int(row['Fours'])
print(total_fours)

#16
total_sixes = 0
for row in reader:
        total_sixes += int(row['Sixes'])
print(total_sixes)

#17
players = []
for row in reader:
        players.append(row['Player'])
players.sort()
for player in players:
    print(player)

#18
teams = set()
for row in reader:
        teams.add(row['Team'])

for team in teams:
    print(team)

#19
team_runs = {}
for row in reader:
        team = row['Team']
        runs = int(row['Runs'])
        team_runs[team] = team_runs.get(team, 0) + runs
print(team_runs)

#20
player_runs = {}
for row in reader:
        player_runs[row['Player']] = int(row['Runs'])

print(player_runs)

#21
def find_top_scorer(filename):
    top_player = ""
    highest_runs = 0
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            runs = int(row['Runs'])
            if runs > highest_runs:
                highest_runs = runs
                top_player = row['Player']
    return top_player, highest_runs
print(find_top_scorer("players.csv"))

#22
def calculate_average_runs(filename):
    total_runs = 0
    player_count = 0
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            total_runs += int(row['Runs'])
            player_count += 1
    return total_runs / player_count
print(calculate_average_runs("players.csv"))

#23
def find_best_team(filename):
    team_runs = {}
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            team = row['Team']
            runs = int(row['Runs'])
            team_runs[team] = team_runs.get(team, 0) + runs
    best_team = max(team_runs, key=team_runs.get)
    return best_team, team_runs[best_team]
print(find_best_team("players.csv"))

#24
def find_total_boundaries(filename):
    total_boundaries = 0
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            total_boundaries += (
                int(row['Fours']) +
                int(row['Sixes'])
            )
    return total_boundaries
print(find_total_boundaries("players.csv"))

#25
try:
    with open('players.csv', 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            print(row)

except FileNotFoundError:
    print("Error: players.csv file not found.")

#26
for row in reader:
        try:
            runs = int(row['Runs'])
            print(runs)

        except ValueError:
            print("Invalid Runs:", row['Runs'])

#27
for row in reader:
        try:
            matches = int(row['Matches'])
            print(matches)

        except ValueError:
            print("Invalid Match Count:", row['Matches'])

#28
df = pd.read_csv("players.csv")
runs = np.array(df["Runs"])

#29
df = pd.read_csv("players.csv")
runs = np.array(df["Runs"])
print("Total Runs:", np.sum(runs))
print("Average Runs:", np.mean(runs))
print("Maximum Runs:", np.max(runs))
print("Minimum Runs:", np.min(runs))
print("Standard Deviation:", np.std(runs))
print("Median:", np.median(runs))

#30
df = pd.read_csv("players.csv")

print(df.head())

#31
df = pd.read_csv("players.csv")
top5 = df.sort_values(
    by="Runs",
    ascending=False
).head(5)
print(top5)

#32
df = pd.read_csv("players.csv")

sorted_players = df.sort_values(
    by="Runs",
    ascending=False
)

print(sorted_players)

#33
df = pd.read_csv("players.csv")

team_runs = df.groupby("Team")["Runs"].sum()

print(team_runs)

#34
df = pd.read_csv("players.csv")

team_avg_runs = df.groupby("Team")["Runs"].mean()

print(team_avg_runs)

#35
df = pd.read_csv("players.csv")

players_600 = df[df["Runs"] > 600]

print(players_600)

#36
df = pd.read_csv("players.csv")

team_runs = df.groupby("Team")["Runs"].sum()

top_team = team_runs.idxmax()

print("Top Team:", top_team)
print("Runs:", team_runs.max())

#37
df = pd.read_csv("players.csv")

top_players = df[df["Runs"] > 600]

top_players.to_csv(
    "top_players.csv",
    index=False
)

print("top_players.csv created")

#38
df = pd.read_csv("players.csv")

team_summary = df.groupby("Team").agg(
    Total_Runs=("Runs", "sum"),
    Average_Runs=("Runs", "mean"),
    Player_Count=("Player", "count")
)

team_summary.reset_index().to_csv(
    "team_summary.csv",
    index=False
)

print("team_summary.csv created")

#39
df = pd.read_csv("players.csv")

while True:
    print("1. Player Analysis")
    print("2. Team Analysis")
    print("3. Boundary Analysis")
    print("4. Export Reports")
    print("5. Exit")
    choice = input("Enter Choice: ")
    if choice == "1":
        print(
            df.sort_values(
                by="Runs",
                ascending=False
            )[["Player", "Runs"]]
        )
    elif choice == "2":
        print(
            df.groupby("Team")["Runs"].sum()
        )
    elif choice == "3":
        print(
            "Total Fours:",
            df["Fours"].sum()
        )
        print(
            "Total Sixes:",
            df["Sixes"].sum()
        )
    elif choice == "4":
        team_summary = df.groupby("Team").agg(
            Total_Runs=("Runs", "sum"),
            Average_Runs=("Runs", "mean"),
            Player_Count=("Player", "count")
        )
        team_summary.reset_index().to_csv(
            "team_summary.csv",
            index=False
        )
        print("Reports Exported")
    elif choice == "5":
        print("Thank You")
        break
    else:
        print("Invalid Choice")
