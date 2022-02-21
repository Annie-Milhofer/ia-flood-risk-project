from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation 
from flood import stations_highest_rel_level
def run():
    """Requirements for Task 2C"""
    # Build list of stations
    stations = build_station_list()
    high_risk_stations = stations_highest_rel_level(stations, N)

    print(high_risk_stations)


if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()