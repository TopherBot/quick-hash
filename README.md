# quick-hash

A minimal, single‑file Python tool that prints the SHA‑256 hash of a file or standard input.

## Installation

```bash
# Clone the repository (public)
git clone https://github.com/yourname/quick-hash.git
cd quick-hash
# No dependencies – just run the script
python3 quick_hash.py --help
```

## Usage

```bash
# Hash a file
python3 quick_hash.py path/to/file.txt

# Hash data from stdin
cat file.txt | python3 quick_hash.py -

# Write hash to a file
python3 quick_hash.py path/to/file.txt -o hash.txt
```

## Options

- `-` : read from stdin.
- `-o <file>` : write the resulting hash to `<file>` instead of stdout.
- `-h, --help` : show help.

## License

MIT – see LICENSE file.
