import unittest
from baseproject.config import cfg
import yaml
import os
import logging


class ConfigCase(unittest.TestCase):
    def test_config(self):
        config_path = os.path.abspath(os.path.join(__file__, "..", "..", "..", "configs/config.yaml"))
        with open(config_path, "r") as test_file:
            test_dict = yaml.safe_load(test_file)
        self.assertEqual(cfg.path.logs, test_dict["base"]["path"]["logs"])


if __name__ == "__main__":
    unittest.main()