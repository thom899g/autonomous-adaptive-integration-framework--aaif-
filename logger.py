import logging

def setup_logger(name: str) -> logging.Logger:
    """
    Configure and return a logger with the specified name.
    
    Args:
        name (str): Name of the logger.
        
    Returns:
        logging.Logger: Configured logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    # Prevent adding multiple handlers
    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        
    return logger