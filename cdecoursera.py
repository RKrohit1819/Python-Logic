# In[ ]:


import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px

# Load the data using pandas
data = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv')

# Initialize the Dash app
app = dash.Dash(__name__)

# Set the title of the dashboard
#app.title = "Automobile Statistics Dashboard"

#---------------------------------------------------------------------------------
# Create the dropdown menu options
dropdown_options = [
    {'label': 'Yearly Statistics', 'value': 'Yearly Statistics'},
    {'label': 'Recession Period Statistics', 'value': 'Recession Period Statistics'}
]
# List of years 
year_list = [i for i in range(1980, 2024, 1)]
#---------------------------------------------------------------------------------------
# Create the layout of the app
app.layout = html.Div([
    #TASK 2.1 Add title to the dashboard
    html.H1("Automobile Sales Statistics Dashboard"),#May include style for title
    html.Div([#TASK 2.2: Add two dropdown menus
        html.Label("Select Statistics:"),
          dcc.Dropdown(id='select year', 
                   options=[
                           {'label': 'Yearly Statistics', 'value': 'Yearly Statistics'},
                           {'label': 'Recession Period Statistics', 'value': 'Recession Period Statistics'}
                           ],
                  placeholder='Select a report type',
                  style={flex})
    ]),
    html.Div(dcc.Dropdown(
            id='select-year',
            options=[{'label': i, 'value': i} for i in year_list],
            value='Yearly Statistics'
        )),
    html.Div([#TASK 2.3: Add a division for output display
    html.Div(id='output-container', className='chart-grid', style={'display': 'flex'}),])
])
#TASK 2.4: Creating Callbacks
# Define the callback function to update the input container based on the selected statistics
@app.callback(
    Output(component_id='select year', component_property='disabled'),
    Input(component_id='input component',component_property='disabled'))

def update_input_container(Input):
    if selected_statistics =='Yearly Statistics': 
        return False
    else: 
        return True

#Callback for plotting
# Define the callback function to update the input container based on the selected statistics
@app.callback(
    Output(component_id='select-year', component_property='disabled'),
    [Input(component_id='select-year', component_property='disabled'), Input(component_id='dropdown-statistics', component_property='disabled')])


def update_output_container(selected_statistics, data):
    if selected_statistics == 'Recession Period Statistics':
        # Filter the data for recession periods
        recession_data = data[data['Recession'] == 1]
        
#TASK 2.5: Create and display graphs for Recession Report Statistics

#Plot 1 Automobile sales fluctuate over Recession Period (year wise)
        # use groupby to create relevant data for plotting
        yearly_rec=recession_data.groupby('Year')['Automobile_Sales'].mean().reset_index()
        R_chart1 = dcc.Graph(
            figure=px.line(yearly_rec, 
                x='Year',
                y='Automobile_Sales',
                title="Average Automobile Sales fluctuation over Recession Period"))

#Plot 2 Calculate the average number of vehicles sold by vehicle type       
        # use groupby to create relevant data for plotting
        average_sales = recession_data.groupby('VehicleType')['Sales'].mean().reset_index()                          
        R_chart2 = dcc.Graph(figure=px.bar(
            average_sales,
            x='VehicleType',
            y='Sales',
            title='Average Number of Vehicles Sold by Vehicle Type'
        ))
        
# Plot 3 Pie chart for total expenditure share by vehicle type during recessions
        # use groupby to create relevant data for plotting
         exp_rec = recession_data.groupby('VehicleType')['Expenditure'].sum().reset_index()
R_chart3 = dcc.Graph(
    figure=px.pie(
        exp_rec,
        values='Expenditure',  # Assuming 'Expenditure' is the column with expenditure data
        names='VehicleType',
        title='Total Expenditure Share by Vehicle Type during Recessions'
    )
)

