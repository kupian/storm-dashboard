from dash import Dash, html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define the layout
app.layout = dbc.Container([
    html.H1("Live Video Feed Dashboard", style={'text-align': 'center', 'margin-bottom': '20px'}),
    dbc.Row([
        dbc.Col(html.Div([
            html.Iframe(
                src="https://www.youtube.com/embed/wiqaaiseH2I?si=BZndaOnUcz-_wHaT?autoplay=1&mute=1",  # Replace with your video URL
                style={'width': '100%', 'height': '300px', 'border': 'none'}
            ),
            html.P("Camera 1", style={'text-align': 'center'})
        ]), width=6),  # Adjust the width as needed
        dbc.Col(html.Div([
            html.Iframe(
                src="https://www.youtube.com/embed/7TTrwuQ-luY?si=vcRmzCtql360yUYN?autoplay=1&mute=1",  # Replace with your video URL
                style={'width': '100%', 'height': '300px', 'border': 'none'}
            ),
            html.P("Camera 2", style={'text-align': 'center'})
        ]), width=6),
        dbc.Col(html.Div([
            html.Iframe(
                src="https://www.meteoblue.com/en/weather/maps/widget/north-port_united-states_4166274?windAnimation=1&gust=1&satellite=1&cloudsAndPrecipitation=1&temperature=1&sunshine=1&extremeForecastIndex=1&geoloc=fixed&tempunit=C&windunit=km%252Fh&lengthunit=metric&zoom=5&autowidth=auto",
                style={'width': '100%', 'height': '400px', 'border': 'none'},
            )
        ]))
    ]),
    # Add more rows as necessary for more video feeds
], fluid=True)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)