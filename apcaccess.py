#!/usr/bin/env python3

import apcaccess
import argparse
import json


if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument("--host", type=str, default="localhost", help="apcupsd hostname or ip address")
    argparser.add_argument("--port", type=int, default=3551, help="apcupsd port")
    argparser.add_argument("--timeout", type=int, default=5, help="Socket timeout")
    argparser.add_argument("--no_units", default=False, action="store_true", help="Strip units from values")
    argparser.add_argument("--json", action="store_true", default=False, help="Output as JSON")
    args = argparser.parse_args()

    try:
        ups = apcaccess.apcaccess(
            host=args.host,
            port=args.port,
            timeout=args.timeout
        )

        if args.json:
            print(json.dumps(ups.status(no_units=args.no_units), indent=4))
        else:
            for k, v in ups.status(no_units=args.no_units).items():
                print(f"{k}: {v}")
    except Exception as e:
        print(f"Error: {e}")
