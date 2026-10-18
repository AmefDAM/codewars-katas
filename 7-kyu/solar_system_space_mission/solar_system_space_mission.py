from preloaded import fuel_map

def successful_mission(solar_system, destination_planet, fuel):
    cost = 0
    if solar_system.index("Earth") < solar_system.index(destination_planet):
        for planet in range(solar_system.index("Earth") +1, solar_system.index(destination_planet) + 1, 1):
            cost += fuel_map[solar_system[planet]]
    elif solar_system.index("Earth") > solar_system.index(destination_planet):
        for planet in range(solar_system.index("Earth") -1, solar_system.index(destination_planet) - 1, -1):
            cost += fuel_map[solar_system[planet]]
    cost += fuel_map[destination_planet]
    return fuel >= cost