import logging
from logger import logger

def log_error(context: str, error: Exception):
    logger.error(f"[{context}] Error: {str(error)}", exc_info=True)

# Example usage:
# try:
#     some_function()
# except Exception as e:
#     log_error("some_function", e)
