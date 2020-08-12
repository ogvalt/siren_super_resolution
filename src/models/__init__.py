"""
Model registry file
"""
from typing import Type

import torch.nn as nn
from omegaconf import DictConfig

from src.core.registry import Registry

from .siren import Siren


class ModelsRegistry(Registry):

    def register(
            self,
            name: str,
            model: Type[nn.Module]
    ) -> None:
        super().register(name=name, user_type=model)

    def __call__(self, cfg: DictConfig) -> nn.Module:
        name = cfg.get("name")
        parameters = cfg.get("parameters")

        model_object: nn.Module = self.named_registry[name]
        return model_object(**parameters)


Models = ModelsRegistry()
Models.register("siren", model=Siren)
