
import pandas as pd
import matplotlib.pyplot as plt

# Cost of living data
data = {
    'City': [
        'Lisbon', 'Barcelona', 'Bangkok', 'Chiang Mai', 'Medellín', 'Mexico City',
        'Tbilisi', 'Canggu', 'Buenos Aires', 'Prague', 'Cape Town', 'Tallinn'
    ],
    'Rent ($)': [1000, 1100, 600, 500, 550, 700, 450, 650, 500, 900, 700, 950],
    'Food ($)': [400, 450, 250, 200, 300, 350, 250, 300, 275, 400, 350, 425],
    'Coworking ($)': [200, 220, 150, 120, 130, 150, 110, 150, 140, 200, 180, 210],
    'Internet ($)': [50, 45, 30, 25, 35, 40, 20, 30, 30, 45, 40, 50],
    'Transport ($)': [80, 90, 60, 40, 50, 70, 40, 50, 50, 85, 70, 90],
    'Lifestyle ($)': [300, 350, 200, 180, 220, 250, 180, 220, 200, 300, 270, 320]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate total monthly cost
df['Total Monthly Cost ($)'] = df.iloc[:, 1:].sum(axis=1)

# Save to Excel
df.to_excel('Digital_Nomad_Cost_Comparison.xlsx', index=False)

# Create and save bar chart
plt.figure(figsize=(10, 6))
plt.bar(df['City'], df['Total Monthly Cost ($)'], color='skyblue')
plt.title('Total Monthly Cost of Living for Digital Nomads')
plt.xlabel('City')
plt.ylabel('Total Monthly Cost ($)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('Nomad_Cost_Comparison_Chart.png')
plt.show()
