import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("IPL.csv", low_memory=False)

# Group runs by batter
top_batsmen = data.groupby('batter')['runs_batter'].sum()

# Sort and get top 10
top_batsmen = top_batsmen.sort_values(ascending=False).head(10)

# Create figure
plt.figure(figsize=(14,7))

# Create bars
bars = plt.bar(top_batsmen.index, top_batsmen.values)

# Title and labels
plt.title("Top 10 IPL Run Scorers (2008 - 2025)", fontsize=18, fontweight='bold')
plt.xlabel("Players", fontsize=13)
plt.ylabel("Total Runs", fontsize=13)

# Rotate names
plt.xticks(rotation=30, ha='right')

# Add values above bars
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,
        height + 100,
        str(int(height)),
        ha='center',
        fontsize=10
    )

# Grid
plt.grid(axis='y', linestyle='--', alpha=0.4)

# Layout fix
plt.tight_layout()

# Save chart
plt.savefig("assets/top_batsmen_pro.png", dpi=300)

# Show chart
plt.show()