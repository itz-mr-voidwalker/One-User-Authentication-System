from auth.logging import Logger
from auth.SecureLayer import SecureLayer
from auth.onboarding.setup import Setup
from auth.login import Login

logger = Logger()


class Directing:
    def __init__(self):
        
        try:
            self.directing()
        except Exception as e:
            logger.error(f"Error occurred during directing process: {e}")
    
    def directing(self):
        try:
            logger.info("Starting the user flow.")
            enc = SecureLayer()
            chks = enc.chk_if_exits()
            if chks:
                logger.info("Encrypted data found, proceeding with login.")
                login = Login()
            else:
                logger.info("No encrypted data found, proceeding with setup.")
                setup = Setup()
        except Exception as e:
            logger.error(f"Error occurred during directing process: {e}")

def main():
    try:
        logger.info("Starting the main program.")
        obj = Directing()
    except Exception as e:
        logger.error(f"Unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
