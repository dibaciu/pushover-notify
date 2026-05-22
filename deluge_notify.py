#!/usr/bin/python
import configparser
import http.client, urllib
import os
import sys

from dataclasses import dataclass

CONFIG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'deluge_notify.cfg')
EVENTS = {
    'add': 'Torrent Added',
    'remove': 'Torrent Removed',
    'complete': 'Torrent Completed',
}

@dataclass(kw_only=True)
class PushoverConfig:
    user_key: str
    api_key: str


def get_config(config_file: str)->PushoverConfig:
    config = configparser.ConfigParser(allow_unnamed_section=True)
    config.read(config_file)
    pushover_config = PushoverConfig(
        user_key=config.get(configparser.UNNAMED_SECTION, 'user_key'),
        api_key=config.get(configparser.UNNAMED_SECTION, 'deluge_pushover_token')
    )
    return pushover_config

config = get_config(CONFIG_FILE)

try:
    torrent_id = sys.argv[1]
    torrent_name = sys.argv[2]
    save_path = sys.argv[3]
except IndexError:
    print(f'Usage: {sys.argv[0]} torrent_id torrent_name save_path')
    sys.exit(255)

try:
    event = [value for key, value in EVENTS.items() if key in sys.argv[0]][0]
except IndexError:
    event = 'Unknown Event'

conn = http.client.HTTPSConnection('api.pushover.net:443')
conn.request("POST", '/1/messages.json',
             urllib.parse.urlencode({
                 'token': f'{config.api_key}',
                 'user': f'{config.user_key}',
                 'device': 'iphone',
                 'message': f'{event}: {torrent_name}',
             }),
             {'Content-type': 'application/x-www-form-urlencoded'})
response = conn.getresponse()
