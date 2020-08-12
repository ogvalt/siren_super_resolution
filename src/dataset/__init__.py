from src.dataset.dataset import DatasetRegistry

from src.dataset.lapsrn import build as lapsrn

Datasets = DatasetRegistry()
Datasets.register("LapSRN", dataset_builder=lapsrn)

