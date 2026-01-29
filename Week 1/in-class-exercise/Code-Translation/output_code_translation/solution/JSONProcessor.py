import json
from typing import Any


class JSONProcessor:
    def read_json(self, file_path: str, output: dict) -> int:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
        except (FileNotFoundError, OSError):
            return 0
        except Exception:
            return -1

        if data is None:
            return -1

        output.clear()
        if isinstance(data, dict):
            output.update(data)
        else:
            # Preserve original behavior for non-dict JSON root
            output["value"] = data
        return 1

    def write_json(self, data: Any, file_path: str) -> int:
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4)
        except (FileNotFoundError, OSError):
            return -1
        except Exception:
            return -1
        return 1

    def process_json(self, file_path: str, remove_key: str) -> int:
        data: dict = {}
        result = self.read_json(file_path, data)

        if result != 1:
            return 0

        if remove_key in data:
            del data[remove_key]
            return self.write_json(data, file_path)
        else:
            return 0
