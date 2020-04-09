# apcaccess

apcaccess is a python library that replicates the functionality provided by the ```apcaccess``` tool. A TCP connection is made to the ```apcupsd``` daemon and the results of a ```status``` command are parsed and returned as a python ```dict```.

## Usage

See `apcaccess.py` for a basic implementation:

```
usage: apcaccess.py [-h] [--host HOST] [--port PORT] [--timeout TIMEOUT]
                    [--no_units]

optional arguments:
  -h, --help         show this help message and exit
  --host HOST        APCUPSD hostname or ip address
  --port PORT        APCUPSD port
  --timeout TIMEOUT  Socket timeout
  --no_units         Strip units from values
```