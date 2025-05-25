
import pandas as pd
import matplotlib.pyplot as plt

# Assumptions
starting_users = 2000
monthly_growth = 0.12
churn_rate = 0.05
bookings_per_user = 1.2
booking_fee = 5
marketing_cost_per_user = 0.75
salaries = 5000
tools_cost = 500
starting_cash = 10000
months = 12

# Initialize lists
users = [starting_users]
revenues = []
marketing_costs = []
total_costs = []
net_incomes = []
cash_flows = [starting_cash]

# Simulate monthly data
for month in range(months):
    if month > 0:
        new_users = users[-1] * monthly_growth
        churned = users[-1] * churn_rate
        users.append(users[-1] + new_users - churned)

    bookings = users[-1] * bookings_per_user
    revenue = bookings * booking_fee
    marketing = users[-1] * marketing_cost_per_user
    total_cost = marketing + salaries + tools_cost
    net_income = revenue - total_cost
    cash_flow = cash_flows[-1] + net_income

    revenues.append(revenue)
    marketing_costs.append(marketing)
    total_costs.append(total_cost)
    net_incomes.append(net_income)
    cash_flows.append(cash_flow)

# Create DataFrame
df = pd.DataFrame({
    'Month': range(1, months + 1),
    'Users': users,
    'Revenue ($)': revenues,
    'Marketing Cost ($)': marketing_costs,
    'Total Costs ($)': total_costs,
    'Net Income ($)': net_incomes,
    'Cash Flow ($)': cash_flows[1:]
})

# Plot results
plt.figure(figsize=(10, 6))
plt.plot(df['Month'], df['Revenue ($)'], label='Revenue ($)', marker='o')
plt.plot(df['Month'], df['Total Costs ($)'], label='Total Costs ($)', marker='o')
plt.plot(df['Month'], df['Net Income ($)'], label='Net Income ($)', marker='o')
plt.title('TravelFlex Monthly Financial Forecast')
plt.xlabel('Month')
plt.ylabel('Amount ($)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig('TravelFlex_Forecast_Chart.png')
plt.show()
