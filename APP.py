import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


st.set_page_config(page_title="IPL Data Analysis", page_icon="🏏", layout="wide")


st.title("🏏 IPL Data Analysis (2008-2024)")
st.markdown("---")


@st.cache_data
def load_data():
    deliveries_id = "1lbdRThloPQZKcDoyjRrg-4mkZtv8e-tK"
    matches_id = "1NJZT9CvvsD4WYWQ7dpCmOovXy5o7U-_W"

    deliveries_url = f"https://drive.google.com/uc?export=download&id={deliveries_id}"
    matches_url = f"https://drive.google.com/uc?export=download&id={matches_id}"

    matches = pd.read_csv(matches_url)
    deliveries = pd.read_csv(deliveries_url)

    matches = matches.dropna(subset=['winner'])
    matches['city'] = matches['city'].fillna('Unknown')
    matches['player_of_match'] = matches['player_of_match'].fillna('Unknown')
    return matches, deliveries

matches, deliveries = load_data()

st.success("✅ Data Loaded Successfully!")
col1, col2 = st.columns(2)
col1.metric("Total Matches", matches.shape[0])
col2.metric("Total Deliveries", deliveries.shape[0])

st.markdown("---")


st.subheader("📊 Visualization 1: Most Matches Won by Each Team")
st.markdown("**Insight:** Mumbai Indians have won the most matches in IPL history, followed by Chennai Super Kings.")
fig1, ax1 = plt.subplots(figsize=(12, 6))
win_counts = matches['winner'].value_counts()
sns.barplot(x=win_counts.values, y=win_counts.index, hue=win_counts.index, palette='rocket', legend=False, ax=ax1)
ax1.set_title('Most Matches Won by Each Team')
ax1.set_xlabel('Number of Wins')
ax1.set_ylabel('Team')
plt.tight_layout()
st.pyplot(fig1)

st.markdown("---")


st.subheader("📊 Visualization 2: Toss Winner vs Match Winner")
st.markdown("**Insight:** Winning the toss does not guarantee winning the match. Nearly 50% of toss winners go on to lose.")
toss_win = matches[matches['toss_winner'] == matches['winner']]
toss_loss = matches[matches['toss_winner'] != matches['winner']]
labels = ['Toss Winner Won Match', 'Toss Winner Lost Match']
sizes = [len(toss_win), len(toss_loss)]
fig2, ax2 = plt.subplots(figsize=(7, 7))
ax2.pie(sizes, labels=labels, autopct='%1.1f%%', colors=['#4CAF50', '#FF5733'], startangle=140)
ax2.set_title('Toss Winner vs Match Winner')
plt.tight_layout()
st.pyplot(fig2)

st.markdown("---")


st.subheader("📊 Visualization 3: Top 10 Run Scorers")
st.markdown("**Insight:** Virat Kohli leads the all-time run scoring charts in IPL history.")
top_scorers = deliveries.groupby('batter')['batsman_runs'].sum().sort_values(ascending=False).head(10)
fig3, ax3 = plt.subplots(figsize=(12, 6))
sns.barplot(x=top_scorers.values, y=top_scorers.index, hue=top_scorers.index, palette='magma', legend=False, ax=ax3)
ax3.set_title('Top 10 Run Scorers in IPL History')
ax3.set_xlabel('Total Runs')
ax3.set_ylabel('Batsman')
plt.tight_layout()
st.pyplot(fig3)

st.markdown("---")


st.subheader("📊 Visualization 4: Top 10 Wicket Takers")
st.markdown("**Insight:** Lasith Malinga is the highest wicket taker in IPL history (2008-2020).")
wickets = deliveries[deliveries['dismissal_kind'].notna()]
top_bowlers = wickets.groupby('bowler')['dismissal_kind'].count().sort_values(ascending=False).head(10)
fig4, ax4 = plt.subplots(figsize=(12, 6))
sns.barplot(x=top_bowlers.values, y=top_bowlers.index, hue=top_bowlers.index, palette='coolwarm', legend=False, ax=ax4)
ax4.set_title('Top 10 Wicket Takers in IPL History')
ax4.set_xlabel('Total Wickets')
ax4.set_ylabel('Bowler')
plt.tight_layout()
st.pyplot(fig4)

st.markdown("---")


st.subheader("📊 Visualization 5: Season-wise Total Runs")
st.markdown("**Insight:** Total runs scored per season has increased over the years, showing batting dominance.")
season_runs = deliveries.groupby('match_id')['total_runs'].sum().reset_index()
season_runs = season_runs.merge(matches[['id', 'season']], left_on='match_id', right_on='id')
season_total = season_runs.groupby('season')['total_runs'].sum()
fig5, ax5 = plt.subplots(figsize=(12, 6))
ax5.plot(season_total.index, season_total.values, marker='o', color='orange', linewidth=2)
ax5.set_title('Season-wise Total Runs Scored in IPL')
ax5.set_xlabel('Season')
ax5.set_ylabel('Total Runs')
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig5)

