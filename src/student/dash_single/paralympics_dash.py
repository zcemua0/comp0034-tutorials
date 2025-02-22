from dash import Dash, html, Input, Output, clientside_callback
import dash_bootstrap_components as dbc

# Define the meta tag for the viewport (required to support responsive design)
meta_tags = [
    {"name": "viewport", "content": "width=device-width, initial-scale=1"},
    # Added for better readability
]

# Variable that contains the external_stylesheet to use, 
external_stylesheets = [
    dbc.themes.BOOTSTRAP,
    dbc.icons.FONT_AWESOME,
]

# Pass the stylesheet and meta_tag variables to the Dash app constructor
app = Dash(__name__, external_stylesheets=external_stylesheets, meta_tags=meta_tags)

# Theme colormode switch
color_mode_switch = html.Span([
    dbc.Label(className="fa fa-moon", html_for="theme-switch"),
    dbc.Switch(id="theme-switch", value=False, className="d-inline-block ms-1", persistence=True),
    dbc.Label(className="fa fa-sun", html_for="theme-switch"),
])

# Define layout components 
row_one = dbc.Row([
    dbc.Col(['App name and text']),
])

row_two = dbc.Row([
    dbc.Col(children=['drop down'], width=4),
    dbc.Col(children=['check boxes'], width={"size": 4, "offset": 2}),
    # 2 'empty' columns between this and the previous column
])

row_three = dbc.Row([
    dbc.Col(children=['line chart'], width=6),
    dbc.Col(children=['bar chart'], width=6),
])

row_four = dbc.Row([
    dbc.Col(children=['world map showing event locations'], width=8),
    dbc.Col(children=['card showing event details'], width=4),
])

app.layout = dbc.Container([
    # Layout components
    row_one,
    row_two,
    row_three,
    row_four,
    
    # Theme switch 
    html.Div([ 
        dbc.Switch(
            id='theme-switch',
            value=False,
            className="d-inline-block ms-1",
            persistence=True,
            label='Theme Mode',
            style={'margin': '20px'}
        ),
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
    app.run(debug=True, port=5050)  # Run the app in debug mode
