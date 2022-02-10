from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list

def run():
    """Requirements for Task 1F"""

    # Build list of stations
    stations = build_station_list()

    print(sorted(inconsistent_typical_range_stations(stations), key = str.lower))
    

if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()

