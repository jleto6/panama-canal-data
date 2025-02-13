# Constants
cost_per_gallon = 0.0002
transits_per_year = 14000

# Lock Data
LOCKS = {
    "panamax": {
        "lock_name": "Panamax",
        "lock_volume": 50_000_000,
        "water_lost": 100
    },
    "neopanamax": {
        "lock_name": "Neopanamax",
        "lock_volume": 38_000_000,
        "water_lost": 55
    }
}

def analyze_transit(ship_size: int, lock_type: str) -> dict:
    lock_data = LOCKS[lock_type.lower()]
    
    water_displaced = ship_size * 240 # Approx. gallons displaced per ton based on water weight (1 ton ≈ 240 gal of freshwater)
    water_needed = lock_data['lock_volume'] - water_displaced
    water_lost = water_needed * (lock_data['water_lost'] / 100)
    cost_per_lock = water_needed * cost_per_gallon
    percent_savings = (water_displaced / lock_data['lock_volume']) * 100

    return {
        "lock_type": lock_data['lock_name'],
        "ship_size": ship_size,
        "water_displaced": water_displaced,
        "water_needed": water_needed,
        "water_lost": water_lost,
        "cost_per_lock": cost_per_lock,
        "percent_savings": percent_savings,
        "annual_water_displaced": water_displaced * 6 * transits_per_year
    }