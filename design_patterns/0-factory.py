#!/usr/bin/env python3
"""
Factory Pattern - Vehicle Factory with Registry
Demonstrates the Open/Closed Principle through dynamic registration
"""


class Bus:
    """Bus vehicle"""
    def mode(self):
        return "road"


class Train:
    """Train vehicle"""
    def mode(self):
        return "rails"


class Bike:
    """Bike vehicle"""
    def mode(self):
        return "lane"


class Scooter:
    """Scooter vehicle - not yet registered"""
    def mode(self):
        return "scooter_lane"


class VehicleFactory:
    """
    Factory for creating vehicles using a registry pattern.

    The registry maps string names to vehicle classes.
    New vehicle types can be added without modifying the create() method.
    """

    def __init__(self):
        """Initialize factory with empty registry and register initial types"""
        self._registry = {}
        # Pre-register existing vehicle types
        self.register_kind("bus", Bus)
        self.register_kind("train", Train)
        self.register_kind("bike", Bike)

    def register_kind(self, name: str, cls):
        """
        Register a new vehicle type in the factory.

        Args:
            name: String identifier for the vehicle type
            cls: The class to instantiate for this vehicle type
        """
        self._registry[name] = cls

    def create(self, kind: str):
        """
        Create a vehicle instance by name.

        Args:
            kind: The registered name of the vehicle type

        Returns:
            An instance of the requested vehicle type

        Raises:
            ValueError: If the vehicle type is not registered
        """
        cls = self._registry.get(kind)
        if cls is None:
            raise ValueError(f"Unknown vehicle kind: {kind}")
        return cls()


def main():
    """Demonstrate the factory pattern with vehicle creation"""
    factory = VehicleFactory()

    # Create and use pre-registered vehicles
    print(factory.create("bus").mode())
    print(factory.create("train").mode())
    print(factory.create("bike").mode())

    # Register the new Scooter type
    factory.register_kind("scooter", Scooter)

    # Create and use the newly registered vehicle
    print(factory.create("scooter").mode())


if __name__ == "__main__":
    main()
