# Piper Wallet (Raspberry Pi Edition)

Piper is a Python-based tool for generating and printing secure cryptocurrency paper wallets. This version is updated for Python 3 and Raspberry Pi compatibility, closely matching the original Piper hardware experience.

## Features
- Print single or bulk wallets for Bitcoin and altcoins
- Shamir's Secret Sharing (SSSS) for splitting secrets
- QR code generation for keys and passwords
- Settings and coin management via GUI
- SQLite database for settings and key storage
- Uses Raspberry Pi hardware RNG for high-entropy keys
- Supports TTL thermal printer via GPIO
- "Forget" mode: physical switch disables key saving

## Requirements
- Raspberry Pi 3B, 4, or Zero W
- Raspbian OS (Raspberry Pi OS, 32-bit recommended)
- Python 3.7+
- [vanitygen](https://github.com/samr7/vanitygen) (compiled for ARM, placed in the Piper-master directory)
- Mini TTL Thermal Receipt Printer (connected to Pi GPIO)
- 2.25" (57mm) thermal paper rolls (BPA-free recommended)
- Momentary pushbutton (for print trigger)
- Jumper wires (M/F)
- 16GB+ microSD card
- 5V 4A power supply

## Python Dependencies
Install all required packages with:

    pip3 install -r requirements.txt

## Hardware Setup
1. **Connect the Thermal Printer:**
   - Connect the printer's RX/TX and power lines to the Pi's GPIO pins as per the printer's datasheet.
   - Example: Printer TX to Pi RX (GPIO 15), Printer RX to Pi TX (GPIO 14), GND to GND, VCC to 5V.
2. **Connect the Pushbutton:**
   - Wire the button between a GPIO pin (e.g., GPIO 17) and GND.
   - Configure the pin as input with pull-up in your code.
3. **(Optional) Add "Forget" Switch:**
   - Wire a toggle switch to a GPIO pin to control whether keys are saved to SD card.

## OS & Software Setup
1. Flash Raspberry Pi OS (32-bit) to your SD card.
2. Boot and expand filesystem, enable SSH if needed.
3. Install Python 3 and pip:

    sudo apt update
    sudo apt install python3 python3-pip python3-pil python3-serial

4. Clone or extract this repository to your Pi.
5. Compile vanitygen for ARM (see vanitygen repo for instructions) and place the binary in the Piper-master directory.
6. Initialize the databases (if not already present):

    python3 init_db.py
    python3 init_keys_db.py

7. (Optional) If you see errors about missing settings or coin types, run:

    python3 fix_settings.py
    python3 fix_coinformats.py

8. Start the GUI:

    python3 gui.py

## Usage
- Use the GUI to print wallets, view keys, manage settings, and add altcoins.
- All wallet data is stored in `keys.db3` and settings in `settings.db3`.
- Serial numbers are tracked in `serialnumber.txt`.
- The pushbutton can be used to trigger wallet generation/printing.
- The "forget" switch disables key saving for true cold storage.

## Troubleshooting
- If you see errors about missing settings or tables, run the provided fix scripts.
- If you see `FileNotFoundError` for `vanitygen`, compile it for ARM and place it in the project directory.
- For Python errors, ensure you are using Python 3 and all dependencies are installed.
- For printer issues, check wiring and permissions (add user to `dialout` group if needed).

## License
This project is licensed under the GNU GPL v3. See license.txt for details.

## Credits
- Original author: Christopher Cassano
- Modernization & Pi hardware support: Community

---

## Wiring Diagram & Hardware Notes
- **Thermal Printer:**
  - TX (printer) → RX (GPIO 15, Pi)
  - RX (printer) → TX (GPIO 14, Pi)
  - GND → GND
  - VCC → 5V (ensure sufficient current)
- **Pushbutton:**
  - One side to GPIO 17 (or your choice)
  - Other side to GND
- **Forget Switch:**
  - One side to GPIO 27 (or your choice)
  - Other side to GND

See the original Piper documentation or community guides for detailed wiring photos and troubleshooting.
