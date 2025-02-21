# Imports for Dash and Dash.html
# Import Dash Bootstrap Components (dbc)
from dash import Dash, html
import dash_bootstrap_components as dbc

# Variable that defines the meta tag for the viewport (required to support responsive design)
meta_tags = [
    {"name": "viewport", "content": "width=device-width, initial-scale=1"},
]

# Variable that contains the external_stylesheet to use, in this case Bootstrap styling from dash bootstrap components (dbc)
external_stylesheets = [dbc.themes.BOOTSTRAP]

# Pass the stylesheet and meta_tag variables to the Dash app constructor
app = Dash(__name__, external_stylesheets=external_stylesheets, meta_tags=meta_tags)

# Add an HTML layout to the Dash app (Using HTML in Dash)
# This is the HTML to create page layout
app.layout = dbc.Container([
    # Heading
    html.H1(children='Hello Dash'),  # similar to html.H1('Hello Dash')
    # Add an HTML div contains html.H1, html.P, html.Img
    # Div = division, use to create sections/divisions
    html.Div(children=[
        html.H1('A First Heading'),
        html.P('Dash: A web application framework for Python.'),  # paragraph
        # This line has been split to adhere to the line length limit

        html.Img(src=app.get_asset_url('bar-chart-placeholder.png'))
    ])
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=5050)
