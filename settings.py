import os
import pathlib

from dataclasses import dataclass


@dataclass
class ConverterSettings:
    textblaze_export_json_path: pathlib.Path | os.PathLike = None
    espanso_matches_path: pathlib.Path | os.PathLike = None
    snippets_directory_name: pathlib.Path | os.PathLike = pathlib.Path(
        "test_version"
    )
    snippets_matches_directory = espanso_matches_path / snippets_directory_name
    folders_key = "folders"
    folder_name_key = "name"
    snippets_key = "snippets"
    snippet_shortcut_key = "shortcut"
    snippet_text_key = "text"
    espanso_file_extension = ".yml"
    replacer_character = "\\"
