#!/usr/bin/env python3

import apcaccess
import argparse
import json
import socket


if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument("--host", type=str, default="localhost", help="apcupsd host name or ip address")
    argparser.add_argument("--port", type=int, default=3551, help="apcupsd port")
    argparser.add_argument("--timeout", type=int, default=5, help="Socket timeout")
    argparser.add_argument("--no_units", default=False, action="store_true", help="Strip units from values")
    argparser.add_argument("--json", action="store_true", default=False, help="Output as JSON")
    args = argparser.parse_args()

    try:
        apc = apcaccess.APCAccess(
            host=args.host,
            port=args.port,
            timeout=args.timeout
        )

        if args.json:
            print(json.dumps(apc.status(no_units=args.no_units), indent=4))
        else:
            for k, v in apc.status(no_units=args.no_units).items():
                print(f"{k}: {v}")
    except ConnectionRefusedError:
        print(f"Connection refused: {args.host}:{args.port}")
    except (socket.herror, socket.gaierror):
        print(f"Connection failed: {args.host}:{args.port}")
    except socket.timeout:
        print(f"Connection timed out: {args.host}:{args.port}")
