#!usr/bin/env python
#-*- coding: utf-8 -*-

class BeeEvaluator():
    
    def __init__(self, dictionary):
        self.bad_coefficient = 0.000095
        self.good_coefficient = 1

        self.wind_limit = 15 + 2
        
        self.humity_ok = 30
        self.humity_max, self.humity_min = (self.humity_ok + 2, self.humity_ok - 2)

        self.ideal_pressure = 1013.25 # 1 atm

        self.temperature_min = 30
        self.temperature_max = 33

        self.dictionary = dictionary
        self.score = 0

    def getScore(self):
        return self.score

    def evaluate(self):
        if self.dictionary["wind"].has_key("speed"):
            self.evaluate_wind()
        if self.dictionary["weather"].has_key("humity"):
            self.evaluate_humity()
        if self.dictionary["weather"].has_key("pressure"):
            self.evaluate_pressure()
        if self.dictionary["weather"].has_key("temp"):
            self.evaluate_temperature()

    def evaluate_wind(self):
        speed = self.dictionary["wind"]["speed"]
        if speed >= self.wind_limit:
            self.decrement(self.wind_limit, (speed - self.wind_limit))
        else:
            self.increment()
    
    def evaluate_humity(self):
        humity = self.dictionary["weather"]["humity"]
        if humity > self.humity_max:
            self.decrement(self.humity_max, (humity - self.humity_max))
        elif humity < self.humity_min:
            self.decrement(self.humity_min, (humity - self.humity_min))
        else:
            self.increment()
        
    def evaluate_pressure(self):
        pressure = self.dictionary["weather"]["pressure"]
        if pressure > self.ideal_pressure:
            self.decrement(self.ideal_pressure, (pressure - self.ideal_pressure))
        elif pressure < self.ideal_pressure:
            self.decrement(self.ideal_pressure, (pressure - self.ideal_pressure))
        else:
            self.increment()
    
    def evaluate_temperature(self):
        temperature = self.dictionary["weather"]["temp"]
        if temperature > self.temperature_max:
            self.decrement(self.temperature_max, (temperature - self.temperature_max))
        elif temperature < self.temperature_min:
            self.decrement(self.temperature_min, (temperature - self.temperature_min))
        else:
            self.increment()

    def getEvaluatedCity(self):
        return {
            "name": self.dictionary["state"],
            "score": self.getScore()
        }

    def decrement(self, limit, exceeded):
        self.score -= (limit - exceeded) * self.bad_coefficient

    def increment(self):
        self.score += self.good_coefficient  