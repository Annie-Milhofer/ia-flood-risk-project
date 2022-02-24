from floodsystem.plot import plot_water_level_with_fit
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level_mod
from floodsystem.datafetcher import fetch_measure_levels
from datetime import timedelta

def run():
    """Requirements for Task 2F"""
    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)
    high_risk_stations_list = stations_highest_rel_level_mod(stations, 5)
    for station_list in high_risk_stations_list:
        station = station_list[0]
        dates, levels = fetch_measure_levels(station.measure_id, dt=timedelta(days=2))
        plot_water_level_with_fit(station, dates, levels, 4)
        plot_water_level_with_fit(station, dates, levels, 4, show_high_low_range=True, dot_like_original_data=False)

if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()