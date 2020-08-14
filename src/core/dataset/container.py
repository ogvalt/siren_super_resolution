from dataclasses import dataclass


@dataclass
class BaseContainer:
    cid: str

    def prepare(self):
        """
        Implement final processing step
        :return Tuple(<data_input>, <data_target>)
        """
        raise NotImplementedError

    def read(self):
        data_input, data_target = self.prepare()

        return {
            "input_key": data_input,
            "input_target_key": data_target
        }
