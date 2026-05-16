#!/usr/bin/env python3
"""quick-hash – compute SHA‑256 hashes for files or stdin.

Features:
  * Single‑file implementation, no external packages.
  * Idempotent: identical input always yields identical output.
  * Clear error handling with concise log messages.
"""
import argparse
import hashlib
import sys
from pathlib import Path

def hash_stream(stream):
    """Return SHA‑256 hex digest of data read from *stream*.
    Reads in 64 KB chunks to keep memory usage low.
    """
    hasher = hashlib.sha256()
    for chunk in iter(lambda: stream.read(65536), b''):
        hasher.update(chunk)
    return hasher.hexdigest()

def main():
    parser = argparse.ArgumentParser(description='Compute SHA‑256 hash of a file or stdin.')
    parser.add_argument('source', help='Path to file or "-" for stdin')
    parser.add_argument('-o', '--output', metavar='FILE', help='Write hash to FILE instead of stdout')
    args = parser.parse_args()

    # Determine input stream
    if args.source == '-':
        stream = sys.stdin.buffer
    else:
        try:
            stream = open(args.source, 'rb')
        except OSError as e:
            sys.stderr.write(f'Error opening "{args.source}": {e}\n')
            sys.exit(1)

    # Compute hash
    try:
        digest = hash_stream(stream)
    finally:
        if args.source != '-':
            stream.close()

    # Output handling
    if args.output:
        try:
            Path(args.output).write_text(digest + '\n')
        except OSError as e:
            sys.stderr.write(f'Error writing to "{args.output}": {e}\n')
            sys.exit(1)
    else:
        print(digest)

if __name__ == '__main__':
    main()
