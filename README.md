# pushover-notify

A lightweight Python script for sending [Pushover](https://pushover.net/) notifications from [Deluge](https://deluge-torrent.org/) torrent client events (torrent added, removed, or completed).

## How it works

Deluge supports running external scripts on torrent events. This script is designed to be called by Deluge with the torrent ID, name, and save path as arguments. It reads your Pushover credentials from a config file and sends a push notification to your device.

The event type (add / remove / complete) is determined by the **name of the script** (or symlink) used to invoke it — so you create one symlink per event.

## Requirements

- Python 3.10+
- A [Pushover](https://pushover.net/) account with:
  - A **User Key**
  - An **Application API Token**

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/dibaciu/pushover-notify.git
   cd pushover-notify
   ```

2. **Create the config file** from the example:
   ```bash
   cp deluge_notify.cfg.example deluge_notify.cfg
   ```

3. **Edit `deluge_notify.cfg`** with your Pushover credentials:
   ```ini
   user_key = <your pushover user key>
   deluge_pushover_token = <your pushover application token>
   ```

4. **Create symlinks** for each event type you want to handle:
   ```bash
   ln -s deluge_notify.py deluge_add.py
   ln -s deluge_notify.py deluge_remove.py
   ln -s deluge_notify.py deluge_complete.py
   ```

5. **Make the script executable:**
   ```bash
   chmod +x deluge_notify.py
   ```

## Deluge configuration

In Deluge, go to **Preferences → Execute** and add a command for each event:

| Event             | Command                          |
|-------------------|----------------------------------|
| Torrent Added     | `/path/to/deluge_add.py`     |
| Torrent Removed   | `/path/to/deluge_remove.py`  |
| Torrent Completed | `/path/to/deluge_complete.py`|

Deluge passes three arguments automatically: `torrent_id`, `torrent_name`, and `save_path`.

## Config file

The script always reads `deluge_notify.cfg` from the **same directory as the script**, regardless of the working directory from which it is invoked.

| Key                    | Description                        |
|------------------------|------------------------------------|
| `user_key`             | Your Pushover user key             |
| `deluge_pushover_token`| Your Pushover application token    |

## License

MIT

