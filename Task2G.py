#How much does the average water level deviates from High bound (assessed by typical bound range)
#The trend of the water level

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level_mod
from floodsystem.datafetcher import fetch_measure_levels
from datetime import timedelta


def run():
    """Requirements for Task 2G"""
    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)
    list = stations_level_over_threshold(stations, 0)
    print(len(list))
    print(list)

if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()

def check_list():
    stations = build_station_list()
    update_water_levels(stations)
    list = stations_level_over_threshold(stations, 0)
    print(len(list))
    print(list)

def check_poly_fit():
    stations = build_station_list()
    update_water_levels(stations)
    high_risk_stations_list = stations_highest_rel_level_mod(stations, 40)
    for station_list in high_risk_stations_list:
        station = station_list[0]
        dates, levels = fetch_measure_levels(station.measure_id, dt=timedelta(days=2))
        #plot water level without typical range
        plot_water_level_with_fit(station, dates, levels, 4)
        #plot water level with typical range
        plot_water_level_with_fit(station, dates, levels, 4, show_high_low_range=True, dot_like_original_data=False)