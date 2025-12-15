import random

class ProxyManager:
    def __init__(self, proxies):
        self.proxies = proxies or []

    def get_proxy(self):
        if not self.proxies:
            return None
        return random.choice(self.proxies)
