class GeographicPoint(object):
    def __init__(self, lat, lon, alt):
        self._latitude = lat
        self._longitude = lon
        self._altitude = alt

    @property
    def latitude(self):
        return self._latitude

    @property
    def longitude(self):
        return self._longitude

    @property
    def altitude(self):
        return self._altitude

    def equals(self, pt):
        return self._latitude == pt.latitude and self._longitude == pt.longitude
