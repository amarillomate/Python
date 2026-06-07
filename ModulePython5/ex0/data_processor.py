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


class DataProcessor(DataProcessor):
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


def main() -> None:
    print("=== Code Nexus - Data Processor ===")

    print("\nTesting Numeric Processor...")
    num_proc = NumericProcessor()

    num_ok = 42
    num_bad = "hello"
    print(f" Trying to validate input {num_ok}: {num_proc.validate(num_ok)}")
    print(f" Trying to validate input {num_bad}: {num_proc.validate(num_bad)}")
    print(" Test invalid ingestion of string 'foo' without prior validation:")
    try:
        num_proc.ingest("foo")
    except Exception as exc:
        print(f" Got exception: {exc}")

    nums = [1, 2, 3, 4, 5]
    print(f" Processing data: {nums}")
    num_proc.ingest(nums)
    to_extract = 3
    print(f" Extracting {to_extract} values...")
    for t in range(to_extract):
        rank, value = num_proc.output()
        print(f" Numeric value {rank}: {value}")

    print("\nTesting Text Processor...")
    text_proc = DataProcessor()

    data_ok = ["Hello", "Nexus","Wolrd"]
    print(f" Trying to validate input {num_ok}: {text_proc.validate(num_ok)}")
    print(f" Processing data: {data_ok}")
    text_proc.ingest(data_ok)
    to_extract = 1
    print(f" Extracting {to_extract} value...")
    for t in range(to_extract):
        rank, value = text_proc.output()
        print(f" Text value {rank}: {value}")

    print("\nTesting Log Processor...")
    log_proc = LogProcessor()

    log_bad = 42
    print(f" Trying to validate input {log_bad}: {log_proc.validate(log_bad)}")
    log_ok = [
                {"log_level": "NOTICE", "log_message": "Connection to server"},
                {"log_level": "ERROR", "log_message": "Unauthorized access!!"},
            ]
    print(f" Processing data: {log_ok}")
    log_proc.ingest(log_ok)
    to_extract = 2
    print(f" Extracting {to_extract} values...")
    for t in range(to_extract):
        level, message = log_proc.output()
        print (f" Log entry: {level}: {message}")
    

if __name__ == "__main__":
    main()
