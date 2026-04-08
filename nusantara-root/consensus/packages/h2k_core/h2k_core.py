import hashlib

class H2KCore:
    def generate_key(self, heartbeat_signal):
        # Heartbeat sebagai entropy murni
        entropy = hashlib.sha256(str(heartbeat_signal).encode()).hexdigest()
        return entropy # Akan diproses oleh aksara-logic
