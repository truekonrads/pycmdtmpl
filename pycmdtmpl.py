import logging
import argparse

#CHANGME: Add the name of the logger - e.g. your program name
LOGGER = logging.getLogger("My amazing program")
LOGGER.setLevel(logging.INFO)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def main():
    
    #CHANGME: Describe what your program does
    parser = argparse.ArgumentParser(description='Do something useful')
    parser.add_argument('--debug', "-d", action="store_true",
                        help='Debug level messages')
    
    args = parser.parse_args()
    if args.debug:
        LOGGER.setLevel(logging.DEBUG)
    
if __name__ == '__main__':
    main()