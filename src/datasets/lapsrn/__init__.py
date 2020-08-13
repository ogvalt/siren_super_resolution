from typing import Mapping, Any

from omegaconf import DictConfig

from core.dataset.dataset import Dataset
from core.dataset.command import DatasetProcessingChain
from src.datasets.discover import FileDiscoverer

from .container import SuperResolutionSampleContainer


idfy = lambda x: "_".join(str(x).split("/")[-2:])


def identify(dataset: Dataset, context: DictConfig) -> Dataset:
    """
    This function identifies set objects
    """

    for idx in range(len(dataset)):
        iid, itype = str(dataset[idx]).split(".")

        dataset[idx] = SuperResolutionSampleContainer(
            cid=idfy(iid),
            image=dataset[idx],
            interpolation=context.downscale_method,
            downscale_factor=context.downscale_factor,
        )
    return dataset


def deduplication(dataset: Dataset, context: DictConfig) -> Dataset:
    """
    This function deals with duplications
    """
    from collections import defaultdict

    elements_grouped_by_iid = defaultdict(list)

    for element in dataset:
        cid = element.cid
        elements_grouped_by_iid[cid].append(element)

    dt = dataset.from_items(
        name=dataset.name,
        items=[
            item[0] for key, item in list(elements_grouped_by_iid.items())
        ]
    )

    return dt


container_creator = DatasetProcessingChain()
container_creator.add(identify)
container_creator.add(deduplication)


def build(config: DictConfig) -> Mapping[str, Dataset]:
    datasets = FileDiscoverer(cfg=config)

    for key, dt in datasets.items():
        datasets[key] = \
            container_creator(dataset=dt, config=config)

    return datasets
