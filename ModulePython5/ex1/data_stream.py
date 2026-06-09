#!/usr/bin/env python3


import typing
import abc


Any = typing.Any


class DataProcessor(abc.ABC):
    def __init__(self) -> None:
        self._buffer: list[str] = []
        self._rank_counter: int = 0

    @abc.abstractmethod
    def validate(self, data: Any) -> bool:
        raise NotImplementedError

    @abc.abstractmethod
    def ingest(self, data: Any) -> bool:
        raise NotImplementedError

    def output(self) -> tuple[int, str]:
        if not self._buffer:
            raise IndexError("No data to output")
        value = self._buffer.pop(0)
        rank = self._rank_counter
        self._rank_counter += 1
        return rank, value


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(isinstance(x, (int,float)) for x in data)
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")

        if isinstance(data, (int, float)):
            self._buffer.append(str(data))
        else:
            for x in data:
                if not isinstance(x, (int, float)):
                    raise ValueError("Invalid Value")
                self._buffer.append(str(x))


class TextProcessor(DataProcessor):
    def  validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return (all(isinstance(x, str) for x in data))
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")

        if isinstance(data, str):
            self._buffer.append(data)
        else:
            for x in data:
                if not isinstance(x, str):
                    raise ValueError("Invalid text data")
                self._buffer.append(x)


class LogProcessor(DataProcessor):
    def _is_log_dict(self, d: Any) -> bool:
        return(
                isinstance(d, dict)
                and all(isinstance(k, str) for k in d.keys())
                and all(isinstance(v, str) for v in d.values())
                )
    def validate(self, data: Any) -> bool:
        if self._is_log_dict(data):
            return True
        if isinstance(data, list):
            return all(self._is_log_dict(x) for x in data)
        return False

    def _format_log(self, entry: dict[str, str]) -> str:
        level = entry.get("log_level", "")
        message = entry.get("log_message", "")
        return f"{level}: {message}"

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Invalid data")

        if isinstance(data, dict):
            self._buffer.append(self._format_log(data))
        else:
            for entry in data:
                if not self._is_log_dict(entry):
                    raise ValueError("Invalid data")
                self._buffer.append(self._format_log(entry))

class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []
        self._total_ingested: dict[DataProcessor, int] = {}

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)
        self._total_ingested[proc] = 0

    def process_stream(self, stream: list[Any]) -> None:
        for elem in stream:
            handled = False
            for proc in self._processors:
                if proc.validate(elem):
                    before = len(proc._buffer)
                    proc.ingest(elem)
                    after = len(proc._buffer)
                    added = after - before
                    self._total_ingested[proc] += added
                    handled = True
                    break
            if not handled:
                print(f"DataStream error - Can't process element in stream: {elem}")

    def print_processors_stats(self) -> None:
        if not self._processors:
            print("DataStream statistics")
            print(" No processor found, no data")
            return

        print("=== DataStream statistics ===")
        for proc in self._processors:
            name = proc.__class__.__name__
            total = self._total_ingested.get(proc, 0)
            remaining = len(proc._buffer)
            print(f" {name} total {total} items processed, remaining {remaining} on processor")


def main() -> None:
    print("=== CodeNexus - DataStream ===")
    print("\nInitialize DataStream...")
    print("== DataStream statidistics ==")
    stream = DataStream()

    stream.print_processors_stats()

    print("\nRegestering Numeric Processor...\n")
    num_proc = NumericProcessor()
    stream.register_processor(num_proc)

    first_batch = [
        "Hello world",
        [3.14,
        -1,
        2.71],
        {"log_level": "WARNING", "log_message": "Telnet access! Use ssh instead"},
        {"log_level": "INFO", "log_message": "User wili is connected"},
        42,
        ["Hi",
        "five"],
    ]
    print("Send first batch of data on stream")
    print(first_batch)
    stream.process_stream(first_batch)
    stream.print_processors_stats()

    print("\nRegistering other data processors")
    text_proc = TextProcessor()
    log_proc = LogProcessor()
    stream.register_processor(text_proc)
    stream.register_processor(log_proc)

    print("Send the same batch again")
    stream.process_stream(first_batch)
    stream.print_processors_stats()

    print("\nConsume some elements from the data processors: Numeric 3, Text 2, Log 1")

    for _ in range(3):
        num_proc.output()

    for _ in range(2):
        text_proc.output()

    for _ in range(1):
        log_proc.output()

    stream.print_processors_stats()


if __name__ == "__main__":
    main()
