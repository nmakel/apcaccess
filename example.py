#!/usr/bin/env python3

import apcaccess
import argparse


if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument("address", type=str, default="localhost", help="APCUPSD hostname or ip address")
    argparser.add_argument("-p", "--port", type=int, default=3551, help="APCUPSD port")
    argparser.add_argument("-t", "--timeout", type=int, default=5, help="Socket timeout")
    args = argparser.parse_args()

    try:
        ups = apcaccess.APCAccess(
            host=args.address,
            port=args.port,
            timeout=args.timeout
        )

        for k,v in ups.status(no_units=False).items():
            print(f"{k}: {v}")
    except Exception as e:
        print(f"Error: {e}")