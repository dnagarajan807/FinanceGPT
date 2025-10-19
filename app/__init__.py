"""
FinanceGPT App Package Initialization
-------------------------------------
This file marks the 'app' directory as a Python package and 
can also be used to define shared package-level initialization logic.
"""

import logging

# Configure basic logging for the package
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

# Optional: define what gets imported when doing 'from app import *'
__all__ = ["config", "data_loader", "vector_store", "rag_pipeline", "router"]
