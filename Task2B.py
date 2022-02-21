from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation 
def run():
    """Requirements for Task 2B"""
    # Build list of stations
    stations = build_station_list()
    names = []
    river_level = []
    for station in stations:
        if MonitoringStation.relative_water_level(station) >= 0.8:
            names.append(station.name)
            river_level.append(MonitoringStation.relative_water_level(station))
        river_name_level = list(zip(names,river_level))
    print(river_name_level)


if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()
