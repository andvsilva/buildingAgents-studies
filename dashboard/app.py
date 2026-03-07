from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

df = pd.DataFrame({
    "x": [1,2,3,4],
    "y": [10,15,13,17]
})

fig = px.line(df, x="x", y="y")
fig.update_layout(template="plotly_dark")

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Dark Dashboard"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)