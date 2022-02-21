from floodsystem.station import MonitoringStation

def stations_level_over_threshold(stations, tol):
    """returns a list of the stations with a flood risk over the tolerance"""
    station_name = []
    water_level = []
    for station in stations:
        if MonitoringStation.relative_water_level(station) > tol:
            station_name.append(station.name)
            water_level.append(MonitoringStation.relative_water_level(station))
    
    station_flood_risk = list(zip(station_name,water_level))
    return station_flood_risk


def stations_highest_rel_level(stations, N):
    """N stations with highest relative water levels"""
    station_name = []
    water_level = []
    for station in stations:
        station_name.append(station.name)
        water_level.append(MonitoringStation.relative_water_level(station))
    
    station_flood_risk = list(zip(station_name,water_level))
    station_flood_risk.sort(key = lambda tup:tup[1])
    return station_flood_risk