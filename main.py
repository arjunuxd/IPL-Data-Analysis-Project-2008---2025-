import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("IPL.csv", low_memory=False)

toss_wins = data['toss_winner'].value_counts().head(10)

print(toss_wins)

plt.figure(figsize=(12,6))

toss_wins.plot(kind='bar')

plt.title("Top Toss Winning Teams", fontsize=16)
plt.xlabel("Teams", fontsize=12)
plt.ylabel("Toss Wins", fontsize=12)

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("assets/toss_winners.png")

plt.show()