import pytest
from datetime import time
from byui_chickfila_wait import (
    get_base_wait_time,
    add_random_variation,
    calculate_wait_time,
    format_wait_time
)

def test_get_base_wait_time():
    """Test the base wait time calculation function."""
    # Test peak time (12:00 PM)
    peak_time = time(12, 0)
    assert get_base_wait_time(peak_time) == 15
    
    # Test before peak time (11:00 AM)
    before_peak = time(11, 0)
    assert get_base_wait_time(before_peak) == 10
    
    # Test after peak time (2:00 PM)
    after_peak = time(14, 0)
    assert get_base_wait_time(after_peak) == 10
    
    # Test 30 minutes before peak (11:00 AM)
    near_peak_start = time(11, 0)
    assert get_base_wait_time(near_peak_start) == 10
    
    # Test 30 minutes after peak (2:00 PM)
    near_peak_end = time(14, 0)
    assert get_base_wait_time(near_peak_end) == 10

def test_add_random_variation():
    """Test the random variation function."""
    base_time = 10
    # Test multiple times to ensure variation works
    variations = [add_random_variation(base_time) for _ in range(10)]
    
    # Check that all variations are within expected range
    assert all(7 <= v <= 13 for v in variations)
    # Check that minimum wait time is 5 minutes
    assert all(v >= 5 for v in variations)

def test_format_wait_time():
    """Test the wait time formatting function."""
    assert format_wait_time(30) == "30 minutes"
    assert format_wait_time(60) == "1 hour"
    assert format_wait_time(90) == "1 hour and 30 minutes"
    assert format_wait_time(120) == "2 hours"
    assert format_wait_time(150) == "2 hours and 30 minutes"

def test_calculate_wait_time():
    """Test the main wait time calculation function."""
    wait_time, breakdown = calculate_wait_time()
    assert isinstance(wait_time, int)
    assert wait_time >= 5
    assert "Base time" in breakdown
    assert "Random variation" in breakdown 