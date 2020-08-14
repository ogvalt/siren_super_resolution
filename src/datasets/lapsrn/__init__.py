from typing import Mapping

from omegaconf import DictConfig

from core.registry import Registry
from core.dataset import (
    Dataset,
    FileDiscoverer,
    DatasetProcessingChain
)


from .super_resolution import SuperResolutionContainerBuilder
from .coordinate2pixel import Coord2PixelContainerBuilder


class ContainerRegistry(Registry):

    def register(
            self,
            name: str,
            container_builder: DatasetProcessingChain
    ) -> None:
        super().register(name=name, user_type=container_builder)

    def __call__(self, dataset: Dataset, cfg: DictConfig):
        container_type = cfg.get("type")

        container_builder: DatasetProcessingChain = \
            self.named_registry[container_type]

        return container_builder(dataset=dataset, config=cfg)


ContainerBuilder = ContainerRegistry()
ContainerBuilder.register("super-resolution", SuperResolutionContainerBuilder)
ContainerBuilder.register("coord2pixel", Coord2PixelContainerBuilder)


def build(config: DictConfig) -> Mapping[str, Dataset]:
    datasets = FileDiscoverer(cfg=config)

    for key, dt in datasets.items():
        datasets[key] = \
            ContainerBuilder(dataset=dt, cfg=config)

    return datasets
