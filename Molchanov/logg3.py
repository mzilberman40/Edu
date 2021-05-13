import logging.config
from log_settings import logger_config
import requests

logging.config.dictConfig(logger_config)

logger = logging.getLogger('app_logger')


def main():
    url = "https://www.google.com"
    message = "Hello from my logger"
    logger.debug(message)
    r = requests.get(url)
    print(r)


if __name__ == "__main__":
    main()
