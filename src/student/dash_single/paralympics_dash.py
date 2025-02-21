# Imports for Dash and Dash.html
from dash import Dash, html

# Create an instance of the Dash app
app = Dash(__name__)

# Add an HTML layout to the Dash app (Using HTML in Dash)
# This is the HTML to create page layout
app.layout = html.Div([
    # children is a special attribute and if used as the first attribute does not need to be named
    # create the heading
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
    app.run(debug=True, port=5051)
