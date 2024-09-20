import json
import os
import pathlib
import re
from collections.abc import Iterable
from pathlib import Path

import loguru
from ruamel.yaml import YAML


class TextBlazeToEspansoConverter:
    """
    Convert TextBlaze JSON file with snippets to an Espanso matches
    directory filled with YAML files named after TextBlaze directories
    """

    def __init__(
        self,
        textblaze_export_json_path: pathlib.Path | os.PathLike = None,
        espanso_matches_path: pathlib.Path | os.PathLike = None,
        snippets_directory_name: (
            pathlib.Path | os.PathLike
        ) = "textblaze_snippets",
    ):
        self.textblaze_export_json_path = textblaze_export_json_path
        self.espanso_matches_path = espanso_matches_path
        self.snippets_directory_name = snippets_directory_name
        assert self.textblaze_export_json_path
        assert self.espanso_matches_path
        self.snippets_matches_directory = (
            self.espanso_matches_path / self.snippets_directory_name
        )
        self.folders_key = "folders"
        self.folder_name_key = "name"
        self.snippets_key = "snippets"
        self.snippet_shortcut_key = "shortcut"
        self.snippet_text_key = "text"
        self.espanso_file_extension = ".yml"
        self.filenames = set()

    def convert(self):
        loguru.logger.debug(f"Creating {self.snippets_matches_directory}")
        self.snippets_matches_directory.mkdir(parents=True, exist_ok=True)
        loguru.logger.debug(
            f"Opening TextBlaze snippets file "
            f"{self.textblaze_export_json_path}"
        )
        snippets_dict = json.loads(
            open(self.textblaze_export_json_path, "r").read()
        )
        for folder in snippets_dict.get(self.folders_key):
            self._save_folders_as_espanso_matches(folder)

    @property
    def yaml_processor(self):
        yaml = YAML(typ="rt", pure=True)
        yaml.indent(mapping=2, sequence=4, offset=2)
        return yaml

    def _save_folders_as_espanso_matches(self, folder: dict):
        matches = {"matches": []}
        filename = (
            self._snake_cased(folder.get(self.folder_name_key))
            + self.espanso_file_extension
        )
        self.filenames.add(filename)
        for snippet in folder.get(self.snippets_key):
            matches["matches"].append(
                {
                    "trigger": self._format_trigger(snippet),
                    "replace": f"{snippet.get(self.snippet_text_key)}",
                }
            )
        self.yaml_processor.dump(
            matches,
            open(self.snippets_matches_directory / filename, "w"),
        )
        loguru.logger.debug(
            f"Saved {filename} to {self.snippets_matches_directory}"
        )

    def _format_trigger(self, snippet):
        """
        I substitute the original symbol bc the escape symbol it typed in a
        single click on any keyboard layout. I prefer it to espanso's default
        """
        return f"{snippet.get(self.snippet_shortcut_key)}".replace("/", "\\")

    @staticmethod
    def _snake_cased(string, regex="([A-Z][a-z]+)", replacement=r"_\1"):
        return re.sub(regex, replacement, string).replace(" ", "_").lower()


if __name__ == "__main__":

    TextBlazeToEspansoConverter(
        Path("TextBlazeExport.json"),
        Path("/home/kalitka/.config/espanso/match"),
        Path("test_version"),
    ).convert()
