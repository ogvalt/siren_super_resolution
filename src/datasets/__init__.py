from src.datasets.dataset import DatasetRegistry

from src.datasets.lapsrn import build as lapsrn

Datasets = DatasetRegistry()
Datasets.register("LapSRN", dataset_builder=lapsrn)

