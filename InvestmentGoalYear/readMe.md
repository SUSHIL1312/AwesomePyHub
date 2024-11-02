
# Investment Goal Years Calculator

## Overview
The Investment Goal Years Calculator is a Python program designed to help individuals estimate the number of years required to reach a specific financial target through regular monthly investments that increase annually. This program considers both the initial investment, the current corpus, and the expected growth rate of the investments, allowing users to make informed decisions about their financial planning.

## Features
- **User-Friendly Interface**: The program prompts users for necessary inputs, making it easy to understand and operate.
- **Dynamic Growth Calculation**: Automatically adjusts the investment amount each year based on the specified percentage increase.
- **Compound Growth Estimation**: Utilizes the Compound Annual Growth Rate (CAGR) to estimate the future value of investments.
- **Target Achievement Calculation**: Accurately calculates the number of years required to meet a financial goal.
- **Total Investment Calculation**: Provides the total amount invested over the years until the target is achieved.

## How It Works
The program calculates the years required to achieve a specified target amount by:
1. **Adding Annual Contributions**: It adds the annual investment contributions to the current corpus.
2. **Compounding Growth**: It applies the expected CAGR to the total amount at the end of each year.
3. **Incremental Investments**: It increases the monthly investment amount by a specified percentage annually.
4. **Yearly Loop**: Continues this process until the total amount reaches or exceeds the target amount.
5. **Investment Tracking**: Tracks the total amount invested throughout the investment period.

## Use Cases
This tool is useful for:
- **Financial Planning**: Helps users understand how long it will take to achieve specific savings goals.
- **Retirement Planning**: Assists individuals in determining how their investments will grow over time, helping them plan for retirement.
- **Investment Strategy Assessment**: Enables users to experiment with different investment amounts, growth rates, and increments to see how these factors affect their time to reach financial goals.

## Input Parameters
- **Initial Monthly Investment**: The amount of money invested monthly (in INR).
- **Current Corpus Size**: The existing amount of money already saved or invested (in INR).
- **Annual Increase in Investment Amount**: The percentage by which the monthly investment will increase each year.
- **Expected CAGR**: The anticipated compound annual growth rate for the investments (in %).
- **Target Amount to Achieve**: The financial goal users want to reach (in INR).

## Example
### Inputs
- **Initial Monthly Investment**: 10,000 INR
- **Current Corpus Size**: 200,000 INR
- **Annual Increase in Investment Amount**: 5%
- **Expected CAGR**: 7%
- **Target Amount to Achieve**: 1,000,000 INR

### Running the Program
```plaintext
Enter the initial monthly investment amount (in INR): 10000
Enter the current corpus size (in INR): 200000
Enter the annual increase in investment amount (in %): 5
Enter the CAGR expected (in %): 7
Enter the target amount to achieve (in INR): 1000000
```

### Output
```plaintext
You will need approximately 7 years to achieve the target amount.
Total amount invested over these years: 820000.00 INR.
```

## Getting Started
1. **Clone the Repository**: Download or clone this repository to your local machine.
  
2. **Run the Program**: Execute the Python script in your terminal or preferred Python environment.
   ```bash
   python investment_goal_calculator.py
   ```
3. **Input Parameters**: Follow the prompts to enter your parameters.

## Requirements
- **Python**: This program requires Python 3.x to run. Ensure you have it installed on your system.

## Contributing
Contributions are welcome! If you have suggestions for improvements or additional features, feel free to submit a pull request or open an issue.

