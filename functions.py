import yaml
import os

PARAMS = []


def validate_config(config):
    """
    validates all input from config file
    Makes dest directory if it doesn't exist

    Example Valid Config
    =======
    src: /home/fargus/Pictures/
    dest: /tmp/SortWallpaper/
    exclude:
      - excludeme
    verbose: false
    params:
      Desktop:
        min_width: 1500
        min_height: 900
        min_ratio: 1.3
        max_ratio: 1.9
      Phone:
        min_width: 720
        min_height: 1500
        min_ratio: 0.36
        max_ratio: 0.76
    """
    assert "src" in config
    if not os.path.isdir(config["src"]):
        raise TypeError("invalid source directory")

    assert "dest" in config
    if not isinstance(config["dest"], str):
        raise TypeError("destination must be string")

    assert "exclude" in config
    if not isinstance(config["exclude"], list):
        raise TypeError("invalid exclude list")

    assert "verbose" in config
    assert isinstance(config["verbose"], bool)

    assert "params" in config
    assert len(config["params"]) != 0
    for x in config["params"]:
        assert "min_width" in config["params"][x]
        assert "min_height" in config["params"][x]
        assert "min_ratio" in config["params"][x]
        assert "max_ratio" in config["params"][x]


def load_config():
    """
    Loads config.yml
    validates it
    creates nessisary directories
    """
    with open(CONFIG_FILE, "r") as ymlconf:
        config = yaml.load(ymlconf, Loader=yaml.FullLoader)

    validate_config(config)

    if not os.path.isdir(config["dest"]):
        try:
            os.mkdir(config["dest"])
        except FileNotFoundError:
            print(
                "Error: unable to create destination directory, check your dest value: %s"
                % config["dest"]
            )
            exit(-2)

    for param in config["params"]:
        try:
            os.mkdir(os.path.join(config['dest'], param))
            print('warning: created ', os.path.join(config['dest'], param))
        except FileExistsError:
            pass
        PARAMS.append(param)

    return config


# loading settings
CONFIG_FILE = "config.yml"
CONFIG = load_config()
