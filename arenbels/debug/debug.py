from sys import argv

#importing module of log
import logging

def init_logger(p=False):
    """Create and configure a logger, then returns it

    In: p , whether the activated level is printed
        argv is used :
            List of all debugging levels:
            python3 arenbels.py ld  -> Debug
            python3 arenbels.py li  -> Info
            python3 arenbels.py lw  -> Warning
            python3 arenbels.py le  -> Error
            python3 arenbels.py lc  -> Critical
            python3 arenbels.py     -> Info

    Out: logger object"""
    logging.basicConfig(filename="log.log",
                        format='%(asctime)s %(levelname)s\t%(message)s',
                        filemode='w')

    #Creating an object
    logger = logging.getLogger()

    #Setting the threshold of logger to DEBUG
    if len(argv)>1:
        if 'ld' in argv:
            logger.setLevel(logging.DEBUG)
        elif 'li' in argv:
            logger.setLevel(logging.INFO)
        elif 'lw' in argv:
            logger.setLevel(logging.WARNING)
        elif 'le' in argv:
            logger.setLevel(logging.ERROR)
        elif 'lc' in argv:
            logger.setLevel(logging.CRITICAL)
        else:
            print("""
            List of all debugging levels:
            python3 arenbels.py ld  -> Debug
            python3 arenbels.py li  -> Info
            python3 arenbels.py lw  -> Warning
            python3 arenbels.py le  -> Error
            python3 arenbels.py lc  -> Critical
            python3 arenbels.py     -> Info
                    """)
            logger.setLevel(logging.INFO)
    else:
        logger.setLevel(logging.INFO)

    if p:
        print_levels(logger)

    return logger

def print_levels(logger):
    """ Prints the levels at which is the logger """
    #True iff debugging state
    DEBUG = logger.level < logging.CRITICAL


    #Test messages
    if DEBUG:
        logger.debug("Level : Debug ")
        logger.info("Level : Info or Lower ")
        logger.warning("Level : Warning or Lower")
        logger.error("Level : Error or lower")
    logger.critical("Level : Any #This message should always be in the log")

def f(*args):
    """ formats a text like a print """
    txt = ""
    for a in args:
        txt += str(a)
    return txt

logger = init_logger()