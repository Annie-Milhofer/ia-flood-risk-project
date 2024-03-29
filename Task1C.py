from floodsystem import geo
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

def run():
    """Requirements for Task 1C"""

    # Build list of stations
    stations = build_station_list()

    #form list of stations within radius of cambridge centre
    stations_in_radius = stations_within_radius(stations,(52.2053,0.1218), 10)
    stations_in_radius.sort(key = lambda tup : tup[0])
    print(stations_in_radius)

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()