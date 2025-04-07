def calculate_monthly_budget(income, expenses):
    """Calculate the monthly budget by subtracting expenses from income.
    
    Args:
        income (float): Monthly income
        expenses (float): Monthly expenses
        
    Returns:
        float: Monthly budget (income - expenses)
    """
    return income - expenses

def calculate_savings_goal(monthly_budget, target_amount, months):
    """Calculate if a savings goal can be achieved within the specified time.
    
    Args:
        monthly_budget (float): Available money per month
        target_amount (float): Amount to save
        months (int): Number of months to save
        
    Returns:
        tuple: (bool, float) - (can_achieve, monthly_savings_needed)
    """
    monthly_savings_needed = target_amount / months
    can_achieve = monthly_savings_needed <= monthly_budget
    return can_achieve, monthly_savings_needed

def calculate_emergency_fund(monthly_expenses, months):
    """Calculate the recommended emergency fund amount.
    
    Args:
        monthly_expenses (float): Monthly expenses
        months (int): Number of months to cover
        
    Returns:
        float: Recommended emergency fund amount
    """
    return monthly_expenses * months

def get_user_input():
    """Get user input for financial calculations.
    
    Returns:
        tuple: (income, expenses, target_amount, months)
    """
    try:
        income = float(input("Enter your monthly income: $"))
        expenses = float(input("Enter your monthly expenses: $"))
        target_amount = float(input("Enter your savings goal: $"))
        months = int(input("Enter number of months to save: "))
        return income, expenses, target_amount, months
    except ValueError:
        print("Please enter valid numbers.")
        return None, None, None, None

def main():
    """Main function to run the personal finance calculator."""
    print("Welcome to the Personal Finance Calculator!")
    print("This program helps you calculate your budget and savings goals.")
    
    income, expenses, target_amount, months = get_user_input()
    if income is None:
        return
    
    # Calculate monthly budget
    monthly_budget = calculate_monthly_budget(income, expenses)
    print(f"\nYour monthly budget is: ${monthly_budget:.2f}")
    
    # Calculate savings goal
    can_achieve, monthly_savings = calculate_savings_goal(monthly_budget, target_amount, months)
    if can_achieve:
        print(f"You can achieve your savings goal! You need to save ${monthly_savings:.2f} per month.")
    else:
        print(f"Your savings goal may be too ambitious. You would need to save ${monthly_savings:.2f} per month.")
    
    # Calculate emergency fund
    emergency_fund = calculate_emergency_fund(expenses, 6)  # 6 months emergency fund
    print(f"\nRecommended emergency fund (6 months of expenses): ${emergency_fund:.2f}")

if __name__ == "__main__":
    main()