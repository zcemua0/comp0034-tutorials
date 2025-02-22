from importlib import resources

# import dash
# import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
# from dash import html


def line_chart(feature):
    """ Creates a line chart with data from paralympics.csv

    Data is displayed over time from 1960 onwards.
    The figure shows separate trends for the winter and summer events.

     Parameters
     feature: events, sports or participants

     Returns
     fig: Plotly Express line figure
     """

    # take the feature parameter from the function and check it is valid
    if feature not in ["sports", "participants", "events", "countries"]:
        raise ValueError(
            'Invalid value for "feature". Must be one of ["sports", '
            '"participants", "events", "countries"]')
    else:
        # Make sure it is lowercase to match the dataframe column names
        feature = feature.lower()

    # Read the data from .csv into a DataFrame
    cols = ["type", "year", "host", feature]
    
    # Uses importlib.resources rather than pathlib.Path
    with resources.path("student.data", "paralympics.csv") as path:
        line_chart_data = pd.read_csv(path, usecols=cols)

        # Create a Plotly Express line chart with the following parameters
        #    line_chart_data is the DataFrame
        #    x="year" is the column to use as the x-axis
        #    y=feature is the column to use as the y-axis
        #    color="type" indicates if winter or summer (# goal: add legends)
        fig = px.line(line_chart_data, x="year", y=feature, color="type",
                      title=f"How has the number of {feature} changed over time?",
                      template="simple_white",
                      labels={
                          "year": "Year",
                          "feature": "",
                      }  
                      )
                      
        return fig
    

# Create bar chart stacked
def bar_gender(event_type):
    """
    Creates a stacked bar chart showing change in the ration of male and female competitors in the summer and winter paralympics.

    Parameters
    event_type: str Winter or Summer

    Returns
    fig: Plotly Express bar chart
    """
    cols = ['type', 'year', 'host', 'participants_m', 'participants_f', 'participants']
    with resources.path("student.data", "paralympics.csv") as path:
        df_events = pd.read_csv(path, usecols=cols)
        
        # Drop Rome as there is no male/female data
        # Drop rows where male/female data is missing
        df_events = df_events.dropna(subset=['participants_m', 'participants_f'])
        df_events.reset_index(drop=True, inplace=True)

        # Add new columns that each contain the result of calculating the % of male and female participants
        df_events['Male'] = df_events['participants_m'] / df_events['participants']
        df_events['Female'] = df_events['participants_f'] / df_events['participants']

        # Sort the values by Type and Year
        df_events.sort_values(['type', 'year'], ascending=(True, True), inplace=True)
        # Create a new column that combines Location and Year to use as the x-axis
        df_events['xlabel'] = df_events['host'] + ' ' + df_events['year'].astype(str)

        # Create the stacked bar plot of the % for male and female
        df_events = df_events.loc[df_events['type'] == event_type]
        fig = px.bar(df_events,
                     x='xlabel',
                     y=['Male', 'Female'],
                     title=f'How has the ratio of female:male participants changed in {event_type} paralympics?',
                     labels={'xlabel': '', 'value': '', 'variable': ''},
                     template="simple_white"
                     )
        fig.update_xaxes(ticklen=0)
        fig.update_yaxes(tickformat=".0%")
        return fig
    
    
   