from typing import Callable, List, Tuple, Any, Mapping
from omegaconf import DictConfig


from core.dataset.dataset import Dataset


class ProcessingChain:
    """
    Abstraction that is used to perform
    transformations on Dataset type
    according to some configuration
    """
    command_chain: List[Tuple[int, Callable]] = []

    def add(self, command: Callable[[Any, Mapping], Any]) -> None:

        order: int = len(self.command_chain) + 1

        self.command_chain.append(
            (order, command)
        )

    def __call__(
            self,
            obj: Any,
            command_context: Mapping
    ) -> Any:
        commands = self.command_chain

        if commands:
            for order, step in commands:
                obj = step(obj, command_context)

        return obj


class DatasetProcessingChain(ProcessingChain):

    def add(
            self,
            command: Callable[[Dataset, DictConfig], Dataset]
    ) -> None:
        super().add(command)

    def __call__(
            self,
            dataset: Dataset,
            config: DictConfig
    ):
        return super().__call__(obj=dataset, command_context=config)

