# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
#from .stationdata import build_station_list  
# attempted alternative to haversine... ((stations(2,0)-p(0))**2 + (stations(2,1)-p(1))**2)**1/2
#haversine(stations.coord,p)
#from dis import _HaveCodeOrStringType
#  # convert decimal degrees to radians 
#        lon1, lat1, lon2, lat2 = map(radians, [station.coord(0), station.coord(1), p(0), p(1)])
#        # haversine formula 
#        dlon = lon2 - lon1 
#        dlat = lat2 - lat1 
#        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
#        c = 2 * asin(sqrt(a))
#        distance = 2*6371*c # where 6371 is the radius of the earth
from .utils import sorted_by_key  # noqa
from .station import MonitoringStation
from math import radians, cos, sin, asin, sqrt
from haversine import haversine

#task 1B
def stations_by_distance(stations,p):
    station_name_distance = {}
    for station in stations:
        distance = haversine(station.coord,p)
        station_name_distance.append(station.station_id, distance)
    sorted_by_key(station_name_distance,1)
    return station_name_distance


#task 1C
def stations_within_radius(stations, centre, r):
    distance = stations_by_distance(stations,centre)
    stations_in = []
    for station in distance:
        if station.distance <= r:
            stations_in.append(stations.station_id)
        else:
            continue
    return stations_in

# Task 1D
def rivers_with_station(stations):
    river_list = []
    all_rivers = [stations[3]]
    for i in all_rivers:
        if all_rivers[i] in river_list:
            continue
        else:
            river_list.append(all_rivers[i])
    return river_list


#def stations_by_river(stations):
    river_dict = {}
    for i in stations:
        if stations.river not in river_dict:
            river_dict[station.river] = [station.name]
        else:
            river_dict[station.river].append(station.name)
            river_dict[station.river].sort()
    return river_dict

