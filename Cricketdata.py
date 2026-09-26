import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:\ProjectDA\Super-Market-Sales-Analysis-\ipl_matches.csv")

df.head()

df.shape

df.info()

df.describe()

df.isnull().sum()

df.duplicated().sum()

df["date"] = pd.to_datetime(df["date"])

df["year"] = df["date"].dt.year

df["month"] = df["date"].dt.month_name()

team1_matches = df["team1"].value_counts()

team2_matches = df["team2"].value_counts()

matches_played = team1_matches.add(team2_matches, fill_value=0)

print(matches_played.sort_values(ascending=False))

team_wins = df["winner"].value_counts()

print(team_wins)

win_percentage = (team_wins / matches_played) * 100

print(win_percentage.sort_values(ascending=False))

toss_wins = df["toss_winner"].value_counts()

print(toss_wins)

toss_decisions = df["toss_decision"].value_counts()

print(toss_decisions)

venue_matches = df["venue"].value_counts()

print(venue_matches)

city_matches = df["city"].value_counts()

print(city_matches)

run_wins = df[df["win_by_runs"] > 0]

wicket_wins = df[df["win_by_wickets"] > 0]

print("Wins by Runs:", len(run_wins))

print("Wins by Wickets:", len(wicket_wins))

average_win_runs = np.mean(df["win_by_runs"])

median_win_runs = np.median(df["win_by_runs"])

maximum_win_runs = np.max(df["win_by_runs"])

print("Average Winning Runs:", average_win_runs)

print("Median Winning Runs:", median_win_runs)

print("Maximum Winning Runs:", maximum_win_runs)

team_wins.plot(
    kind="bar",
    figsize=(12, 6)
)

plt.title("IPL Team Wins")

plt.xlabel("Team")

plt.ylabel("Number of Wins")

plt.xticks(rotation=90)

plt.tight_layout()

plt.show()

top_venues = venue_matches.head(10)

top_venues.plot(
    kind="bar",
    figsize=(10, 6)
)

plt.title("Top 10 Venues by Matches")

plt.xlabel("Venue")

plt.ylabel("Number of Matches")

plt.xticks(rotation=75)

plt.tight_layout()

plt.show()

toss_decisions.plot(
    kind="pie",
    autopct="%1.1f%%",
    figsize=(7, 7)
)

plt.title("Toss Decision Distribution")

plt.ylabel("")

plt.show()

run_wins["win_by_runs"].plot(
    kind="hist",
    bins=10,
    figsize=(8, 5)
)

plt.title("Winning Runs Distribution")

plt.xlabel("Winning Runs")

plt.ylabel("Number of Matches")

plt.tight_layout()

plt.show()

win_percentage.sort_values(
    ascending=False
).plot(
    kind="bar",
    figsize=(12, 6)
)

plt.title("Team Win Percentage")

plt.xlabel("Team")

plt.ylabel("Win Percentage")

plt.xticks(rotation=90)

plt.tight_layout()

plt.show()

city_matches.head(10).plot(
    kind="bar",
    figsize=(10, 6)
)

plt.title("Top 10 Cities by Matches")

plt.xlabel("City")

plt.ylabel("Number of Matches")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()

print("Total Matches:", len(df))

print("Total Teams:", len(set(df["team1"]) | set(df["team2"])))

print("Most Successful Team:", team_wins.idxmax())

print("Most Used Venue:", venue_matches.idxmax())

print("Most Common Toss Decision:", toss_decisions.idxmax())

print("Highest Winning Margin:", df["win_by_runs"].max())

print("Average Winning Runs:", round(np.mean(df["win_by_runs"]), 2))

print("Most Successful Team Win Percentage:", round(win_percentage.max(), 2))
