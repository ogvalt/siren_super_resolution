from typing import Dict, Any

suppress_errors = True


class Registry:
    def __init__(self) -> None:
        self.named_registry: Dict[str, Any] = {}

    def register(
            self,
            name: str,
            user_type: object
    ) -> None:
        if name in self.named_registry.keys():
            msg: str = f"[{self.__name__}] user_type {name} already registered"
            if suppress_errors:
                raise RuntimeWarning(msg)
            else:
                raise RuntimeError(msg)

        self.named_registry[name] = user_type

    def replace(
            self,
            name: str,
            user_type: object
    ) -> None:
        self.named_registry[name] = user_type

    def __call__(self, *args, **kwargs):
        pass
