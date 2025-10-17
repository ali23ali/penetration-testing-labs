#!/usr/bin/env python3
"""Sample auto-recon script (stub)

Usage:
    python3 auto_recon.py target.com
"""
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: auto_recon.py <target>")
        sys.exit(1)
    target = sys.argv[1]
    print(f"Starting quick recon on {target} (this is a stub)...")

if __name__ == '__main__':
    main()
