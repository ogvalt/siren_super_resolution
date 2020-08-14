from src.models import Models
from src.datasets import Datasets


def train(device, cfg):
    dataset = Datasets(cfg.dataset)
    model = Models(cfg.model)
    return 0
