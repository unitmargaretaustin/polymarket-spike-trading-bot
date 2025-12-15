import time
from automation.tasks import SpikeScanner

class Scheduler:
    def __init__(self, settings, logger):
        self.settings = settings
        self.logger = logger
        self.scanner = SpikeScanner(settings, logger)

    def run(self):
        interval = self.settings["scan_interval_seconds"]

        while True:
            try:
                self.scanner.scan_markets()
            except Exception as e:
                self.logger.exception(f"Scheduler error: {e}")

            time.sleep(interval)
