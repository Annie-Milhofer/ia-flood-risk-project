# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

#from stationdata import build_station_list
from .utils import sorted_by_key  # noqa
#from dis import _HaveCodeOrStringType

def stations_by_distance(stations,p):
    from utils import sorted_by_key
    stations_distance = [stations.name,haversine(stations.coord,p)]
    sorted_by_key(stations_distance,1)
    return stations_distance

