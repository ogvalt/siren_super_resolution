import pathlib
from dataclasses import dataclass

from omegaconf import DictConfig

import cv2
from catalyst.utils import imread

from core.dataset import (
    Dataset,
    BaseContainer,
    DatasetProcessingChain
)

default_interpolations = {
    "nearest": cv2.INTER_NEAREST,
    "bilinear": cv2.INTER_LINEAR,
    "bicubic": cv2.INTER_CUBIC,
}


@dataclass
class SuperResolutionSampleContainer(BaseContainer):
    image: pathlib.Path
    interpolation: str
    downscale_factor: int

    def prepare(self):
        image_path = self.image
        scale = 1 / self.downscale_factor
        interpolation = self.interpolation

        img_input_target = imread(image_path)
        img_input = cv2.resize(
            img_input_target,
            None, None,
            fx=scale, fy=scale,
            interpolation=default_interpolations[interpolation]
        )

        return img_input, img_input_target


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


SuperResolutionContainerBuilder = DatasetProcessingChain()
SuperResolutionContainerBuilder.add(identify)
SuperResolutionContainerBuilder.add(deduplication)
