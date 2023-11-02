from battery.battery import Battery
from datetime import date

class NubbinBattery(Battery):
    def __init__(self, last_service_date: date, current_date: date):
        super().__init__(last_service_date)
        self.current_date = current_date

    def needs_service(self) -> bool:
        # Calculate the service threshold date for NubbinBattery (3 years)
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 3)

        # Check if the current date is beyond the service threshold date
        return service_threshold_date < self.current_date
