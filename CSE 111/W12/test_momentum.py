import pytest
from momentum import *

@pytest.fixture
def clear_workouts():
    """Clear the global workouts list before each test."""
    global workouts
    workouts = []
    return True

def test_add_workout(clear_workouts):
    """Test adding a workout entry."""
    date = datetime(2025, 3, 18)
    result = add_workout(date, "Bench Press", 3, 10, 135)
    assert result is True
    assert len(workouts) == 1
    assert "bench press" in workouts[0]
    assert "135" in workouts[0]

def test_get_personal_best(clear_workouts):
    """Test personal best calculation."""
    date1 = datetime(2025, 3, 18)
    date2 = datetime(2025, 3, 19)
    add_workout(date1, "Squat", 3, 10, 185)
    add_workout(date2, "Squat", 3, 8, 205)
    pb = get_personal_best("Squat")
    assert pb == 205