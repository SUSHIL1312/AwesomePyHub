def calculate_years(initial_investment, current_corpus, annual_increase_percent, cagr, target_amount):
    # Convert CAGR percentage to a decimal
    cagr_decimal = cagr / 100.0
    annual_increase_decimal = annual_increase_percent / 100.0
    
    # Initial values
    total_amount = current_corpus
    investment = initial_investment
    years = 0
    total_invested = current_corpus  # Keep track of the total amount invested

    # Iterate until the total amount reaches or exceeds the target amount
    while total_amount < target_amount:
        # Add the current year's total investment to the corpus
        total_amount += investment * 12  # Convert monthly investment to yearly
        total_invested += investment * 12  # Update total invested
        
        # Apply CAGR to grow the total amount for the next year
        total_amount *= (1 + cagr_decimal)
        
        # Increase investment by the annual increase percentage for the next year
        investment *= (1 + annual_increase_decimal)
        
        # Increment year counter
        years += 1

    return years, total_invested

# Take user inputs
initial_investment = float(input("Enter the initial monthly investment amount (in INR): "))
current_corpus = float(input("Enter the current corpus size (in INR): "))
annual_increase_percent = float(input("Enter the annual increase in investment amount (in %): "))
cagr = float(input("Enter the CAGR expected (in %): "))
target_amount = float(input("Enter the target amount to achieve (in INR): "))

# Calculate the number of years required and total amount invested
years_required, total_invested = calculate_years(initial_investment, current_corpus, annual_increase_percent, cagr, target_amount)

print(f"You will need approximately {years_required} years to achieve the target amount.")
print(f"Total amount invested over these years: {total_invested:.2f} INR.")
