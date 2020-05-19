import yaml
from box import Box
import os


config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'configs/config.yaml'))
with open(config_path) as yml_file:
    cfg = Box(yaml.safe_load(yml_file))