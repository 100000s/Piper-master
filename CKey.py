# Minimal CKey class for Piper (for BIP38 and wallet_enc.py)
# This is a placeholder. For real security, use a vetted implementation!

class CKey:
    def __init__(self):
        self._privkey = None
        self._compressed = False

    def generate(self, privkey_bytes):
        self._privkey = privkey_bytes

    def set_compressed(self, compressed):
        self._compressed = compressed

    def get_privkey(self):
        return self._privkey

    def is_compressed(self):
        return self._compressed
