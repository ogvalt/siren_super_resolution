from omegaconf import DictConfig

from src.core.dataset import Dataset
from src.dataset.discover import FileDiscoverer


def build(config: DictConfig) -> Dataset:
    datasets = FileDiscoverer(cfg=config)
    return datasets
