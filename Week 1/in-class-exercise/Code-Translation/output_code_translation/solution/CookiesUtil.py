import json
import sys
from typing import Dict, Any


class CookiesUtil:
    def __init__(self, cookiesFile: str):
        self.cookies_file: str = cookiesFile
        self.cookies: Dict[str, str] = {}

    def get_cookies(self, response: Dict[str, Any]) -> None:
        if "cookies" in response:
            # Expecting a dict of string keys/values
            self.cookies = dict(response["cookies"])
        self._save_cookies()

    def load_cookies(self) -> Dict[str, Any]:
        cookies_data: Dict[str, Any] = {}
        try:
            with open(self.cookies_file, "r", encoding="utf-8") as file:
                cookies_data = json.load(file)
        except FileNotFoundError:
            # File doesn't exist – return empty dict
            pass
        except Exception as e:
            print(f"Error reading JSON file: {e}", file=sys.stderr)
        return cookies_data

    def _save_cookies(self) -> bool:
        try:
            with open(self.cookies_file, "w", encoding="utf-8") as file:
                json.dump(self.cookies, file, indent=4)
            return True
        except Exception as e:
            print(f"Error writing JSON file: {e}", file=sys.stderr)
            return False

    def set_cookies(self, request: Dict[str, Any]) -> None:
        cookie_parts = [f"{key}={value}" for key, value in self.cookies.items()]
        request["cookies"] = "; ".join(cookie_parts)
