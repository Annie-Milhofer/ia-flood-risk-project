# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""

#from .stationdata import update_water_levels

class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d

    # Task 1F
    def typical_range_consistent(self):
        if not isinstance(self.typical_range, tuple):
            return False
        low, high = self.typical_range
        if low == None or high == None or high - low < 0:
            return False
        else:
            return True

    #Task 2B
    def relative_water_level(self):
        if self.typical_range_consistent() == True:
            # Set up relative water level
            if self.latest_level != None:
                relative_level = (self.latest_level - self.typical_range[0])/(self.typical_range[1] - self.typical_range[0])
            else:
                relative_level = None
            return relative_level 
        else:
            return None

#Task 1F part 2
def inconsistent_typical_range_stations(stations):
    list = []
    for station in stations:
        if MonitoringStation.typical_range_consistent(station) == False:
            list.append(station.name)
    list.sort()
    return list