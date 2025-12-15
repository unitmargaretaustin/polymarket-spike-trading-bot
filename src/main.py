from automation.scheduler import Scheduler
from automation.utils.config_loader import load_settings
from automation.utils.logger import setup_logger

def main():
    settings = load_settings()
    logger = setup_logger()

    logger.info("Starting Polymarket Spike Trading Bot")

    scheduler = Scheduler(settings, logger)
    scheduler.run()

if __name__ == "__main__":
    main()
