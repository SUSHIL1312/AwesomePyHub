# Function to calculate future value of an increasing monthly investment
def calculate_future_value(cagr, initial_investment, annual_increment_percent, years, months_per_year):
    total_value = 0
    for year in range(1, years + 1):
        # Calculate the monthly investment for the current year
        monthly_investment = initial_investment * (1 + annual_increment_percent / 100) ** (year - 1)
        for month in range(months_per_year):
            # Calculate future value of each monthly investment
            time_remaining = years - (year - 1) - (month / months_per_year)
            future_value = monthly_investment * (1 + cagr / months_per_year) ** (time_remaining * months_per_year)
            total_value += future_value
    return total_value

# Inputs (variables)
initial_investment = float(input("Enter the initial monthly investment (in INR): "))
annual_increment_percent = float(input("Enter the annual increment percentage: "))
years = int(input("Enter the duration of investment in years: "))
cagr_low = float(input("Enter the low estimate of CAGR (20 for 20%): "))/100
cagr_high = float(input("Enter the high estimate of CAGR (22 for 22%): "))/100  
months_per_year = 12

# Calculate the total value for both low and high CAGR estimates
total_value_low = calculate_future_value(cagr_low, initial_investment, annual_increment_percent, years, months_per_year)
total_value_high = calculate_future_value(cagr_high, initial_investment, annual_increment_percent, years, months_per_year)

# Display the results
print(f"Total investment Corpus value at {cagr_low * 100}% CAGR: {total_value_low:.2f} INR")
print(f"Total investment Coupus value at {cagr_high * 100}% CAGR: {total_value_high:.2f} INR")
