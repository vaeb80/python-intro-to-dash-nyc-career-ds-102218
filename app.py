import dash
import dash_core_components as dcc
import dash_html_components as html
from uber_data import data

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1("Hey, this is my first dash app!"),
    html.P("Still under construction... :)"),
    dcc.Graph(
        id = "uber_pricing_graph",
        figure = {
            'data': data,
            'layout': {
                'title': 'Uber Pricing in Brooklyn and Manhattan'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
