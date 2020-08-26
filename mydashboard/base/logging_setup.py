import logging
import sys


class BaseFilter(logging.Filter):
    app_name=None
    space=None

    def filter(self, record):
        record.app_name=self.app_name
        record.space=self.space
        return True


def generate_logging_config():

    class Filter(BaseFilter):
        app_name = 'mydashboard'
        space = 'DEV'

    logging_config = \
        {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'verbose': {
                'class': 'logging.Formatter',
                'format': '{levelname} timestamp=%{asctime}s {module} {process:d} {thread:d} {message}',
                'style': '{',
            },
            'default': {
            'format': '{levelname} {message}',
            'style': '{',
            },
        },
        'filters': {
            'base_filter': {'()': Filter},
        },
        'handlers': {
            'stdout': {
                'class': 'logging.StreamHandler',
                'formatter': 'verbose',
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
        }
    }
    return logging_config
