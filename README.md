# pushover-notify

A lightweight Python script for sending arbitrary [Pushover](https://pushover.net/) notifications from the command line. Pass a message via argument or pipe it through stdin.

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
   cp pushover_notify.cfg.example pushover_notify.cfg
   ```

3. **Edit `pushover_notify.cfg`** with your Pushover credentials:
   ```ini
   user_key = <your pushover user key>
   pushover_token = <your pushover application token>
   ```

4. **Make the script executable:**
   ```bash
   chmod +x pushover_notify.py
   ```

## Usage

```bash
# Pass message as an argument
pushover_notify.py --message "Hello from the terminal"
pushover_notify.py -m "Hello from the terminal"

# Pipe message from stdin
echo "Hello from the terminal" | pushover_notify.py

# Pipe multi-line output
some_command | pushover_notify.py
```

## Config file

The script always reads `pushover_notify.cfg` from the **same directory as the script**, regardless of the working directory from which it is invoked.

| Key               | Description                     |
|-------------------|---------------------------------|
| `user_key`        | Your Pushover user key          |
| `pushover_token`  | Your Pushover application token |


## License

MIT