# Plot 4 bar chart for the effect of unemployment rate on vehicle type and sales
        grouped_data = recession_data.groupby('VehicleType').agg({'Sales': 'mean','UnemploymentRate': 'mean'}).reset_index()
       R_chart4 = dcc.Graph(
       fig = px.bar(
    grouped_data,
    x='VehicleType',
    y=['Sales', 'UnemploymentRate'],
    barmode='group',
    labels={'VehicleType': 'Vehicle Type', 'value': 'Mean Value'},
    title='Effect of Unemployment Rate on Vehicle Type and Sales'
)

        return [
            html.Div(className='chart-item', children=[html.Div(children=R_chart1),html.Div(children=R_chart2)],style={'display': 'flex'}),
            html.Div(className='chart-item', children=[html.Div(children=R_chart3),html.Div(children=R_chart4)],style={'display': 'flex'})
            ]

# TASK 2.6: Create and display graphs for Yearly Report Statistics
 # Yearly Statistic Report Plots                             
    elif (input_year and selected_statistics=='Yearly Statistic') :
        yearly_data = data[data['Year'] == 2010]
                              
#TASK 2.5: Creating Graphs Yearly data
                              
#plot 1 Yearly Automobile sales using line chart for the whole period.
        yas = data.groupby('Year')['Automobile_Sales'].mean().reset_index()
      # Create the line chart using Plotly Express
        Y_chart1 = dcc.Graph(
            figure=px.line(
            yas,
            x='Year',  # X-axis: Year
            y='Automobile_Sales',  # Y-axis: Average Automobile Sales
            title='Yearly Automobile Sales',
            labels={'Automobile_Sales': 'Average Sales'},
            template='plotly_dark'  # Example: Use a dark theme (you can change this)
    )
)
            
# Plot 2 Total Monthly Automobile sales using line chart.
        total_monthly_sales = data.groupby('Month')['Automobile_Sales'].sum().reset_index()
        # Create the line chart using Plotly Express
        Y_chart2 = dcc.Graph(
            figure=px.line(
                total_monthly_sales,
                x='Month',  # X-axis: Month
                y='Automobile_Sales',  # Y-axis: Total Monthly Automobile Sales
                title='Total Monthly Automobile Sales',
                labels={'Automobile_Sales': 'Total Sales'},
                template='plotly_dark'  # Example: Use a dark theme (you can change this)
            )
        )

            # Plot bar chart for average number of vehicles sold during the given year
        avr_vdata = yearly_data[yearly_data['Year'] == input_year].groupby('VehicleType')['Automobile_Sales'].mean().reset_index()
        Y_chart3 = dcc.Graph(
    figure=px.bar(
        avr_vdata,
        x='VehicleType',  # X-axis: VehicleType
        y='Automobile_Sales',  # Y-axis: Average Vehicles Sold
        title=f'Average Vehicles Sold by Vehicle Type in the year {input_year}',
        labels={'Automobile_Sales': 'Average Sales'},
        template='plotly_dark'  # Example: Use a dark theme (you can change this)
    )
)

            # Total Advertisement Expenditure for each vehicle using pie chart
        exp_data = yearly_data.groupby('VehicleType')['AdvertisementExpenditure'].sum().reset_index()
       Y_chart4 = dcc.Graph(
    figure=px.pie(
        exp_data,
        values='AdvertisementExpenditure',  # Values for the pie slices
        names='VehicleType',  # Names of the pie slices
        title='Total Advertisement Expenditure for Each Vehicle Type',
        template='plotly_dark'  # Example: Use a dark theme (you can change this)
    )
)

#TASK 2.6: Returning the graphs for displaying Yearly data
        return [
                html.Div(className='chart-item', children=[html.Div(Y_chart1,html.Div(Y_chart2)],style={'display': 'flex'}),
                html.Div(className='chart-item', children=[html.Div(Y_chart3),html.Div(Y_chart4)],style={'display': 'flex'})
                ]
        
    else:
        return None

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)

