from dash import Dash, html, Input, Output, clientside_callback
import dash_bootstrap_components as dbc

# Define the meta tag for the viewport (required to support responsive design)
meta_tags = [
    {"name": "viewport", "content": "width=device-width, initial-scale=1"},
]

# Variable that contains the external_stylesheet to use, 
external_stylesheets = [
    dbc.themes.BOOTSTRAP,
    dbc.icons.FONT_AWESOME,]

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
    dbc.Col([
        html.H1("Paralympics Data Analytics"),
        html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent congue luctus elit nec gravida.")
    ], width=12)
], justify="center", align="center")

row_two = dbc.Row([
    
    # Drop Down Column 1
    dbc.Col([
        dbc.Select(
            options=[
                {"label": "Events", "value": "events"},  # The value is in the format of the column heading in the data
                {"label": "Sports", "value": "sports"},
                {"label": "Countries", "value": "countries"},
                {"label": "Athletes", "value": "participants"},
            ],
            value="events",  # The default selection
            id="dropdown-input",  # id uniquely identifies the element, will be needed later for callbacks
        ),
    ], width=4),
    
    #Checklist Column 2
    dbc.Col([
        html.Div([
            dbc.Label("Select the Paralympic Games type"),
            dbc.Checklist(
                options=[
                    {"label": "Summer", "value": "summer"},
                    {"label": "Winter", "value": "winter"},
                ],
                value=["summer"],  # Values is a list as you can select 1 AND 2
                id="checklist-input",
            ),
        ])         
    ], width={"size": 4, "offset": 2}),
    # 2 'empty' columns between this and the previous column
], justify = "between")

row_three = dbc.Row([
# note: className="img-fluid" is a Bootstrap class and prevents the image spanning the next column    
    # Column 1: line chart Img
    dbc.Col(children=[
        html.Img(src=app.get_asset_url('line-chart-placeholder.png'), className="img-fluid"),   
    ], width=6),
    
    # Column 2: bar chart img
    dbc.Col(children=[
        html.Img(src=app.get_asset_url('bar-chart-placeholder.png'), className="img-fluid"),
    ], width=6),
], justify = "between")

row_four = dbc.Row([
    # Column 1: visualisation map with markers for events.
    dbc.Col(children=[
        html.Img(src=app.get_asset_url('map-placeholder.png'), className="img-fluid"),
    ], width=8),
    
    # Column 2: card with event details        
    dbc.Col(children=[
        dbc.Card([
            dbc.CardImg(src=app.get_asset_url("logos/2022_Beijing.jpg"), top=True),
            dbc.CardBody([
                html.H4("Beijing 2022", className="card-title"),
                html.P("Number of athletes: XX", className="card-text", ),
                html.P("Number of events: XX", className="card-text", ),
                html.P("Number of countries: XX", className="card-text", ),
                html.P("Number of sports: XX", className="card-text", ),
            ]),
        ],
            style={"width": "18rem"},
        ),    
    ], width=4),
], justify = "between")

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
