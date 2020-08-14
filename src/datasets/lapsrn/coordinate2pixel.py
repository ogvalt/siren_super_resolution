from dataclasses import dataclass

from omegaconf import DictConfig

from core.dataset import (
    Dataset,
    BaseContainer,
    DatasetProcessingChain
)


@dataclass
class Coord2PixelSampleContainer(BaseContainer):

    def prepare(self):
        return tuple(..., ...)


def foo(dataset: Dataset, context: DictConfig) -> Dataset:
    return dataset


def boo(dataset: Dataset, context: DictConfig) -> Dataset:
    return dataset


def doo(dataset: Dataset, context: DictConfig) -> Dataset:
    return dataset


Coord2PixelContainerBuilder = DatasetProcessingChain()
Coord2PixelContainerBuilder.add(foo)
Coord2PixelContainerBuilder.add(boo)
Coord2PixelContainerBuilder.add(doo)
