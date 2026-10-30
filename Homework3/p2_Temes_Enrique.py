class ParkingPermit:
    """Parent class that represents a general university parking permit."""
    def __init__(self, name: str, months: int, schedule: dict[str,int])-> None:
        """Parent class constructor for initializing name, months, and schedule."""
        self.name = name
        self.months = months
        self.schedule = schedule

    def cost(self)->int:
        """Parent class method for returning the cost someone has to pay."""
        return self.months * self.schedule["fee"]

    def __str__(self)->str:
        """Parent class method for showing how long someone has had parking permit."""
        return f"{self.name} has had a parking permit for {self.months} months."

    def __repr__(self)->str:
        """Parent class method for showing detailed permit details for certain person."""
        return f"{self.name} has had a parking permit for {self.months} months."

class StudentPermit(ParkingPermit):
    """Child class that represents a student parking permit."""
    def __init__(self, name: str, months: int, schedule: dict[str,int], vehicles: int)->None:
        """Child class StudentPermit constructor that calls parent constructor and initializes the int vehicles."""
        super().__init__(name, months, schedule)
        self.vehicles = vehicles

    def cost(self)->int:
        """Returns cost for student permit based on how many vehicles have permits."""
        if self.vehicles > 1:  
            return (self.schedule["Student Permit"] * self.months) + (self.schedule["One-time fee"] * (self.vehicles-1))
        else:
            return self.schedule["Student Permit"] * self.months

    def __str__(self)->str:
        """Child class method for showing how long a student has had a parking permit."""
        return f"{self.name} has had a parking permit for {self.months} months."

    def __repr__(self)->str:
        """Overrides parent class __repr__ by adding how many vehicles student uses."""
        return f"{super().__repr__()} In addition, {self.name} uses {self.vehicles} vehicles."

class FacultyPermit(ParkingPermit):
    """Child class that represents faculty parking permits."""
    def __init__(self   , name: str, months: int, schedule: dict[str,int], access: bool)->None:
        """Child class FacultyPermit constructor that calls parent constructor and initializes the bool access."""
        super().__init__(name, months, schedule)
        self.access = access

    def cost(self)->int:
        """Returns cost for faculty permit based on garage access."""
        if self.access:
            return (self.schedule["Faculty Permit"] * self.months) + (self.schedule["Garage Access"] * self.months)
        else:
            return (self.schedule["Faculty Permit"] * self.months)

    def __str__(self)->str:
        """Child class method for showing how long a faculty member has had a parking permit."""
        return f"{self.name} has had a parking permit for {self.months} months."

    def __repr__(self)->str:
        """Overrides parent class __repr by adding whether or not faculty has garage access."""
        if self.access:
            return f"{ super().__repr__()} In addition, {self.name} has garage access."
        else:
            return f"{ super().__repr__()} In addition, {self.name} does not have garage access."  

def main()->None:
    """Independent of any class. Creates child class objects before calling summarize_list to print 
    all necessary information."""
    schedule = {"Student Permit": 25, "One-time fee": 10, "Faculty Permit": 40, "Garage Access": 15}
    studentPermit = StudentPermit("Enrique Temes", 4, schedule, 2)
    facultyPermit = FacultyPermit("Jacob Morales", 24, schedule, True)
    permits = [studentPermit, facultyPermit]
    print("Z23734170")
    print(f"Total revenue: ${summarize_list(permits)}")

def summarize_list(permits: list[ParkingPermit])->int:
    """Prints each person's name, permit costs and returns total revenue."""
    revenue = 0
    for permit in permits:
        revenue += permit.cost()
        print(f"{permit.__str__()}")
        print(f"{permit.__repr__()}")
        print(f"Permit cost for {permit.name}: ${permit.cost()}")

    return revenue

solution = main()