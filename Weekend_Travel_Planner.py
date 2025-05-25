
import pandas as pd

# Sample data for destinations
trip_data = {
    'Destination': ['Asheville', 'Nashville', 'Savannah', 'Miami', 'New York City', 'Chicago'],
    'Travel Type': ['Car', 'Car', 'Car', 'Flight', 'Flight', 'Flight'],
    'Distance (mi)': [200, 250, 250, None, None, None],
    'Flight Cost ($)': [None, None, None, 180, 220, 200],
    'Lodging per Night ($)': [120, 130, 110, 150, 170, 160],
    'Food & Drinks per Day ($)': [60, 65, 55, 70, 80, 75],
    'Activities ($)': [100, 120, 90, 150, 180, 160],
    'Trip Length (days)': [3, 3, 3, 3, 3, 3]
}

# Create DataFrame
df = pd.DataFrame(trip_data)

# Compute transport cost
gas_cost_per_mile = 0.15
df['Transport Cost ($)'] = df.apply(
    lambda row: row['Distance (mi)'] * gas_cost_per_mile * 2 if row['Travel Type'] == 'Car' else row['Flight Cost ($)'],
    axis=1
)

# Lodging and food cost
df['Lodging Cost ($)'] = df['Lodging per Night ($)'] * (df['Trip Length (days)'] - 1)
df['Food & Drinks Cost ($)'] = df['Food & Drinks per Day ($)'] * df['Trip Length (days)']

# Total cost
df['Total Cost ($)'] = df['Transport Cost ($)'] + df['Lodging Cost ($)'] + df['Food & Drinks Cost ($)'] + df['Activities ($)']

# Save to Excel
df_final = df[[
    'Destination', 'Travel Type', 'Transport Cost ($)', 'Lodging Cost ($)',
    'Food & Drinks Cost ($)', 'Activities ($)', 'Total Cost ($)'
]]
df_final.to_excel('Weekend_Travel_Planner.xlsx', index=False)
