from typing import Callable

from omegaconf import DictConfig

from src.core.registry import Registry
from core.dataset.dataset import Dataset


class DatasetRegistry(Registry):

    def register(
            self,
            name: str,
            dataset_builder: Callable
    ) -> None:
        super().register(name=name, user_type=dataset_builder)

    def __call__(self, cfg: DictConfig) -> Dataset:
        name = cfg.get("name")
        parameters = cfg.get("parameters")

        dataset_builder_fn: Callable = self.named_registry[name]
        return dataset_builder_fn(parameters)




