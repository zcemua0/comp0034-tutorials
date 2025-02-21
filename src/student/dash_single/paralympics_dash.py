from dash import Dash, html, Input, Output, clientside_callback
import dash_bootstrap_components as dbc

# Define the meta tag for the viewport (required to support responsive design)
meta_tags = [
    {"name": "viewport", "content": "width=device-width, initial-scale=1"},
]

# Variable that contains the external_stylesheet to use, 
external_stylesheets = [dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME]

# Pass the stylesheet and meta_tag variables to the Dash app constructor
app = Dash(__name__, external_stylesheets=external_stylesheets, meta_tags=meta_tags)

# colormode switch
color_mode_switch = html.Span([
    dbc.Label(className="fa fa-moon", html_for="theme-switch"),
    dbc.Switch(id="theme-switch", value=False, className="d-inline-block ms-1", persistence=True),
    dbc.Label(className="fa fa-sun", html_for="theme-switch"),
])

# This is the HTML to create page layout
app.layout = dbc.Container([
    html.H1(children='Hello Dash'), 
     
    # Add theme switcher
    html.Div(children=[ 
        dbc.Switch(
            id='theme-switch',
            value=False,
            className="d-inline-block ms-1",
            persistence=True,
            label='Theme Mode',
            style={'margin': '20px'}
        ),
        html.H1('A First Heading'),  
        html.P('Toggle the theme using the switch below:'),
        html.P('Dash: A web application framework for Python.'),        
        html.Img(src=app.get_asset_url('bar-chart-placeholder.png'))
    ]),
    # Hidden div for setting Bootstrap theme
    html.Div(id="theme-container", style={"display": "none"})
])

# Client-side callback to toggle theme
clientside_callback(
    """
    (switchOn) => {
        document.documentElement.setAttribute("data-bs-theme", switchOn ? "dark" : "light");
        return window.dash_clientside.no_update;
    }
    """,
    Output("theme-switch", "id"), 
    Input("theme-switch", "value"),
)

# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=5050)
