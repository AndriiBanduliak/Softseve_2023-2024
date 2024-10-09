class WashingMachine:
    def __init__(self):
        self.washer = Washer()
        self.rinser = Rinser()
        self.spinner = Spinner()

    def start_washing(self):
        self.washer.wash()

    def start_rinsing(self):
        self.rinser.rinse()

    def start_spinning(self):
        self.spinner.spin()

    def startWashing(self):
        self.start_washing()
        self.start_rinsing()
        self.start_spinning()


class Washer:
    def wash(self):
        print("Washing...")


class Rinser:
    def rinse(self):
        print("Rinsing...")


class Spinner:
    def spin(self):
        print("Spinning...")


washingMachine = WashingMachine()
