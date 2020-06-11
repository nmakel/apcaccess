# apcaccess

apcaccess is a python library and tool that replicates `apcaccess` functionality.

## Usage

See `apcaccess.py` for a basic implementation:

```
usage: apcaccess.py [-h] [--host HOST] [--port PORT] [--timeout TIMEOUT]
                    [--no_units] [--json]

optional arguments:
  -h, --help         show this help message and exit
  --host HOST        apcupsd host name or ip address
  --port PORT        apcupsd port
  --timeout TIMEOUT  Socket timeout
  --no_units         Strip units from values
  --json             Output as JSON
```