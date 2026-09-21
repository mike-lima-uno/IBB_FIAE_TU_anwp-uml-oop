class LkwMaut:
    """Calculate the toll for a truck based on emission class and axles."""

    RATES = {
        "A": (12.50, 13.10),
        "B": (14.60, 15.20),
        "C": (15.70, 16.30),
        "D": (18.80, 19.40),
        "E": (19.80, 20.40),
        "F": (20.80, 21.40),
    }

    def __init__(self, emission_class: str, axles: int, kilometers: float):
        self.emission_class = emission_class.upper()
        self.axles = axles
        self.kilometers = kilometers

    def calculate(self) -> float:
        if self.emission_class not in self.RATES:
            raise ValueError("Unbekannte Schadstoffklasse")
        if self.axles < 1:
            raise ValueError("Die Achsanzahl muss positiv sein")

        rate_index = 0 if self.axles <= 3 else 1
        rate = self.RATES[self.emission_class][rate_index]
        return rate * self.kilometers


if __name__ == "__main__":
    test_trucks = [
        LkwMaut("A", 2, 13),
        LkwMaut("D", 5, 13),
    ]

    for truck in test_trucks:
        print(f"{truck.calculate():.1f} Eurocent")