LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'mylogger': {
            'handlers': ['console'],
            'level': 'INFO',
        },
    },
}
