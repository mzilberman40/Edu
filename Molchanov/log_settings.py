import logging

logger_config = {
    'version': 1,   # mandatory key - value
    'disable_existing_loggers': False,   # отключает все логгеры системы, не описанные в этом файле, кроме корневого
    'formatters': {
        'std_formatter': {
            'format': "{asctime} - {levelname} - {name} - {module}:{funcName}:{lineno} - {message}",
            'style': '{'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': logging.DEBUG,
            'formatter': 'std_formatter'
        }
    },

    'loggers': {
        'app_logger': {
            'level': logging.DEBUG,
            'handlers': ['console'],
            'propagate': False
        }
    },
    # 'filters': {},
    # 'root': {},
    # 'incremental': True     # указывает, что этот файл конфигурации дополнительный к другому

}