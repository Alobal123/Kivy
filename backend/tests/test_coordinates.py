from backend.coordinates import Coordinates


def test_distance():
    point_1 = Coordinates(50.0833439, 14.4249247)
    point_2 = Coordinates(50.0841942, 14.4237311)
    distance = point_2.distance(point_1)
    print(distance)
    assert (100 < distance < 150)

    point_3 = Coordinates(50.0841306, 14.4238225)
    distance = point_2.distance(point_3)
    print(distance)
    assert (5 < distance < 15)

