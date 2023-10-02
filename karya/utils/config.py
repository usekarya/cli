import json
import os


class Config:
    CONFIG_FILE_BASE_PATH: str = os.path.expanduser("~/.opennu/")
    CONFIG_FILE: str = "config.json"

    def __write_key(self, key: str, value: str):
        os.makedirs(self.CONFIG_FILE_BASE_PATH, exist_ok=True)

        config_json = {}
        if os.path.isfile(self.CONFIG_FILE_BASE_PATH + self.CONFIG_FILE):
            config_json = json.load(open(self.CONFIG_FILE_BASE_PATH + self.CONFIG_FILE, "r"))

        config_json[key] = value

        json.dump(config_json, open(self.CONFIG_FILE_BASE_PATH + self.CONFIG_FILE, "w"), indent=4)

    @classmethod
    def write_auth_key(cls, auth_key: str):
        cls.__write_key(cls, "auth_key", auth_key)

    @classmethod
    def write_base_url(cls, base_url: str):
        cls.__write_key(cls, "base_url", base_url)


__all__ = ["Config"]
