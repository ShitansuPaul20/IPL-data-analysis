# 🏏 IPL Data Analysis (2008-2024)

## 📌 Project Overview
This project performs Exploratory Data Analysis (EDA) on IPL (Indian Premier League) cricket data from 2008 to 2024. The analysis includes data cleaning, preprocessing, and 10 meaningful visualizations with insights.

---

## 📂 Dataset
- **Source:** [Kaggle - IPL Complete Dataset](https://www.kaggle.com/datasets/patrickb1912/ipl-complete-dataset-20082020)
- **Files Used:**
  - `matches.csv` — Match-level data (1090 matches) - [matches.csv](https://drive.google.com/file/d/1NJZT9CvvsD4WYWQ7dpCmOovXy5o7U-_W/view?usp=drive_link)
  - `deliveries.csv` — Ball-by-ball data (172,943 deliveries) - [deliveries.csv](https://drive.google.com/file/d/1lbdRThloPQZKcDoyjRrg-4mkZtv8e-tK/view?usp=drive_link)

---

## 🛠️ Libraries Used
- `Pandas` — Data manipulation and cleaning
- `Matplotlib` — Data visualization
- `Seaborn` — Statistical data visualization

---

## 🧹 Data Cleaning
- Removed rows where `winner` was null (abandoned matches)
- Filled missing `city` values with `'Unknown'`
- Filled missing `player_of_match` values with `'Unknown'`

---

## 📊 Visualizations

| # | Visualization | Insight |
|---|--------------|---------|
| 1 | Most Matches Won by Each Team | Mumbai Indians are the most successful IPL team |
| 2 | Toss Winner vs Match Winner | Winning toss does not guarantee winning the match |
| 3 | Top 10 Run Scorers | Virat Kohli leads the run-scoring charts |
| 4 | Top 10 Wicket Takers | Lasith Malinga is the highest wicket taker (2008-2020) |
| 5 | Season-wise Total Runs | Run scoring has increased over the years |
| 6 | Most Player of the Match Awards | AB de Villiers and Chris Gayle dominate POTM awards |
| 7 | Season-wise Fours and Sixes | 2013 had the most boundaries in IPL history |
| 8 | Winning by Runs vs Wickets | More matches are won by wickets than by runs |
| 9 | Top 10 Venues by Matches | Wankhede Stadium and Chinnaswamy host the most matches |
| 10 | Top 10 Batsmen by Average Runs per Ball | Hard-hitters dominate the average runs per ball |

---

## 🚀 How to Run
1. Open [Google Colab](https://colab.research.google.com)
2. Upload `IPL_Data_Analysis.ipynb`
3. Upload `matches.csv` and `deliveries.csv` to the session
4. Run all cells from top to bottom

---

## 📁 Project Structure
```
IPL-Data-Analysis/
│
├── IPL_Data_Analysis.ipynb   ← Main notebook
├── matches.csv               ← Match data
├── deliveries.csv            ← Ball-by-ball data
└── README.md                 ← Project documentation
```

---

## 👤 Author
- **Name:** Shitansu Paul
- **Date:** April 2026
