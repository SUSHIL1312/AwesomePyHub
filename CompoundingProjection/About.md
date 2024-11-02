
# Future Value Calculator for Growing Monthly Investments

## Overview
This program calculates the future value of a monthly investment with an annual increment, taking into account compound growth (CAGR). It allows users to input the initial monthly investment, an annual increment percentage, the investment duration, and estimated CAGR rates. The program then projects the potential total investment value at the end of the specified period, using both a low and high CAGR estimate.

## Features
- **Flexible Inputs**: Allows users to define the initial monthly investment, the annual increment as a percentage, the investment period in years, and custom CAGR estimates.
- **Dynamic Growth Calculation**: Calculates future value by compounding monthly investments over the entire period.
- **Two Growth Estimates**: Provides projections based on two different CAGR values, enabling users to assess both conservative and optimistic growth scenarios.

## How It Works
The program calculates the projected value of monthly contributions that increase each year by a specified percentage. It uses compounding to estimate how much each monthly investment will grow over the remaining period and adds up these values to provide an estimated final investment value.

## Use Cases
This tool is useful for:
- **Financial Planning**: Helps individuals estimate the future value of their investment plans with an annual increment, such as SIPs (Systematic Investment Plans).
- **Goal-Based Investment Analysis**: Allows investors to understand potential outcomes based on different CAGR rates, useful for setting realistic financial goals.
- **Retirement Planning**: Enables users to estimate long-term growth of retirement savings when monthly contributions grow over time.

## Input Parameters
- **Initial Monthly Investment**: The amount you plan to invest monthly at the beginning of the investment period.
- **Annual Increment Percentage**: The percentage increase in monthly investment each year.
- **Investment Duration (in years)**: The total duration of the investment period.
- **CAGR Low Estimate**: Lower bound estimate for Compound Annual Growth Rate.
- **CAGR High Estimate**: Upper bound estimate for Compound Annual Growth Rate.
- **Months Per Year**: The number of months per year, typically 12.

## Example
Assume:
- Initial Monthly Investment: 45,000 INR
- Annual Increment Percentage: 10%
- Investment Duration: 6 years
- CAGR Low Estimate: 20% 
- CAGR High Estimate: 22% 

Running the program with these inputs will provide the estimated total investment values under both the 20% and 22% CAGR scenarios.

## Getting Started
1. Clone this repository to your local machine.
2. Run the Python file in a terminal or Python environment.
3. Enter your parameters when prompted.

## Requirements
- Python 3.x

## Example Usage
```plaintext
Enter the initial monthly investment (in INR): 45000
Enter the annual increment percentage: 10
Enter the duration of investment in years: 6
Enter the low estimate of CAGR (as a decimal, e.g., 20 for 20%): 20
Enter the high estimate of CAGR (as a decimal, e.g., 22 for 22%): 22

```

Output:
```plaintext
Total investment value at 20.0% CAGR: 1234567.89 INR
Total investment value at 22.0% CAGR: 1345678.90 INR
```


