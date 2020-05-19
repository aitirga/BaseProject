import yaml
from box import Box
import os
from dotenv import load_dotenv, find_dotenv
import logging.config

load_dotenv(dotenv_path=f"{os.getcwd()}\.env")
env = os.environ["ENVIRONMENT"]
env_config = os.environ["GENERAL_CONFIG_FILE"]
env_logging = os.environ["LOGGING_CONFIG_FILE"]
env_model = os.environ["MODEL_CONFIG_FILE"]

config_path = os.path.abspath(env_config)
with open(config_path) as yml_file:
    full_cfg = Box(yaml.safe_load(yml_file), default_box=True)
    full_cfg.base.path.root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

cfg = Box({**full_cfg["base"], **full_cfg[env]}, default_box=True, default_box_attr=None)

os.makedirs(cfg.path.logs, exist_ok=True)
log_config_path = env_logging
if os.path.exists(log_config_path):
    with open(log_config_path, "r") as log_config_file:
        log_config = yaml.safe_load(log_config_file)
    logging.config.dictConfig(log_config)
else:
    raise FileNotFoundError(f"Log yaml configuration file not found on {log_config_path}")
