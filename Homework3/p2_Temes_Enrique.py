class ParkingPermit:
    def __init__(self, name, months, schedule)-> None:
        self.name = name
        self.months = months
        self.schedule = schedule

    def cost(self):
        return self.months * self.schedule["fee"]

class StudentPermit(ParkingPermit):
    def __init__(self, name, months, schedule, vehicles):
        super().__init__(name, months, schedule)
        self.name = name
        self.months = months
        self.schedule = schedule
        self.vehicles = vehicles

    def cost(self):
        if self.vehicles > 1:  
            return (25 * self.months) + (10 * (self.vehicles-1))
        else:
            return 25 * self.months

class FacultyPermit(ParkingPermit):
    def __init__(self, name, months, schedule, access):
        super().__init__(name, months, schedule)
        self.name = name
        self.months = months
        self.schedule = schedule
        self.access = access

    def cost(self):
        if self.access:
            return 40 * self.months + 15*self.months
        else:
            return 40 * self.months