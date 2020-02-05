
from sys import argv


#importing module
import logging

#Create and configure logger
logging.basicConfig(filename="log.log",
                    format='%(asctime)s %(levelname)s\t%(message)s',
                    filemode='w')

#Creating an object
logger = logging.getLogger()

#Setting the threshold of logger to DEBUG
if len(argv)>1:
    if argv[1] == 'd':
        logger.setLevel(logging.DEBUG)
    elif argv[1] == 'i':
        logger.setLevel(logging.INFO)
    elif argv[1] == 'w':
        logger.setLevel(logging.WARNING)
    elif argv[1] == 'e':
        logger.setLevel(logging.ERROR)
    elif argv[1] == 'c':
        logger.setLevel(logging.CRITICAL)
    else:
        print("""
        List of all debugging levels:
        python3 protocol.py d  -> Debug
        python3 protocol.py i  -> Info
        python3 protocol.py w  -> Warning
        python3 protocol.py e  -> Error
        python3 protocol.py c  -> Critical
        python3 protocol.py    -> Info
                """)
        logger.setLevel(logging.INFO)
else:
    logger.setLevel(logging.INFO)

#True iff debugging state
DEBUG = logger.level < logging.CRITICAL


#Test messages
if DEBUG:
    logger.debug("Level : Debug ")
    logger.info("Level : Info or Lower ")
    logger.warning("Level : Warning or Lower")
    logger.error("Level : Error or lower")
logger.critical("Level : Any #This message should always be in the log")
