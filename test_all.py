from floodsystem.geo import stations_by_distance, haversine, stations_within_radius, rivers_with_station, stations_by_river, rivers_by_station_number
from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations


def tests():
    """Tests for Task 1 function"""

    #Task 1B - create 2 stations
    station_id = "Test station_id"
    measure_id = "Test measure_id"
    typical_range = (0, 1)
    river = "Test river"
    town = "Test Town"
    station1 = MonitoringStation(station_id, measure_id, "Station A", (53.2053, 0.1218), typical_range, river, town)
    station2 = MonitoringStation(station_id, measure_id, "Station B", (53.2053, 10.1218), typical_range, river, town)

    stations = [station1, station2]
    p = (52.2053, 0.1218)
    centre = (52.2053, 0.1218)
    r = 10
    dist1 = haversine(p[0], p[1], 53.2053, 0.1218)
    dist2 = haversine(p[0], p[1], 53.2053, 10.1218)

    list1 = stations_by_distance(stations, p)
    assert list1 == [("Station A", dist1), ("Station B", dist2)]

    #Task 1C - create 2 stations
    station_id = "Test station_id"
    measure_id = "Test measure_id"
    typical_range = (1.0, 2.0)
    river = "Test river"
    town = "Test Town"
    station1 = MonitoringStation(station_id, measure_id, "Station A", (52.2053, 0.1218), typical_range, river, town)
    station2 = MonitoringStation(station_id, measure_id, "Station B", (52.2053, 10.1218), typical_range, river, town)

    stations = [station1, station2]
    centre = (52.2053, 0.1218)
    r = 10

    list1 = stations_within_radius(stations, centre, r)

    assert list1 == ["Station A"]

    #Tasks 1D & E - create 4 test stations
    station_id = "Test station_id"
    measure_id = "Test measure_id"
    river = "Test river"
    coord = (0.0, 0.0)
    town = "Test Town"
    typical_range = (0, 1)
    station1 = MonitoringStation(station_id, measure_id, "Station A", (0, 0), typical_range, "River A", town)
    station2 = MonitoringStation(station_id, measure_id, "Station B", (0, 1), typical_range, "River A", town)
    station3 = MonitoringStation(station_id, measure_id, "Station C", (0, 2), typical_range, "River B", town)
    station4 = MonitoringStation(station_id, measure_id, "Station D", (0, 3), typical_range, "River C", town)

    test = rivers_with_station([station3, station2, station1, station4])

    assert test == ["River A", "River B", "River C"]

    test2 = stations_by_river([station3, station2, station1, station4])
 
    assert test2["River A"] == ["Station A", "Station B"]
    assert test2["River B"] == ["Station C"]
    assert test2["River C"] == ["Station D"]

    x = rivers_by_station_number([station1, station2, station3, station4], 1)
    y = rivers_by_station_number([station1, station2, station3, station4], 2)

    #test for N = 1, return most number of stations: A with 2
    assert x == [("River A", 2)]
    #test for N = 2, return most number of stations: A, B and C since they have the same number of stations
    assert y == [("River A", 2), ("River B", 1), ("River C", 1)]

    #Task 1F - create 3 test stations
    station_id = "Test station_id"
    measure_id = "Test measure_id"
    river = "Test river"
    coord = (0.0, 0.0)
    town = "Test Town"
    station1 = MonitoringStation(station_id, measure_id, "Station A", coord, (0.0, 1.0), river, town)
    station2 = MonitoringStation(station_id, measure_id, "Station B", coord, (1.0, 0.0), river, town)
    station3 = MonitoringStation(station_id, measure_id, "Station C", coord, (0), river, town)
    station4 = MonitoringStation(station_id, measure_id, "Station D", coord, "string", river, town)

    test = inconsistent_typical_range_stations([station1, station2, station3, station4])

    #test for inconsistent typical ranges: 
    #A is consistent
    #B is inconsistent as typical_range[0]>typical_range
    #C is inconsistent as it only has one item in typical_range tuple
    #D is inconsistent as it its typical_range is a string not a tuple
    assert test == ["Station B", "Station C", "Station D"]

print(tests())