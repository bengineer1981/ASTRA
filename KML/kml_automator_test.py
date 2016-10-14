#!/usr/bin/env python
# -*- coding: utf-8 -*-
import conversions
import math
from geographic_point import GeographicPoint
class location:
    def __init__(self,latitude,longitude,altitude):
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude

def compute_endpoint(origin, bearing, distance):
    EARTH_RADIUS_IN_METERS = 6371137.0
    angular_distance = float(distance) / EARTH_RADIUS_IN_METERS
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

def create_tour_open(foldername):
    XMLVERSION = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
    KMLXMLNS = "<kml xmlns=\"http://www.opengis.net/kml/2.2\" xmlns:gx=\"http://www.google.com/kml/ext/2.2\" " \
               "xmlns:kml=\"http://www.opengis.net/kml/2.2\" xmlns:atom=\"http://www.w3.org/2005/Atom\">\n"
    DOCUMENT_NAME = "\t<Document>\n" + \
                    "\t\t<name>{}</name>\n" \
                    "\t\t<open>1</open>\n" \
                    "\t\t<visibility>1</visibility>\n"
    return XMLVERSION + KMLXMLNS + DOCUMENT_NAME.format(foldername)


def create_tour_close():
    return "\t</Document>\n" \
           "</kml>\n"

def create_icon(icon, icon_name, scale=1, heading=None):
    output = "\t\t<Style id=\"" + icon_name + "\">\n" \
                                              "\t\t\t<IconStyle>\n" \
                                              "\t\t\t\t<scale>" + repr(scale) + "</scale>\n"
    if heading is not None:
        output += "\t\t\t\t<heading>" + repr(heading) + "</heading>\n"
    output += "\t   \t\t\t<Icon><href>" + icon + "</href></Icon>\n" \
                                                 "\t\t\t</IconStyle>\n" \
                                                 "\t\t</Style>\n"
    return output

def create_folder_open(folder_name):
    return "\t\t<Folder id='PlotView'>\n \
           \t\t\t<name>{0}</name>\n \
           \t\t\t<open>0</open><visibility>0</visibility>\n".format(folder_name)


def create_folder_close():
    return "\t\t</Folder>\n"

def plot_icon(icon, location, name):
    result = "\t\t<Placemark>\n \
                \t\t\t<name>{0}</name>\n \
                \t\t\t<styleUrl>#{1}</styleUrl>\n \
                \t\t\t<open>0</open><visibility>0</visibility>\n \
                \t\t\t<Point>".format(name, icon)
    if location.altitude != 0:
        result += "<altitudeMode>absolute</altitudeMode>"
    result += "<coordinates>{0},{1},{2}</coordinates></Point>\n \
                \t\t</Placemark>\n".format(location.longitude, location.latitude, location.altitude)
    return result

def plot_line(name, line_color, line_width, start_point, end_point):
    return "\t\t\t<Placemark> \n\
            \t\t\t\t<name>{0}</name> \n\
            \t\t\t\t<visibility>0</visibility> \n\
            \t\t\t\t<Style id=\"linestyleExample\"> \n\
            \t\t\t\t<LineStyle> \n\
            \t\t\t\t\t<color>{1}</color> \n\
            \t\t\t\t\t<width>{2}</width> \n\
            \t\t\t\t</LineStyle> \n\
            \t\t\t\t</Style> \n\
            \t\t\t\t<LineString><altitudeMode>absolute</altitudeMode><coordinates>{3},{4},{5},{6},{7},{8}</coordinates></LineString> \n\
            \t\t\t</Placemark>\n".format(name, line_color, line_width, start_point.longitude, start_point.latitude,
                                         start_point.altitude, end_point.longitude, end_point.latitude,
                                         end_point.altitude)



node1_loc = location(38.88541097824265,-77.10719816506928,0)
node2_loc = location(38.88453630832175,-77.10772528265257,0)
node3_loc = location(38.8845691509614,-77.10638801565288,0)
start1 = node1_loc
end1 = compute_endpoint(node1_loc,3,'1000000')
foldername = 'KmlFile'


file_start = create_tour_open(foldername)
node1_icon = create_icon('http://maps.google.com/mapfiles/kml/shapes/target.png','s_ylw-pushpin_hl0')
node2_icon = create_icon('http://maps.google.com/mapfiles/kml/shapes/target.png','s_ylw-pushpin_hl0')
node3_icon = create_icon('http://maps.google.com/mapfiles/kml/shapes/target.png','s_ylw-pushpin_hl0')
folder = create_folder_open("automate_test")
node1 = plot_icon('m_ylw-pushpin0',node1_loc,'node 1')
node2 = plot_icon('m_ylw-pushpin0',node2_loc,'node 2')
node3 = plot_icon('m_ylw-pushpin0',node3_loc,'node 3')
line1 = plot_line('line 1','ff0000aa',5,start1,end1)
folder_close = create_folder_close()
file_end = create_tour_close()

filename = open('/home/ben/Desktop/KML/automated.kml','w')
filename.write(file_start)
filename.write(node1_icon)
filename.write(node2_icon)
filename.write(node3_icon)
filename.write(folder)
filename.write(node1)
filename.write(node2)
filename.write(node3)
filename.write(line1)
filename.write(line2)
filename.write(line3)
filename.write(folder_close)
filename.write(file_end)
filename.close()
