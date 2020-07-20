"""
    This file setup basic paths for current project
"""

import pathlib
import sys

path_current_file = pathlib.Path(__file__)
path_current_folder = path_current_file.parents[0]

project_root = path_current_file.parents[1]
configs_root = project_root.joinpath("configs")
data_root = project_root.joinpath("presets/data")
logs_root = project_root.joinpath("presets/logs")

sys.path.append(
    str(project_root)
)
sys.path.extend([
    str(project_root),
    str(configs_root),
    str(data_root),
    str(logs_root)
])
