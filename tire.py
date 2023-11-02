class Tire:
    def __init__(self, tire_type, tire_wear):
        self.tire_type = tire_type
        self.tire_wear = tire_wear

    def needs_service(self):
        if self.tire_type == "Carrigan":
            return any(wear >= 0.9 for wear in self.tire_wear)
        elif self.tire_type == "Octoprime":
            return sum(self.tire_wear) >= 3
        else:
            return False
