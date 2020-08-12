from dataclasses import dataclass
from typing import Any, Iterable, List


@dataclass(init=False, repr=True)
class Dataset:
    """
    Pass
    """
    name: str
    items: List[Any]

    def __init__(self, name: str):
        """
        Default initialization, empty named dataset
        """
        self.name = name
        self.items: List[Any] = []

    @classmethod
    def from_items(cls, name: str, items: List[Any]):
        """
        Create initialization, empty named dataset
        """

        instance = cls(name=name)
        instance.items = items

        return instance

    def __str__(self):
        return f"{self.__class__.__name__}" \
               f"(" \
               f"name={self.name}, " \
               f"length={self.__len__()}, " \
               f"items={self.items}, " \
               f")"

    def __len__(self):
        """
        Get dataset length
        """
        return self.items.__len__()

    def __getitem__(self, index: int):
        """
        Pass
        """
        return self.items[index]

    def __setitem__(self, index: int, value: Any):
        """
        Pass
        """
        self.items[index] = value

    def append(self, value: Any):
        """
        Pass
        """
        self.items.append(value)
        return self

    def extend(self, values: Iterable):
        """
        Pass
        """
        self.items.extend(values)
        return self
