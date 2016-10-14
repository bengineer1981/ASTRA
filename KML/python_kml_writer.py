#!/usr/bin/env python
# -*- coding: utf-8 -*-
kml_file = open('/home/ben/Desktop/python_kml_writer_output.kml','w+')

line1 = '<?xml version="1.0" encoding="UTF-8"?>\n'
line2 = '<kml xmlns="http://www.opengis.net/kml/2.2">\n'
line3 = '\t<Document>\n'
line5 = '\t\t<name>Paths</name>\n'
line6 = '\t\t<description>Examples of paths. Note that the tessellate tag is by default\n'
line7 = '\t\tset to 0. If you want to create tessellated lines, they must be authored\n'
line8 = '\t\t(or edited) directly in KML.</description>\n'
line9 = '\t\t<Style id="yellowLineGreenPoly">\n'
line10 ='\t\t\t<LineStyle>\n'
line11 ='\t\t\t\t<color>7f00ffff</color>\n'
line12 ='\t\t\t\t<width>2</width>\n'
line13 ='\t\t\t</LineStyle>\n'
line14 ='\t\t\t<PolyStyle>\n'
line15 ='\t\t\t\t<color>7f00ff00</color>\n'
line16 ='\t\t\t</PolyStyle>\n'
line17 ='\t\t</Style>\n'
line18 ='\t\t<Placemark>\n'
line19 ='\t\t\t<name>Absolute Extruded</name>\n'
line20 ='\t\t\t<description>Transparent green wall with yellow outlines</description>\n'
line21 ="\t\t\t<styleUrl>#yellowLineGreenPoly</styleUrl>'\n"
line22 ='\t\t\t<LineString>\n'
line23 ='\t\t\t\t<extrude>1</extrude>\n'
line24 ='\t\t\t\t<tessellate>1</tessellate>\n'
line25 ='\t\t\t\t<altitudeMode>absolute</altitudeMode>\n'
line26 ='\t\t\t\t<coordinates> -112.2550785337791,36.07954952145647,2357\n'
line27 ='\t\t\t\t-112.2549277039738,36.08117083492122,2357\n'
line28 ='\t\t\t\t-112.2552505069063,36.08260761307279,2357\n'
line29 ='\t\t\t\t</coordinates>\n'
line30 ='\t\t\t</LineString>\n'
line31 ='\t\t</Placemark>\n'
line32 ='\t</Document>\n'
line33 ='</kml>\n'
kml_file.writelines([line1,line2,line3,line5,line6,line7,line8,line9,
line10,line11,line12,line13,line14,line15,line16,line17,line18,line19,line20,
line21,line22,line23,line24,line25,line26,line27,line28,line29,line30,line31,line32,line33])