st.markdown("---")


st.subheader("📊 Visualization 6: Most Player of the Match Awards")
st.markdown("**Insight:** AB de Villiers and Chris Gayle have won the most Player of the Match awards.")
top_players = matches['player_of_match'].value_counts().head(10)
fig6, ax6 = plt.subplots(figsize=(12, 6))
sns.barplot(x=top_players.values, y=top_players.index, hue=top_players.index, palette='viridis', legend=False, ax=ax6)
ax6.set_title('Most Player of the Match Awards')
ax6.set_xlabel('Number of Awards')
ax6.set_ylabel('Player')
plt.tight_layout()
st.pyplot(fig6)

st.markdown("---")


st.subheader("📊 Visualization 7: Season-wise Fours and Sixes")
st.markdown("**Insight:** 2013 season had the most boundaries. Sixes have increased significantly over the years.")
fours = deliveries[deliveries['batsman_runs'] == 4].groupby('match_id')['batsman_runs'].count().reset_index()
sixes = deliveries[deliveries['batsman_runs'] == 6].groupby('match_id')['batsman_runs'].count().reset_index()
fours = fours.merge(matches[['id', 'season']], left_on='match_id', right_on='id')
sixes = sixes.merge(matches[['id', 'season']], left_on='match_id', right_on='id')
season_fours = fours.groupby('season')['batsman_runs'].count()
season_sixes = sixes.groupby('season')['batsman_runs'].count()
fig7, ax7 = plt.subplots(figsize=(12, 6))
ax7.bar(season_fours.index, season_fours.values, label='Fours', color='blue', alpha=0.7)
ax7.bar(season_sixes.index, season_sixes.values, label='Sixes', color='red', alpha=0.7, bottom=season_fours.values)
ax7.set_title('Season-wise Fours and Sixes')
ax7.set_xlabel('Season')
ax7.set_ylabel('Count')
plt.xticks(rotation=45)
ax7.legend()
plt.tight_layout()
st.pyplot(fig7)

st.markdown("---")


st.subheader("📊 Visualization 8: Winning by Runs vs Wickets")
st.markdown("**Insight:** More matches are won by wickets than runs, showing chasing teams have an advantage.")
win_by_runs = matches[matches['result'] == 'runs']['result'].count()
win_by_wickets = matches[matches['result'] == 'wickets']['result'].count()
labels = ['Won by Runs', 'Won by Wickets']
sizes = [win_by_runs, win_by_wickets]
fig8, ax8 = plt.subplots(figsize=(7, 7))
ax8.pie(sizes, labels=labels, autopct='%1.1f%%', colors=['#3498DB', '#E74C3C'], startangle=140, explode=(0.05, 0.05))
ax8.set_title('Winning by Runs vs Wickets')
plt.tight_layout()
st.pyplot(fig8)

st.markdown("---")


st.subheader("📊 Visualization 9: Top 10 Venues by Number of Matches")
st.markdown("**Insight:** Wankhede Stadium and M. Chinnaswamy Stadium have hosted the most IPL matches.")
top_venues = matches['venue'].value_counts().head(10)
fig9, ax9 = plt.subplots(figsize=(12, 6))
sns.barplot(x=top_venues.values, y=top_venues.index, hue=top_venues.index, palette='Set2', legend=False, ax=ax9)
ax9.set_title('Top 10 Venues by Number of Matches')
ax9.set_xlabel('Number of Matches')
ax9.set_ylabel('Venue')
plt.tight_layout()
st.pyplot(fig9)

st.markdown("---")


st.subheader("📊 Visualization 10: Top 10 Batsmen by Average Runs per Ball")
st.markdown("**Insight:** Hard-hitting batsmen dominate the average runs per ball chart.")
avg_runs = deliveries.groupby('batter')['batsman_runs'].mean().sort_values(ascending=False).head(10)
fig10, ax10 = plt.subplots(figsize=(12, 6))
sns.barplot(x=avg_runs.values, y=avg_runs.index, hue=avg_runs.index, palette='cubehelix', legend=False, ax=ax10)
ax10.set_title('Top 10 Batsmen by Average Runs per Ball')
ax10.set_xlabel('Average Runs')
ax10.set_ylabel('Batsman')
plt.tight_layout()
st.pyplot(fig10)

st.markdown("---")


st.subheader("📝 Conclusion")
st.markdown("""
This analysis of IPL data from 2008 to 2024 reveals that:
- 🏆 **Mumbai Indians** are the most successful IPL team
- 🏏 **Virat Kohli** is the leading run scorer
- 🎳 **Lasith Malinga** is the highest wicket taker
- 📈 **Batting has become more dominant** over the years
- 🎯 **Toss winning** does not significantly impact match results
""")
