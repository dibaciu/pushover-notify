#!/usr/bin/python
import argparse
import configparser
import http.client, urllib
import os
import sys

from dataclasses import dataclass

CONFIG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pushover_notify.cfg')


@dataclass(kw_only=True)
class PushoverConfig:
    user_key: str
    api_key: str


def get_config(config_file: str) -> PushoverConfig:
    config = configparser.ConfigParser(allow_unnamed_section=True)
    config.read(config_file)
    return PushoverConfig(
        user_key=config.get(configparser.UNNAMED_SECTION, 'user_key'),
        api_key=config.get(configparser.UNNAMED_SECTION, 'pushover_token')
    )


def get_message() -> str:
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--message', type=str, default=None)
    args = parser.parse_args()

    if args.message:
        return args.message

    if not sys.stdin.isatty():
        return sys.stdin.read().strip()

    parser.print_usage()
    sys.exit(1)


config = get_config(CONFIG_FILE)
message = get_message()

conn = http.client.HTTPSConnection('api.pushover.net:443')
conn.request("POST", '/1/messages.json',
             urllib.parse.urlencode({
                 'token': config.api_key,
                 'user': config.user_key,
                 'device': 'iphone',
                 'message': message,
             }),
             {'Content-type': 'application/x-www-form-urlencoded'})
response = conn.getresponse()
