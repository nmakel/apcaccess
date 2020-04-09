import socket


class apcaccess:

    SOCK_CMD = "\x00\x06status".encode()
    SOCK_EOF = "  \n\x00\x00"
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

    def get(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(self.timeout)
            s.connect((self.host, self.port))
            s.send(self.SOCK_CMD)

            buffer = ""

            while not buffer.endswith(self.SOCK_EOF):
                buffer += s.recv(self.SOCK_BUF).decode()

            return buffer
        except ConnectionRefusedError:
            print(f"Connection refused by {self.host}:{self.port}")
        except (socket.timeout, socket.gaierror):
            print(f"Unable to connect to {self.host}:{self.port}")
        finally:
            s.close()

        return False

    def parse(self, raw, no_units):
        parsed = {}
        lines = [x[1:-1] for x in raw[:-len(self.SOCK_EOF)].split("\x00") if x]

        if no_units:
            lines = self.strip_units(lines)

        for line in lines:
            values = line.split(":", 1)
            parsed[values[0].strip()] = values[1].strip()

        return parsed

    def strip_units(self, lines):
        for line in lines:
            for unit in self.units:
                if line.endswith(f" {unit}"):
                    line = line[:(-1-len(unit))]

            yield line

    def status(self, no_units=False):
        raw = self.get()
        output = {}

        if raw:
            for k, v in self.parse(raw, no_units).items():
                output[k] = v
        
        return output
