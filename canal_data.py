# Constants
cost_per_gallon = 0.0002
transits_per_year = 14000

# Lock Data
LOCKS = {
    "panamax": {
        "lock_name": "Panamax", # Name of lock type
        "lock_volume": 50_000_000, # Gallons the lock chamber holds when full
        "water_lost": 100 # Percent of water lost due to not being recycled (e.g. flushed out to sea)
    },
    "neopanamax": {
        "lock_name": "Neopanamax", # Name of lock type
        "lock_volume": 38_000_000, # Percent of water lost due to not being recycled (e.g. flushed out to sea)
        "water_lost": 55 # Percent of water lost due to not being recycled (e.g. flushed out to sea)

    }
}

def analyze_transit(ship_size: int, lock_type: str) -> dict:
    """
    Estimates water usage and cost metrics for a given ship transit.

    Args:
        ship_size (int): Ship weight in tons.
        lock_type (str): Type of lock ("panamax" or "neopanamax").

    Returns:
        dict: Contains water displaced, water needed, water lost,
              cost per transit, percent savings, and annual displacement estimate.

    Notes:
        Assumes each ton displaces ~240 gallons of freshwater.
        Water lost is based on non-recyclable water percentage per lock type.
    """
    lock_data = LOCKS[lock_type.lower()]
    
    water_displaced = ship_size * 240 # Approx. gallons displaced per ton based on water weight (1 ton ≈ 240 gal of freshwater)
    water_needed = lock_data['lock_volume'] - water_displaced # Water needed after subtracting what the ship already displaced
    water_lost = water_needed * (lock_data['water_lost'] / 100) # Loss from non-recycled water
    cost_per_lock = water_needed * cost_per_gallon # Total water cost per lock
    percent_savings = (water_displaced / lock_data['lock_volume']) * 100 # % of lock volume saved by displacement

# Return summary metrics as a dictionary
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