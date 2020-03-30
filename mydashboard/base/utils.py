import os


def get_os_environ(key):

    try:
        return str(os.environ[key])
    except KeyError:
        raise EnvironmentError(
            "Value:{} not set in the environment variable.Please set".format(key)
        )
