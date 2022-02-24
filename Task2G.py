#How much does the average water level deviates from High bound (assessed by typical bound range)
#The trend of the water level

from floodsystem.analysis import polyfit_coeff
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.station import MonitoringStation
from datetime import timedelta

def _linear_regression(station):
    dates, levels = fetch_measure_levels(station.measure_id, dt=timedelta(days=2))
    p_coeff = polyfit_coeff(dates, levels, 1)
    #print("p_coeff for station", station.name, p_coeff[0])
    return p_coeff[0]

def risk_assessment(station):
    value = MonitoringStation.relative_water_level(station)
    if value == None:
        return None
    elif MonitoringStation.typical_range_consistent(station) == False:
        return None
    return _linear_regression(station) + value

def risk_categorization(risk_lev):
    if risk_lev < 0.4:
        return "low"
    elif risk_lev < 0.8:
        return "moderate"
    elif risk_lev < 1.2:
        return "high"
    else:
        return "severe"

def run():
    """Requirements for Task 2G"""
    
    # Build list of stations over relative water level threshold 0.4
    stations = build_station_list()
    update_water_levels(stations)
    list = stations_level_over_threshold(stations, 0.4)
    sorted_stations = [n[0] for n in list]

    # Sort current stations by risk_assessment function in descending order
    risk_assess_sorted_stations = sorted(sorted_stations, key = risk_assessment, reverse = True)

    #return conclusions
    print("Total number of stations over flood warning threshold:", len(list), "\n")
    for station in risk_assess_sorted_stations:
        risk_lev = risk_assessment(station)
        print("Station name:", station.name, "\n risk level factor:", risk_lev, "\n flood likelihood:", risk_categorization(risk_lev), "\n")
    

if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()


