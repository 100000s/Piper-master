# serializeBTC.py - Realistic Bitcoin serialization helpers for Piper
# This is a minimal implementation based on typical Bitcoin serialization logic.
# You may need to expand this based on further usage in wallet_enc.py or other files.

import struct
import binascii

# Example: pack/unpack integers in little-endian

def ser_uint256(u):
    """Serialize a 256-bit integer as 32 bytes, little-endian."""
    return u.to_bytes(32, 'little')

def deser_uint256(b):
    """Deserialize 32 bytes as a 256-bit integer, little-endian."""
    return int.from_bytes(b, 'little')

def ser_compact_size(size):
    """Serialize a variable-length integer (Bitcoin's compact size)."""
    if size < 253:
        return struct.pack('<B', size)
    elif size < 0x10000:
        return b'\xfd' + struct.pack('<H', size)
    elif size < 0x100000000:
        return b'\xfe' + struct.pack('<I', size)
    else:
        return b'\xff' + struct.pack('<Q', size)

def ser_string(s):
    """Serialize a string with compact size prefix."""
    if isinstance(s, str):
        s = s.encode('utf-8')
    return ser_compact_size(len(s)) + s

def hash256(s):
    import hashlib
    return hashlib.sha256(hashlib.sha256(s).digest()).digest()

# Add more functions as needed for your wallet_enc.py usage.
