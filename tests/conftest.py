import sys
import os

path = os.path.join(os.path.dirname(__file__), "..", "source")

sys.path.insert(0, path)  # add 'fluently' library path for importing into the tests


class Thing(object):
    """A simple data type class for use within the unit tests."""

    def __init__(self, **data: dict[str, object]):
        if not isinstance(data, dict):
            raise TypeError("The 'data' argument must reference a dictionary!")

        self._data: dict = data

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({str(self._data)})"

    def __getattr__(self, name) -> object:
        if name.startswith("_"):
            value = super().__getattr__(name)
        elif name in self._data:
            value = self._data[name]
        else:
            value = None

        return value
