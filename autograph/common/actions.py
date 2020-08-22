# Definition ==========================================================
#
# Contains helper functions to perform actions of the UI widgets.
# This file's functions should also standalone if necessary, the UI
# only provides a means to call this set of functions.
#
# Imports =============================================================

# Standard Libraries
import logging
import time

# =====================================================================

def test_logging():
    """This function serves to test the various levels of logging and
    the ability of each handler to emit messages.
    THIS IS INTENDED TO BE A TEMPORARY FUNCTION, to assist in the
    implementation of logging functionality while the logging branch
    is in active development.
    """
    logging.debug('This is a DEBUG-level log.')
    time.sleep(0.5)
    logging.info('This is an INFO-level log.')
    time.sleep(0.5)
    logging.warning('This is a WARNING-level log.')
    time.sleep(0.5)
    logging.error('This is an ERROR-level log.')