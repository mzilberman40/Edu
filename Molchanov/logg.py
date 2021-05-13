"""
Doc:
https://docs.python.org/3/library/logging.html

Cources:

Oleg Molchanov
https://www.youtube.com/watch?v=qqdgynJ5ATU
https://www.patreon.com/posts/karta-kursa-v-32537851

"""


import logging
import requests


logger = logging.getLogger()
# print(logger.handlers)
# logging.basicConfig(level=logging.NOTSET, filename='logger.log')
logging.basicConfig(level=logging.NOTSET)

#
# print(logger)
# print(logger.level)
# logger.setLevel(logging.DEBUG)  # меняет только уровень обработчика, но не уровень хэндлера
# print(logger)
# print()
# print(logger.handlers)


# Посмотреть все задействованные логгеры:
for key in logging.Logger.manager.loggerDict:
    print(key)

logging.getLogger('urllib3').setLevel(logging.CRITICAL)

def main():
    # print(logging.NOTSET)
    # print(logging.DEBUG)
    # print(logging.INFO)
    # print(logging.WARNING)
    # print(logging.ERROR)
    # print(logging.CRITICAL)
    msg = "Msg for logger"
    logger.debug(msg)
    # logger.info(msg)
    # logger.warning(msg)
    # logger.error(msg)
    # logger.critical(msg)
    # logger = logging.logg
    # print(logger)
    url = "https://www.google.com"
    r = requests.get(url)


if __name__ == "__main__":
    main()
