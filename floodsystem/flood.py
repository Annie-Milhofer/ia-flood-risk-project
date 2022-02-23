from .station import MonitoringStation
#from .utils import sorted_by_key
#task 2B
def stations_level_over_threshold(stations, tol):
    """returns a list of the stations with a flood risk over the tolerance"""
    station_name = []
    water_level = []
    for station in stations:
        value = MonitoringStation.relative_water_level(station)
        if value == None:
            break
        elif value >= 0.8:
            station_name.append(station.name)
            water_level.append(value)
    
    station_flood_risk = list(zip(station_name,water_level))
    station_flood_risk.sort(key = lambda tup:tup[1])
    return station_flood_risk

#task 2C
def stations_highest_rel_level(stations, N):
    """N stations with highest relative water levels"""
    station_name = []
    water_level = []
    for station in stations:
        if station.latest_level == None:
            break
        elif MonitoringStation.typical_range_consistent(station) == False:
            break
        elif station.latest_level >= 100:
            break
        else:
            station_name.append(station.name)
            water_level.append(MonitoringStation.relative_water_level(station))
    
    station_flood_risk = list(zip(station_name,water_level))
    station_flood_risk.sort(key = lambda tup:tup[1])
    return station_flood_risk