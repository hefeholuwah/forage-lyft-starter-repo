from abc import ABC, abstractmethod
from datetime import date, datetime

class Battery(ABC):
    def __init__(self, last_service_date: date):
        self.last_service_date = last_service_date

    @abstractmethod
    def needs_service(self) -> bool:
        pass

class SpindlerBattery(Battery):
    def __init__(self, last_service_date: date, current_date: date):
        super().__init__(last_service_date)
        self.current_date = current_date

    def needs_service(self) -> bool:
        # Calculate the service threshold date for SpindlerBattery
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)

        # Check if the current date is beyond the service threshold date
        return service_threshold_date < self.current_date

class NubbinBattery(Battery):
    def __init__(self, last_service_date: date, current_date: date):
        super().__init__(last_service_date)
        self.current_date = current_date

    def needs_service(self) -> bool:
        # Calculate the service threshold date for NubbinBattery
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)

        # Check if the current date is beyond the service threshold date
        return service_threshold_date < self.current_date

# Usage examples:
spindler_battery = SpindlerBattery(date(2021, 1, 1), datetime.now().date())
nubbin_battery = NubbinBattery(date(2020, 1, 1), datetime.now().date())

# Check if the batteries need service
print("Spindler Battery needs service:", spindler_battery.needs_service())
print("Nubbin Battery needs service:", nubbin_battery.needs_service())
