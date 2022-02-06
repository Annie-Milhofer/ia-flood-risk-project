# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
#from .stationdata import build_station_list  
#from dis import _HaveCodeOrStringType
#from haversine import haversine, Unit

from .utils import sorted_by_key  # noqa
from .station import MonitoringStation
from math import radians, cos, sin, asin, sqrt

#imported haversine by copying code across
def haversine(lat1, lon1, lat2, lon2):
    R = 6372.8  # Earth radius in kilometers
    dLat = radians(lat2 - lat1)
    dLon = radians(lon2 - lon1)
    lat1 = radians(lat1)
    lat2 = radians(lat2)
    a = sin(dLat / 2)**2 + cos(lat1) * cos(lat2) * sin(dLon / 2)**2
    c = 2 * asin(sqrt(a))
    return R * c

# Task 1B
def stations_by_distance(stations,p):
    names = []
    distances = []
    for station in stations:
        distance = haversine(station.coord[0],station.coord[1],p[0],p[1])
        names.append(station.name)
        distances.append(distance)
    
    station_name_distance = list(zip(names,distances))
    station_name_distance.sort(key = lambda tup: tup[1])
    return station_name_distance


# Task 1C
def stations_within_radius(stations, centre, r):
    distance = stations_by_distance(stations,centre)
    stations_in = []
    for station in distance:
        if station[1] <= r:
            stations_in.append(station[0])
        else:
            continue
    return stations_in

# Task 1D part 1
def rivers_with_station(stations):
    river_list = []
    all_rivers = [stations[3]]
    for i in all_rivers:
        if all_rivers[i] in river_list:
            continue
        else:
            river_list.append(all_rivers[i])
    return river_list

# Task 1D part 2
def stations_by_river(stations):
    river_dict = {}
    for station in stations:
        if stations.river not in river_dict:
            river_dict[station.river] = [station.name]
        else:
            river_dict[station.river].append(station.name)
            river_dict[station.river].sort()
    return river_dict