#!/usr/bin/env python3
import argparse
from datetime import datetime

def main():
    p = argparse.ArgumentParser(description="Simple QA hello CLI")
    p.add_argument("--name", "-n", default="QA Engineer", help="Your name")
    p.add_argument("--repeat", "-r", type=int, default=1, help="How many times to print")
    args = p.parse_args()

    stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for _ in range(max(1, args.repeat)):
        print(f"[{stamp}] Hello, {args.name}! Ready to test.")

if __name__ == "__main__":
    main()
