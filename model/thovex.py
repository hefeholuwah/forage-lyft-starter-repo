from engine.capulet_engine import CapuletEngine


from datetime import datetime
from tire import Tire  # Import the Tire class

class Thovex(CapuletEngine):
    def __init__(self, last_service_date, current_mileage, last_service_mileage, tire_info):
        super().__init__(last_service_date, current_mileage, last_service_mileage)
        self.tire = Tire(tire_info["type"], tire_info["wear"])  # Initialize the Tire instance

    def needs_service(self):
        # Check if either the engine or the tire needs service
        return super().needs_service() or self.tire.needs_service()


