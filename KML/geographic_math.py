import math

from cartesian_point import CartesianPoint
import conversions
from geographic_point import GeographicPoint

EARTH_RADIUS_IN_METERS = 6371137.0


def compute_endpoint(origin, bearing, distance):
    angular_distance = distance / EARTH_RADIUS_IN_METERS
    bearing_radians = conversions.degrees_to_radians(bearing)
    lat1 = conversions.degrees_to_radians(origin.latitude)
    lon1 = conversions.degrees_to_radians(origin.longitude)
    radianLat2 = math.asin(math.sin(lat1) * math.cos(angular_distance) +
                           math.cos(lat1) * math.sin(angular_distance) * math.cos(bearing_radians))
    radianLon2 = lon1 + math.atan2(math.sin(bearing_radians) * math.sin(angular_distance) * math.cos(lat1),
                                   math.cos(angular_distance) - math.sin(lat1) * math.sin(radianLat2))
    lat2 = conversions.radians_to_degrees(radianLat2)
    lon2 = conversions.radians_to_degrees(radianLon2)
    return GeographicPoint(lat2, lon2, origin.altitude)


def compute_bearing(start, end):
    if start.equals(end):
        return -1

    lat1 = conversions.degrees_to_radians(start.latitude)
    lat2 = conversions.degrees_to_radians(end.latitude)
    dlon = conversions.degrees_to_radians(end.longitude - start.longitude)
    y = math.sin(dlon) * math.cos(lat2)
    x = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(dlon)
    theta = math.atan2(y, x)
    theta = conversions.radians_to_degrees(theta)
    theta += 360.0
    while theta > 360.0:
        theta -= 360.0
    return theta


def compute_distance(start, end):
    if start.equals(end):
        return 0
    lat1 = conversions.degrees_to_radians(start.latitude)
    lat2 = conversions.degrees_to_radians(end.latitude)
    lon1 = conversions.degrees_to_radians(start.longitude)
    lon2 = conversions.degrees_to_radians(end.longitude)
    x = math.acos(math.sin(lat1) * math.sin(lat2) +
                  math.cos(lat1) * math.cos(lat2) *
                  math.cos(lon2 - lon1)) * EARTH_RADIUS_IN_METERS
    y = math.fabs(start.altitude - end.altitude)
    result = math.sqrt(x * x + y * y)
    return result


def compute_2d_distance(start, end):
    if start.equals(end):
        return 0
    lat1 = conversions.degrees_to_radians(start.latitude)
    lat2 = conversions.degrees_to_radians(end.latitude)
    lon1 = conversions.degrees_to_radians(start.longitude)
    lon2 = conversions.degrees_to_radians(end.longitude)
    return math.acos(math.sin(lat1) * math.sin(lat2) +
                     math.cos(lat1) * math.cos(lat2) *
                     math.cos(lon2 - lon1)) * EARTH_RADIUS_IN_METERS


def compute_midpoint(start, end):
    lat1 = conversions.degrees_to_radians(start.latitude)
    lon1 = conversions.degrees_to_radians(start.longitude)
    lat2 = conversions.degrees_to_radians(end.latitude)
    lon2 = conversions.degrees_to_radians(end.longitude)
    bx = math.cos(lat2) * math.cos(lon2 - lon1)
    by = math.cos(lat2) * math.sin(lon2 - lon1)
    latm = math.atan2(math.sin(lat1) + math.sin(lat2),
                      math.sqrt(math.pow(math.cos(lat1) + bx, 2) + math.pow(by, 2)))
    lonm = lon1 + math.atan2(by, math.cos(lat1) + bx)
    return GeographicPoint(conversions.radians_to_degrees(latm),
                           conversions.radians_to_degrees(lonm),
                           (max(start.altitude, end.altitude) - min(start.altitude, end.altitude)) / 2.0)


def cartesian_coordinate_to_geographic(cartesian_point, origin, rotation=0):
    rotated_cartesian_coordinates = rotate_cartesian_coordinates(cartesian_point.x, cartesian_point.y,
                                                                 cartesian_point.z, rotation)
    phi_angle = conversions.radians_to_degrees(math.atan2(rotated_cartesian_coordinates.x,
                                                          rotated_cartesian_coordinates.y))
    length = math.sqrt(math.pow(cartesian_point.x, 2) + math.pow(cartesian_point.y, 2))
    result = compute_endpoint(origin, phi_angle, length)
    return GeographicPoint(result.latitude, result.longitude, cartesian_point.z)


def geographic_coordinate_to_cartesian(origin, point, rotation):
    length = compute_2d_distance(origin, point)
    heading = compute_bearing(origin, point)
    cartesian_angle = geographic_heading_to_cartesian_angle(heading)
    x = length * math.cos(conversions.degrees_to_radians(cartesian_angle));
    y = length * math.sin(conversions.degrees_to_radians(cartesian_angle));
    rotated_cartesian_coordinates = rotate_cartesian_coordinates(x, y, point.altitude, rotation)
    # print "length@geographicHeading: {0}@{1}, {2}".format(length, heading, cartesian_angle)
    # print "x,y: {0},{1}".format(x, y)
    # print "rotated x,y: {0},{1}".format(rotated_cartesian_coordinates.x, rotated_cartesian_coordinates.y)
    return rotated_cartesian_coordinates


def geographic_heading_to_cartesian_angle(geographic_heading):
    if 0 < geographic_heading < 180:
        geographic_heading = 0 - geographic_heading
    else:
        geographic_heading = 360 - geographic_heading
    if geographic_heading < 0:
        geographic_heading += 360.0
    geographic_heading += 90
    return geographic_heading % 360


def geographic_heading_wrap_angle(geographic_heading):
    if geographic_heading >= 360.0:
        temp = int(geographic_heading / 360)
        geographic_heading -= temp * 360
    elif geographic_heading < 0:
        temp = int(geographic_heading / 360)
        geographic_heading += temp * 360
        geographic_heading += 360
    return geographic_heading % 360


def rotate_cartesian_coordinates(x, y, z, rotation_degrees):
    # http://www.mathematics-online.org/inhalt/aussage/aussage444/
    cartesian_rotate_radians = conversions.degrees_to_radians(rotation_degrees)
    xhat = x * math.cos(cartesian_rotate_radians) + y * math.sin(cartesian_rotate_radians)
    yhat = -x * math.sin(cartesian_rotate_radians) + y * math.cos(cartesian_rotate_radians)
    return CartesianPoint(xhat, yhat, z)
