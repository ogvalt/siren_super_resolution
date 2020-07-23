"""
This file setup environment
"""

import logging
import os

from dotenv import load_dotenv
from omegaconf import DictConfig

from src.base import configs_root, path_env_file

logger = logging.getLogger()

load_dotenv(dotenv_path=path_env_file)

if "ENV" in os.environ:
    hydra_config_path = str(configs_root.joinpath(
        f"{os.environ['ENV']}.yaml"
    ))
    logging.info(f"[Environment] Hydra config path: {hydra_config_path}")
else:
    raise EnvironmentError(
        f"[Environment] Environment type does not specified. "
        f"Check {path_env_file}"
    )


def setup_runtime(cfg_env: DictConfig):
    """
    Setup runtime environment.
    Runtime options:
        ["cuda", "cuda:0", "cuda:<index>", "cpu", ""]
    Args:
        cfg_env (dict): Configuration

    Returns:
        None
    """
    runtime: str = cfg_env.runtime

    runtime_name, runtime_devices = \
        runtime.split(":") if ":" in runtime else [runtime, ""]

    if runtime_name == "cuda" and runtime_devices:
        os.environ["CUDA_VISIBLE_DEVICES"] = f"{runtime_devices}"
        logger.info(f"[Environment] Configuration: CUDA_VISIBLE_DEVICES="
                    f"{os.environ['CUDA_VISIBLE_DEVICES']}")
    elif runtime_name == "cpu":
        os.environ["CUDA_VISIBLE_DEVICES"] = ""
        logger.info(f"[Environment] Configuration: CUDA_VISIBLE_DEVICES="
                    f"{os.environ['CUDA_VISIBLE_DEVICES']}")

    from catalyst.utils import set_global_seed, prepare_cudnn, get_device

    seed: int = cfg_env.seed

    set_global_seed(seed)
    logger.info(f"[Environment] Configuration. Seed: {seed}")

    prepare_cudnn(deterministic=True, benchmark=False)
    logger.info(f"[Environment] Configuration. CUDNN: "
                f"deterministic=True, benchmark=False")

    device = get_device()

    logger.info(f"[Environment] Runtime: {device}")

    return device
