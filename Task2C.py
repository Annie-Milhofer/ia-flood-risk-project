from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import MonitoringStation 
from floodsystem.flood import stations_highest_rel_level
def run():
    """Requirements for Task 2C"""
    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)
    high_risk_stations = stations_highest_rel_level(stations, 10)

    print(high_risk_stations)


if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()