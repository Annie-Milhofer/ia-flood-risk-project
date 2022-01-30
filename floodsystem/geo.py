# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
#from .stationdata import build_station_list
#from dis import _HaveCodeOrStringType
from .utils import sorted_by_key  # noqa
from .station import MonitoringStation

#task 1B
def stations_by_distance(stations,p):
    station_name_distance = {}
    for i in stations:
        distance = ((stations(2,0)-p(0))**2 + (stations(2,1)-p(1))**2)**1/2
        station_name_distance.append(stations.station_id, distance)
    
    sorted_by_key(station_name_distance,1)
    return station_name_distance


#task 1C
def stations_within_radius(stations, centre, r):
    station_distance = stations_by_distance(stations,centre)
