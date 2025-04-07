import pytest
from winter_navigator import (
    calculate_commute_time,
    find_safe_routes,
    get_parking_recommendations,
    get_winter_preparation_checklist,
    get_weather_data
)

def test_calculate_commute_time():
    """Test that commute times are calculated correctly."""
    # Test each weather condition with 1 mile distance
    assert calculate_commute_time(1.0, 'clear') == 7
    assert calculate_commute_time(1.0, 'snow') == 13
    assert calculate_commute_time(1.0, 'ice') == 14
    assert calculate_commute_time(1.0, 'blizzard') == 21

def test_find_safe_routes():
    """Test that safe routes are found correctly."""
    # Test MC to Hart route
    routes = find_safe_routes('MC', 'Hart', 'clear')
    assert len(routes) == 3  # Should have 3 routes in clear weather
    
    routes = find_safe_routes('MC', 'Hart', 'snow')
    assert len(routes) == 2  # Should only have sheltered routes in snow

def test_get_parking_recommendations():
    """Test that parking recommendations are correct."""
    # Test morning parking
    morning_lots = get_parking_recommendations('clear', 'morning')
    assert 'MC Lot' in morning_lots
    assert 'Hart Lot' in morning_lots
    
    # Test evening parking
    evening_lots = get_parking_recommendations('snow', 'evening')
    assert 'Library Lot' in evening_lots

def test_get_winter_preparation_checklist():
    """Test that winter preparation checklist is correct."""
    # Test basic items are always included
    clear_list = get_winter_preparation_checklist('clear')
    assert "Wear warm winter coat" in clear_list
    assert "Bring gloves and hat" in clear_list
    
    # Test snow adds correct items
    snow_list = get_winter_preparation_checklist('snow')
    assert "Bring snow scraper" in snow_list
    
    # Test blizzard adds emergency kit
    blizzard_list = get_winter_preparation_checklist('blizzard')
    assert "Bring emergency kit" in blizzard_list

def test_get_weather_data():
    """Test that weather data has required information."""
    weather = get_weather_data()
    # Check that all required weather info is present
    assert weather['condition'] == 'snow'
    assert weather['temperature'] == 25
    assert weather['wind_speed'] == 15

    if __name__ == "__main__":
        pytest.main(["-v", __file__])

    pytest.main(["-v"])