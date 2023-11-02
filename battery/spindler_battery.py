from battery.battery import Battery
from datetime import date

class SpindlerBattery(Battery):
    def __init__(self, last_service_date: date, current_date: date):
        super().__init__(last_service_date)
        self.current_date = current_date

    def needs_service(self) -> bool:
        # Calculate the service threshold date for SpindlerBattery
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 3)

        # Check if the current date is beyond the service threshold date
        return service_threshold_date < self.current_date

# Usage example:
if __name__ == "__main__":
    spindler_battery = SpindlerBattery(date(2021, 1, 1), date.today())

    # Check if the SpindlerBattery needs service
    if spindler_battery.needs_service():
        print("Spindler Battery needs service.")
    else:
        print("Spindler Battery does not need service.")
