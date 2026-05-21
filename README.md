# 🏏 IPL Data Analysis Project

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge\&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-black?style=for-the-badge\&logo=pandas)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Project-Completed-success?style=for-the-badge)

---

# 📌 Project Overview

The **IPL Data Analysis Project** is a beginner-friendly sports analytics project developed using Python. The project focuses on analyzing Indian Premier League (IPL) cricket data to uncover meaningful insights related to:

* Team performances
* Match-winning trends
* Top batsmen
* Top bowlers
* Toss analysis
* Data visualization

This project was created as part of a self-learning journey toward becoming a **Data Analyst**.

---

# 🎯 Objectives

The main objectives of this project are:

* Learn real-world data analysis workflow
* Understand how CSV datasets are analyzed using Python
* Perform sports data analytics
* Create meaningful visualizations
* Build a beginner-level portfolio project
* Practice data grouping, sorting, and aggregation

---

# 🛠 Technologies Used

| Technology  | Purpose                      |
| ----------- | ---------------------------- |
| Python      | Programming Language         |
| Pandas      | Data Analysis & Manipulation |
| Matplotlib  | Data Visualization           |
| CSV Dataset | IPL Cricket Data             |
| VS Code     | Development Environment      |

---

# 📂 Project Structure

```text
IPL_Project/
│
├── assets/
│   ├── top_teams.png
│   ├── top_batsmen.png
│   ├── top_bowlers.png
│   └── toss_winners.png
│
├── IPL.csv
├── main.py
└── README.md
```

---

# 📥 Dataset Information

The dataset used in this project contains detailed IPL match information including:

* Match details
* Teams
* Players
* Runs scored
* Wickets taken
* Toss results
* Venues
* Match winners
* Ball-by-ball analysis

Dataset File:

```text
IPL.csv
```

---

# ⚙️ Installation & Setup

## Step 1 — Install Python

Download Python:

```text
https://www.python.org/downloads/
```

---

## Step 2 — Install Required Libraries

Run the following commands in terminal:

```bash
pip install pandas
pip install matplotlib
```

---

# 🚀 Loading Dataset

## Code Used

```python
import pandas as pd

data = pd.read_csv("IPL.csv", low_memory=False)

print(data.head())
```

## Explanation

* `pandas` is used for data analysis.
* `read_csv()` loads the dataset.
* `head()` displays the first 5 rows.

---

# 📊 Analysis 1 — Most Successful IPL Teams

## Objective

Analyze which IPL teams have won the most matches.

---

## Code Used

```python
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("IPL.csv", low_memory=False)

wins = data['match_won_by'].value_counts().head(10)

wins.plot(kind='bar')

plt.title("Top IPL Teams")
plt.xlabel("Teams")
plt.ylabel("Wins")

plt.savefig("assets/top_teams.png")

plt.show()
```

---

## Concepts Learned

| Concept        | Description            |
| -------------- | ---------------------- |
| value_counts() | Counts repeated values |
| plot()         | Creates graph          |
| savefig()      | Saves chart as image   |
| title()        | Adds chart title       |

---

## Output

* Bar chart showing top IPL teams by match wins.
* Saved image inside assets folder.

---

# 🏏 Analysis 2 — Top IPL Run Scorers

## Objective

Find the highest run scorers in IPL history.

---

## Code Used

```python
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("IPL.csv", low_memory=False)

top_batsmen = data.groupby('batter')['runs_batter'].sum()

top_batsmen = top_batsmen.sort_values(ascending=False).head(10)

print(top_batsmen)

plt.figure(figsize=(12,6))

top_batsmen.plot(kind='bar')

plt.title("Top 10 IPL Run Scorers", fontsize=16)
plt.xlabel("Players", fontsize=12)
plt.ylabel("Runs", fontsize=12)

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("assets/top_batsmen.png")

plt.show()
```

---

## Concepts Learned

