"""
File with experiments
"""

import os

import hydra
from omegaconf import DictConfig

from env import hydra_config_path, setup_runtime


@hydra.main(config_path=hydra_config_path)
def experiments(cfg: DictConfig):
    """
    Pass
    """
    device = setup_runtime(cfg.env)

    from src.experiments.train import train

    train(device, cfg)


if __name__ == "__main__":
    experiments()
