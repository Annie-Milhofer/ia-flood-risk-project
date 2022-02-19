from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation 
def run():
    """Requirements for Task 1A"""
    # Build list of stations
    stations = build_station_list()
    river_level = []
    for station in stations:
        river_level.append(MonitoringStation().relative_water_level(station))
    print(river_level)


if __name__ == "__main__":
    print("*** Task 1A: CUED Part IA Flood Warning System ***")
    run()
