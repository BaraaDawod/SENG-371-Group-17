# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Hello World'),

    html.Div(children='''
        Online banking website in progress.
    '''),
])

if __name__ == '__main__':
    app.run_server(debug=True)