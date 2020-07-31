"""
File with experiments
"""

import hydra
from omegaconf import DictConfig

from env import hydra_config_path, setup_runtime


@hydra.main(config_path=hydra_config_path)
def experiments(cfg: DictConfig):
    """
    Pass
    """
    device = setup_runtime(cfg.env)

    # TODO: Place experiment here
    print(device)


if __name__ == "__main__":
    experiments()
