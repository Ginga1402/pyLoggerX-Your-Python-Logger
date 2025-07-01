from logger.custom_logger import get_logger

logger = get_logger("demo_logger")

def demonstrate_logging_levels():
    """
    Demonstrates the usage of all logging levels.
    """
    logger.debug("DEBUG: Useful for diagnosing problems, used mainly during development.")
    logger.info("INFO: General operational messages, confirming things are working as expected.")
    logger.warning("WARNING: Indicates something unexpected, or potential issue in the future.")
    logger.error("ERROR: A more serious problem, something failed.")
    logger.critical("CRITICAL: A serious error, indicating the program itself may not be able to continue.")

    try:
        value = 10 / 0
    except ZeroDivisionError:
        logger.exception("EXCEPTION: Captures the stack trace along with the error message.")

# Call the function to see the logs in action
demonstrate_logging_levels()
