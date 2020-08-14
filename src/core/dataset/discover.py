import pathlib
from typing import Mapping

from omegaconf import DictConfig

from src.base import project_root
from core.dataset.dataset import Dataset


def search_all_files_by_extension(
        path: pathlib.Path,
        extensions: list
) -> list:
    """
    Discover files by path
    """
    files_discovered = []

    for file_type in extensions:
        files_discovered += list(
            path.glob(f"**/*.{file_type}")
        )

    return files_discovered


def discover_files(
        cfg: DictConfig
) -> Mapping[str, Dataset]:
    datasets = {
        key: search_all_files_by_extension(
            path=project_root.joinpath(value[0]),
            extensions=value[1]
        )
        for key, value in cfg.paths.items()
    }

    datasets = {
        key: Dataset.from_items(
            items=value,
            name=key,
        )
        for key, value in datasets.items()
    }

    return datasets


FileDiscoverer = discover_files
