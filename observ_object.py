from math import tan, acos, radians, degrees
from datetime import date as Date
from convertor import *


class ObservObject:
    """Represent different objects to observations(Planets, Comets, Asteroids)"""

    def __init__(self, typ, name, r_a, decl, mag, con):
        """
        :param typ: type of object(Planet, Comet, Asteroid)
        :param name: name of object
        :param r_a: right ascension
        :param decl: declination
        :param mag: magnitude
        :param con: constellation
        """
        self.typ = typ
        self.name = name
        self.r_a = r_a
        self.decl = decl
        self.mag = mag
        self.con = con

    def __repr__(self):
        return [self.typ, self.name, self.r_a, self.decl, self.mag, self.con]

    def __str__(self):
        name = self.typ + ' ' + self.name
        r_a = hours_to_str(self.r_a)
        decl = degree_to_str(self.decl)
        mag = str(self.mag)
        con = self.con
        rise = time_to_str(self.rise) if self.rise else '-----'
        set = time_to_str(self.set) if self.set else '-----'

        return (name + 40*' ')[:40] + (r_a+5*' ')[:10] + '\t' + (decl+5*' ')[:13] + \
               '\t' + mag + '\t' + (con+15*' ')[:15] + '\t' + rise + '\t' + set

    def calc_time(self, date, place, timezone):
        """Return time of rise and set of object in a place and date
        :param date: date of day for observation in format [year, month, day] e.c. [2020, 3, 8]
        :param place: place of observation in format [latitude (°), longitude (°)] e.c. [+49.84, +24.03]
        :param timezone: timezone, including summer/winter time e.c. +3
        """
        year, month, day = date
        lat, lon = place

        c = -tan(radians(self.decl))*tan(radians(lat))
        if c < -1 or c > 1:
            self.rise = None
            self.set = None
            return None, None

        delta_time = (Date(year, month, day) - Date(year, 9, 21)).days/365.24219*360
        delta = hours_to_degree(self.r_a) - delta_time + hours_to_degree(timezone) - lon

        hour_angle = degrees(acos(c))
        if hour_angle < 180:
            rise_HA = 360 - hour_angle
            set_HA = hour_angle
        else:
            rise_HA = hour_angle
            set_HA = 360 - hour_angle

        rise_time = degree_to_hours((rise_HA + delta)%360)
        set_time = degree_to_hours((set_HA + delta)%360)

        self.rise = rise_time
        self.set = set_time
        return rise_time, set_time

