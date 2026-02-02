# Piper Wallet (Windows Edition)

Piper is a Python-based tool for generating and printing secure cryptocurrency paper wallets. This version is updated for Python 3 and Windows compatibility.

## Features
- Print single or bulk wallets for Bitcoin and altcoins
- Shamir's Secret Sharing (SSSS) for splitting secrets
- QR code generation for keys and passwords
- Settings and coin management via GUI
- SQLite database for settings and key storage

## Requirements
- Python 3.7+
- Windows OS (tested on Windows 10/11)
- [vanitygen.exe](https://github.com/samr7/vanitygen) (must be in the Piper-master directory)

## Python Dependencies
Install all required packages with:

    pip install -r requirements.txt

## Setup
1. Clone or extract this repository.
2. Ensure `vanitygen.exe` is present in the Piper-master directory.
3. Initialize the databases (if not already present):

    python init_db.py
    python init_keys_db.py

4. (Optional) If you see errors about missing settings or coin types, run:

    python fix_settings.py
    python fix_coinformats.py

5. Start the GUI:

    python gui.py

## Usage
- Use the GUI to print wallets, view keys, manage settings, and add altcoins.
- All wallet data is stored in `keys.db3` and settings in `settings.db3`.
- Serial numbers are tracked in `serialnumber.txt`.

## Troubleshooting
- If you see errors about missing settings or tables, run the provided fix scripts.
- If you see `FileNotFoundError` for `vanitygen.exe`, download it and place it in the project directory.
- For Python errors, ensure you are using Python 3 and all dependencies are installed.

## License
This project is licensed under the GNU GPL v3. See license.txt for details.

## Credits
- Original author: Christopher Cassano
- Windows/Python 3 migration: Community
