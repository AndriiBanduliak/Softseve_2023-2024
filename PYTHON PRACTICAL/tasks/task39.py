import json
import xml.etree.ElementTree as ET


# Adaptee classes for different types of vehicles
class MotorCycle:
    def __init__(self):
        self.name = "MotorCycle"

    def TwoWheeler(self):
        return "TwoWheeler"


class Truck:
    def __init__(self):
        self.name = "Truck"

    def FourWheeler(self):
        return "FourWheeler"

    def EightWheeler(self):
        return "EightWheeler"


class Car:
    def __init__(self):
        self.name = "Car"

    def FourWheeler(self):
        return "FourWheeler"


# Adapter class to translate XML data to JSON
class Adapter:
    def __init__(self, obj, **adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        return getattr(self.obj, attr)

    def original_dict(self):
        return self.obj.__dict__

    def to_json(self):
        # Convert XML data to JSON format
        xml_data = self.original_dict()
        json_data = json.dumps(xml_data, indent=4)
        return json_data




