# apcaccess

apcaccess is a python library that replicates the functionality provided by the ```apcaccess``` tool. A TCP connection is made to the ```apcupsd``` daemon and the results of a ```status``` command are parsed and returned as a python ```dict```.

## Usage

See `apcaccess.py` for a basic implementation:

```
usage: apcaccess.py [-h] [--host HOST] [--port PORT] [--timeout TIMEOUT]
                    [--no_units] [--json]

optional arguments:
  -h, --help         show this help message and exit
  --host HOST        apcupsd hostname or ip address
  --port PORT        apcupsd port
  --timeout TIMEOUT  Socket timeout
  --no_units         Strip units from values
  --json             Output as JSON
```