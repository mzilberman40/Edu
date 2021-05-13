"""
Doc:
https://docs.python.org/3/library/logging.html

Cources:

Oleg Molchanov
https://www.youtube.com/watch?v=qqdgynJ5ATU
https://www.patreon.com/posts/karta-kursa-v-32537851

"""
import logging

logging.basicConfig()

app_logger = logging.getLogger('app_logger')
# print(app_logger)
# print(app_logger.parent)
# print(app_logger.handlers)

utils_logger = logging.getLogger('app_logger.utils_logger')
# print(utils_logger)
# print(utils_logger.parent)
utils_logger.setLevel(logging.DEBUG)
# print(utils_logger.handlers)

root_logger = app_logger.parent
# print(root_logger)
# print(root_logger.parent)
# print(root_logger.handlers)

utils_logger.propagate = False  # Выключает всплывание сообщений в иерархии логгеров

console_handler = logging.StreamHandler()
app_logger.addHandler(console_handler)
# или так:
# app_logger.handlers.append(console_handler)

f = logging.Formatter(fmt="%(levelname)s - %(name)s - %(message)s")
console_handler.setFormatter(f)

utils_logger.addHandler(console_handler)


def main():
    msg = "Hello from logger"
    utils_logger.debug(msg)


if __name__ == "__main__":
    main()