| Concept       | Description             |
| ------------- | ----------------------- |
| groupby()     | Groups player-wise data |
| sum()         | Calculates total runs   |
| sort_values() | Sorts highest to lowest |
| figsize       | Adjusts chart size      |
| xticks()      | Rotates labels          |

---

## Output

* Top 10 batsmen visualization
* Total runs comparison
* Professional formatted chart

---

# 🎯 Analysis 3 — Top IPL Wicket Takers

## Objective

Identify bowlers with highest wickets in IPL.

---

## Code Used

```python
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("IPL.csv", low_memory=False)

top_bowlers = data.groupby('bowler')['bowler_wicket'].sum()

top_bowlers = top_bowlers.sort_values(ascending=False).head(10)

print(top_bowlers)

plt.figure(figsize=(12,6))

top_bowlers.plot(kind='bar')

plt.title("Top 10 IPL Wicket Takers", fontsize=16)
plt.xlabel("Bowlers", fontsize=12)
plt.ylabel("Wickets", fontsize=12)

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("assets/top_bowlers.png")

plt.show()
```

---

## Concepts Learned

| Concept           | Description                     |
| ----------------- | ------------------------------- |
| groupby('bowler') | Groups bowler-wise data         |
| bowler_wicket     | Counts wickets                  |
| visualization     | Displays performance comparison |

---

## Output

* Top wicket-taking bowlers chart
* Bowler performance insights

---

# 🪙 Analysis 4 — Toss Winner Analysis

## Objective

Analyze which IPL teams win tosses most frequently.

---

## Code Used

```python
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
```

---

## Concepts Learned

| Concept              | Description                 |
| -------------------- | --------------------------- |
| categorical analysis | Team-based comparisons      |
| chart formatting     | Improved visual appearance  |
| visualization export | Saving graphs automatically |

---

# 📈 Key Insights

## Team Insights

* Mumbai Indians emerged as one of the most successful IPL teams.
* Chennai Super Kings consistently performed among top teams.
* Toss-winning frequency showed patterns among major franchises.

---

## Player Insights

* Top batsmen demonstrated consistency across seasons.
* Leading bowlers dominated wicket-taking charts.
* Player performance can be clearly visualized using grouped analytics.

---

# 🧠 Skills Gained

This project helped in learning:

* Python fundamentals
* Data analysis workflow
* CSV file handling
* Data grouping and aggregation
* Data visualization
* Problem solving
* Error handling
* Project structuring
* Documentation writing

---

# 🚧 Challenges Faced

## 1. Library Installation Errors

Solved by:

```bash
pip install pandas
pip install matplotlib
```

---

## 2. Missing Folder Error

Error:

```text
FileNotFoundError
```

Solution:

Created an `assets` folder manually.

---

## 3. Dataset Understanding

Learned how to:

* identify useful columns
* understand player statistics
* interpret cricket datasets

---

# 🔮 Future Improvements

Future enhancements planned:

* Power BI Dashboard
* Season-wise analysis
* Venue analysis
* Win prediction model
* Interactive charts
* SQL integration
* Streamlit web dashboard

---

# 📷 Sample Visualizations

## Team Wins Analysis

```text
assets/top_teams.png
```

## Top Batsmen Analysis

```text
assets/top_batsmen.png
```

## Top Bowlers Analysis

```text
assets/top_bowlers.png
```

## Toss Winner Analysis

```text
assets/toss_winners.png
```

---

# 💡 Conclusion

This IPL Data Analysis project successfully demonstrates beginner-level sports analytics using Python.

The project provided practical experience in:

* handling real-world datasets
* analyzing cricket statistics
* generating insights
* creating visualizations
* organizing project documentation

This project marks an important step toward becoming a Data Analyst.

---

## Dataset

Dataset was too large to upload to GitHub.
Download IPL dataset separately from Kaggle.

---

# 👨‍💻 Author

**Arjun A Acharry**

Aspiring Data Analyst | UI/UX Designer | Tech Enthusiast

---

# ⭐ If You Like This Project

Consider giving the repository a ⭐ on GitHub.
