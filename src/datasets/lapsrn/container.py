import pathlib
from dataclasses import dataclass
from typing import Mapping, Any

import cv2
from catalyst.utils import imread


@dataclass
class BaseContainer:
    cid: str


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

    def read(self) -> Mapping[str, Any]:
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

        return {
            "input_key": img_input,
            "input_target_key": img_input_target
        }
