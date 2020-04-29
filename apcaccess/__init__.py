import socket
import time


class APCAccess:

    SOCK_CMD = "\x00\x06status".encode()
    SOCK_EOF = "\n\x00\x00"
    SOCK_BUF = 1024

    units = (
        "Minutes",
        "Seconds",
        "Percent",
        "Volts",
        "Watts",
        "Amps",
        "Hz",
        "C",
        "VA",
        "Percent Load Capacity"
    )

    def __init__(self, host="localhost", port=3551, timeout=5):
        self.host = host
        self.port = port
        self.timeout = timeout

    def _get_status(self):
        buffer = ""

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(self.timeout)
            sock.connect((self.host, self.port))
            sock.send(self.SOCK_CMD)

            t_start = time.monotonic()

            while not buffer.endswith(self.SOCK_EOF):
                buffer += sock.recv(self.SOCK_BUF).decode()

                if (time.monotonic() - t_start) > self.timeout:
                    raise socket.timeout

        return buffer

    def _parse(self, raw, no_units):
        parsed = {}
        lines = [x[1:-1] for x in raw[:-len(self.SOCK_EOF)].split("\x00") if x]

        if no_units:
            lines = self._strip_units(lines)

        for line in lines:
            values = line.split(":", 1)
            parsed[values[0].strip()] = values[1].strip()

        return parsed

    def _strip_units(self, lines):
        for line in lines:
            for unit in self.units:
                if line.endswith(f" {unit}"):
                    line = line[:(-1 - len(unit))]

            yield line

    def status(self, no_units=False):
        return self._parse(self._get_status(), no_units)
