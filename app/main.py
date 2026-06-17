class Distance:

    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, others) -> Distance:
        if isinstance(others, Distance):
            return Distance(km=self.km + others.km)
        else:
            return Distance(km=self.km + others)

    def __iadd__(self, others) -> "Distance":
        if isinstance(others, Distance):
            self.km += others.km
        else:
            self.km += others
        return self

    def __mul__(self, others) -> "Distance":
        return Distance(km=self.km * others)

    def __truediv__(self, others) -> "Distance":
        return Distance(km=(round((self.km / others), 2)))

    def __lt__(self, others) -> bool:
        if isinstance(others, Distance):
            return self.km < others.km
        return self.km < others

    def __gt__(self, others) -> bool:
        if isinstance(others, Distance):
            return self.km > others.km
        return self.km > others

    def __eq__(self, others) -> bool:
        if isinstance(others, Distance):
            return self.km == others.km
        return self.km == others

    def __le__(self, others) -> bool:
        if isinstance(others, Distance):
            return self.km <= others.km
        return self.km <= others

    def __ge__(self, others) -> bool:
        if isinstance(others, Distance):
            return self.km >= others.km
        return self.km >= others
