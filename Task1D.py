from floodsystem.geo import stations_by_river, rivers_with_station
from floodsystem.stationdata import build_station_list


def run():
    """Requirements for Task 1D"""
    # Build list of stations
    stations = build_station_list()
    #part a
    river_list = rivers_with_station(stations)
    river_list.sort()
    print(len(river_list))
    print(river_list[:10])
    #part b
    station_list = stations_by_river(stations)
    print(station_list["River Aire"])
    print(station_list["River Cam"])
    print(station_list["River Thames"])
    #need to print specific rivers by referencing the 


if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()
