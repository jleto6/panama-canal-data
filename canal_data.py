#!/usr/bin/env python3

def main():
    
    ship_size = int(input("Ship Tonnage: "))
    lock_type = input("Lock Type (Panamax or Neopanamax): ").lower()

    if (lock_type == "panamax"):
        current_type = 0
        print("Panamax")
    elif (lock_type == "neopanamax"):
        current_type = 1
        print("Neopanamax")

    cost_per_gallon = 0.0002
    panamax_volume = 50,000,000
    neopanamax_volume = 38,000,000

    # Amount of water a ship will displace based on tonnage
    water_displaced = ship_size * 240 #one ton displaces approximately 240 gallons of water

    # Using a panamax lock
    if (current_type == 0):
        handle_panamax()

    # Using a panamax lock
    if (current_type == 1):
        handle_neopanamax()

def handle_panamax():
    print("working on panamx")

def handle_neopanamax():
    print("working on neopanamx")

if __name__ == "__main__":
    main()