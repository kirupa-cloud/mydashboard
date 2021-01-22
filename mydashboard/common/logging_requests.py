import logging
import os
import requests
from requests.adapters import HTTPAdapter
from urllib3 import Retry

DEFAULT_RETRIES = 3
DEFAULT_BACKOFF_FACTOR = 1
DEFAULT_STATUS_FORCELIST = [500, 502, 504]

LOGGER = logging.getLogger(__name__)


def send(method, url, **kwargs):
    headers = kwargs.pop('headers')

    with requests.session() as session:
        if kwargs.pop("retry", False):
            retries = kwargs.pop("retries", DEFAULT_RETRIES)
            backoff_factor = kwargs.pop("backoff_factor", DEFAULT_BACKOFF_FACTOR)
            status_forcelist = kwargs.pop("status_forcelist", DEFAULT_STATUS_FORCELIST)

            _enable_retry(session, retries, backoff_factor, status_forcelist, **kwargs)

        response = session.request(
            method, url, headers=headers, **kwargs,)

        return response


def _enable_retry(session, retries, backoff_factor, status_forcelist, **kwargs):

    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )

    adapter = HTTPAdapter(max_retries=retry)
    session.mount("http://", adapter)
    session.mount("https://", adapter)

    return session
