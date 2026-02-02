# Minimal hdm.py for Piper
# This is a placeholder for HD wallet/seed functionality.
# Replace with a real implementation for production use.

class HDMWallet:
    def __init__(self, *args, **kwargs):
        self.seed = None
    def generate_seed(self):
        self.seed = 'mock-seed-phrase'
        return self.seed
    def get_seed(self):
        return self.seed or 'mock-seed-phrase'
    def get_xpub(self):
        return 'mock-xpub'
    def get_xprv(self):
        return 'mock-xprv'
