from battery.battery import Battery
from datetime import date

class NubbinBattery(Battery):
    def __init__(self, last_service_date: date, current_date: date):
        super().__init__(last_service_date)
        self.current_date = current_date

    def needs_service(self) -> bool:
        # Calculate the service threshold date for NubbinBattery
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)

        # Check if the current date is beyond the service threshold date
        return service_threshold_date < self.current_date

# Usage example:
if __name__ == "__main__":
    nubbin_battery = NubbinBattery(date(2019, 1, 1), date.today())

    # Check if the NubbinBattery needs service
    if nubbin_battery.needs_service():
        print("Nubbin Battery needs service.")
    else:
        print("Nubbin Battery does not need service.")
