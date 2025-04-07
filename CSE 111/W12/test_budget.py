import pytest
from budget import calculate_monthly_budget, calculate_savings_goal, calculate_emergency_fund

def test_calculate_monthly_budget():
    """Test the calculate_monthly_budget function."""
    # Test case 1: Normal case
    assert calculate_monthly_budget(5000, 3000) == 2000
    
    # Test case 2: Zero income
    assert calculate_monthly_budget(0, 1000) == -1000
    
    # Test case 3: Equal income and expenses
    assert calculate_monthly_budget(3000, 3000) == 0

def test_calculate_savings_goal():
    """Test the calculate_savings_goal function."""
    # Test case 1: Achievable goal
    can_achieve, monthly_savings = calculate_savings_goal(1000, 5000, 5)
    assert can_achieve == True
    assert monthly_savings == 1000
    
    # Test case 2: Unachievable goal
    can_achieve, monthly_savings = calculate_savings_goal(500, 5000, 5)
    assert can_achieve == False
    assert monthly_savings == 1000
    
    # Test case 3: Zero months
    with pytest.raises(ZeroDivisionError):
        calculate_savings_goal(1000, 5000, 0)

def test_calculate_emergency_fund():
    """Test the calculate_emergency_fund function."""
    # Test case 1: Normal case
    assert calculate_emergency_fund(2000, 6) == 12000
    
    # Test case 2: Zero expenses
    assert calculate_emergency_fund(0, 6) == 0
    
    # Test case 3: Different number of months
    assert calculate_emergency_fund(2000, 3) == 6000 