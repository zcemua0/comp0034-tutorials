from dash import Dash, html, Input, Output, clientside_callback, dcc
import dash_bootstrap_components as dbc

from student.dash_single.creating_charts import line_chart, bar_gender, scatter_geo, create_card

# Define the meta tag for the viewport (required to support responsive design)
meta_tags = [{"name": "viewport", "content": "width=device-width, initial-scale=1"},]

# Variable that contains the external_stylesheet to use, 
external_stylesheets = [
    dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME,]

# Pass the stylesheet and meta_tag variables to the Dash app constructor
app = Dash(__name__, external_stylesheets=external_stylesheets, meta_tags=meta_tags)

# Theme colormode switch
color_mode_switch = html.Span([
    dbc.Label(className="fa fa-moon", html_for="theme-switch"),
    dbc.Switch(id="theme-switch", value=False, className="d-inline-block ms-1", persistence=True),
    dbc.Label(className="fa fa-sun", html_for="theme-switch"),
])

# Create the figure (chart) variables
line_fig = line_chart("sports")
bar_fig = bar_gender("winter")
map = scatter_geo()
card = create_card("Sydney 2000")

# Define layout components 
row_one = dbc.Row([
    dbc.Col([
        html.H1("Paralympics Data Analytics Dashboard", id='title'),
        html.P("Try to answer the questions using the charts below.")
    ], width=12)
], justify="center", align="center")

row_two = dbc.Row([
    # Drop Down Column 1
    dbc.Col(children=[
        # format: Input(component_id="", component_property="",  options, value=...)
        dbc.Select(
            id="dropdown-category",     # This is the component's id that will let to find component on the webpage
            options=[
                {"label": "Events", "value": "events"},  # The value is in the format of property with the needed value for the callback
                {"label": "Sports", "value": "sports"},  # The value is the heading format of the selected options
                {"label": "Countries", "value": "countries"},
                {"label": "Athletes", "value": "participants"},
            ],
            value="events",  # The default selection
        ),
    ], width=4),
    # Checklist Column 2
    dbc.Col(children=[
        html.Div([
            dbc.Label("Select the Paralympic Games type"),
            dbc.Checklist(
                options=[
                    {"label": "Summer", "value": "summer"},
                    {"label": "Winter", "value": "winter"},
                ],
                value=["summer"],  # Values is a list as you can select 1 AND 2
                id="checklist-games-type",
            ),
        ])         
    ], width={"size": 4, "offset": 2}), # 2 'empty' columns between columns
], justify="between")

row_three = dbc.Row([
    # Column 1: line chart ( This is the output for line chart)
    dbc.Col(children=[
        dcc.Graph(id="line-chart", figure=line_fig), ], width=6),   
    # Column 2: bar char
    dbc.Col(children=[], id="bar-chart", width=6),
], align="start")

row_four = dbc.Row([
    # Column 1: visualisation map with markers for events.
    dbc.Col(children=[
        dcc.Graph(id='map', figure=map), ], width=8),
    # Column 2: card with event details        
    dbc.Col(children=[card], id='card', width=4),
    ], align="start")

app.layout = dbc.Container([    
    # ----Layout components----
    row_one,
    row_two,
    row_three,
    row_four,
    
    # ----Theme switch---- # try to define above then just call dbc.switch here
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
    html.Div(id="theme-container", style={"display": "none"}),       
])


# Callback to update the line chart
@app.callback(
    Output(component_id="line-chart", component_property="figure"),
    Input(component_id="dropdown-category", component_property="value"),
)   # ensure no blank line
def update_line_chart(feature):
    """ Update the line chart based on the dropdown selection """
    figure = line_chart(feature)
    return figure


# Callback to update the bar chart
# This version removes the original bar chart component from the layout and treats the Col as the Output
@app.callback(
    Output(component_id='bar-chart', component_property='children'),
    Input(component_id='checklist-games-type', component_property='value')
)
def update_bar_chart(selected_values):
    """ Updates the bar chart based on the checklist selection.
     Creates one chart for each of the selected values.
     """
    figures = []
    # Iterate the list of values from the checkbox component
    for value in selected_values:
        fig = bar_gender(value)
        # Assign id to be used to identify the charts
        id = f"bar-chart-{value}"
        element = dcc.Graph(figure=fig, id=id)
        figures.append(element)
    return figures


# Callback to update the card based on the map hover data
@app.callback(
    Output('card', 'children'),
    Input('map', 'hoverData'),
)
def display_card(hover_data):
    """ 
    Display a card with information about the selected country on the map 
    """
    if hover_data is not None:
        text = hover_data['points'][0]['hovertext']
        return create_card(text)


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
