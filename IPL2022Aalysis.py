import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

data = pd.read_csv("IPL 2022.excel.csv")
print(data)

#Number of matches won by each team in IPL 2022

# figure = px.bar(data, x = data['match_winner'],title = "Number of matches won in IPL 2022 ")
# print(figure.show())

# # Standardize 'won_by' values before mapping
data["won_by"] = data["won_by"].str.strip().str.lower()

# Map the standardized values to Chasing or Defending
data["won_by"] = data["won_by"].map({"wickets": "Chasing", "runs": "Defending"})

# Check if both categories are mapped correctly
print(data["won_by"].value_counts())

# Prepare labels and counts for the pie chart
won_by = data["won_by"].value_counts()
labels = won_by.index
counts = won_by.values

# Colors for the pie chart
colors = ['gold', 'lightgreen']

# # Create the pie chart
fig = go.Figure(data=[go.Pie(labels=labels, values=counts)])

# # Update layout and traces
fig.update_layout(title_text='Numbers of matches won by defending or chasing')
fig.update_traces(
    hoverinfo='label+percent',
    textinfo='value',
    textfont_size=30,
    marker=dict(colors=colors, line=dict(color='black', width=3))
)

# Display the pie chart
fig.show()

#Best bowler in IPL 2022
# figure  = px.bar(data, x = data["best_bowling"], title = "Best bowlwr in Ipl in 2022")
# figure.show()

#Best Player of the match in IPL 2022:
# figure = px.bar(data, x = data["player_of_the_match"], title = "Best Player of the match in IPL 2022:")
# figure.show()

figure = px.bar(data, x = data["top_scorer"], y = data["highscore"], color  = data["highscore"],title = "Most scorer of the match in IPL 2022")
figure.show()