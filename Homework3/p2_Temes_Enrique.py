class ParkingPermit:
    def __init__(self, name, months, schedule)-> None:
        self.name = name
        self.months = months
        self.schedule = schedule

    def cost(self)->None:
        return self.months * self.schedule["fee"]

    def __str__(self)->str:
        return f"{self.name} has had a parking permit for {self.months} months."

    def __repr__(self)->str:
        return f"{self.name} has had a parking permit for {self.months} months."

class StudentPermit(ParkingPermit):
    def __init__(self, name, months, schedule, vehicles)->None:
        super().__init__(name, months, schedule)
        self.name = name
        self.months = months
        self.schedule = schedule
        self.vehicles = vehicles

    def cost(self)->int:
        if self.vehicles > 1:  
            return (self.schedule["Student Permit"] * self.months) + (self.schedule["One-time fee"] * (self.vehicles-1))
        else:
            return self.schedule["Student Permit"] * self.months

    def __repr__(self)->str:
        super().__repr__()
        return f"In addition, {self.name} uses {self.vehicles} vehicles."

class FacultyPermit(ParkingPermit):
    def __init__(self, name: str, months: int, schedule: dict, access: bool)->None:
        super().__init__(name, months, schedule)
        self.name = name
        self.months = months
        self.schedule = schedule
        self.access = access

    def cost(self)->int:
        if self.access:
            return (self.schedule["Faculty Permit"] * self.months) + (self.schedule["Garage Access"] * self.months)
        else:
            return (self.schedule["Faculty Permit"] * self.months)

    def __repr__(self)->str:
        super().__repr__()
        if self.access:
            return f"In addition, {self.name} has garage access."
        else:
            return f"In addition, {self.name} does not have garage access."  

def main():
    schedule = {"Student Permit": 25, "One-time fee": 10, "Faculty Permit": 40, "Garage Access": 15}
    studentPermit = StudentPermit("Enrique Temes", 4, schedule, 2)
    facultyPermit = FacultyPermit("Jacob Morales", 24, schedule, True)
    permits = [studentPermit, facultyPermit]
    print("Z23734170")
    print(f"Total revenue: ${summarize_list(permits)}")

def summarize_list(permits: list[ParkingPermit])->int:
    revenue = 0
    for permit in permits:
        revenue += permit.cost()
        print(f"{permit.__str__()}")
        print(f"{permit.__repr__()}")
        print(f"Permit cost for {permit.name}: ${permit.cost()}")

    return revenue

solution = main()