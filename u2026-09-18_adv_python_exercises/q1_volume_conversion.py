class VolumeConverter:
    """Convert a volume given in liters to a suitable unit."""

    def __init__(self, liters: float):
        self.liters = liters

    def convert(self) -> str:
        if self.liters >= 1.0:
            return f"{self.liters:.1f} l"
        if self.liters >= 0.1:
            return f"{self.liters * 100:.1f} cl"
        if self.liters >= 0.001:
            return f"{self.liters * 1000:.1f} ml"
        return "Wert zu klein"


if __name__ == "__main__":
    test_values = [0.0001, 0.02, 0.42, 1.0, 2.5, 10.0]

    for value in test_values:
        print(f"{value:>8} l ->\t{VolumeConverter(value).convert():>10}")