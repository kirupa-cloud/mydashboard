import logging
import sys


class BaseFilter(logging.Filter):
    app_name = None
    space = None

    def filter(self, record):
        record.app_name = self.app_name
        record.space = self.space
        return True


def generate_logging_config():

    class Filter(BaseFilter):
        app_name = 'homeutils'
        space = 'DEV'

    logging_config = \
        {
            'version': 1,
            'disable_existing_loggers': False,
            'formatters': {
                'default': {
                    'class': 'logging.Formatter',
                    'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
                    'style': '{'
                },
                'default1': {
                    'class': 'logging.Formatter',
                    'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
                    'style': '{'
                },
            },
            'filters': {'base_filter': {'()': Filter},
                        },
            'handlers': {
                'stdout': {
                    'class': 'logging.StreamHandler',
                    'formatter': 'default',
                    'stream': sys.stdout,
                    'filters': ['base_filter'],
                },
            },
            'root': {
                'handlers': ['stdout'],
                'level': 'DEBUG',
            },
            'loggers': {
                'django': {
                    'handlers': ['stdout'],
                    'level': 'INFO',
                    'propagate': False,
                },
                'django.request': {
                    'handlers': ['stdout'],
                    'level': 'ERROR',
                    'propagate': False,
                },
            },
        }
    return logging_config
