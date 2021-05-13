import logging.config
from log_settings import logger_config

logging.config.dictConfig(logger_config)
logger = logging.getLogger('app_logger')


def main():
    try:
        x = 3 / 0
    except Exception as err:
        logger.exception(f"Exception:  {err} ")


if __name__ == "__main__":
    main()
