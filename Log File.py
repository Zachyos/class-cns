import os
os.system('cls')
import logging
from colored import fg, bg, attr
from stat import filemode

name_log = ( input("Name your log file: "))

logging.basicConfig(filename=name_log,
                    format='%(asctime)s %(message)s',
                    filemode='w')
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)
txt = ( input("Enter what you would like to log: "))
logger.debug(txt)

print("%s%sLog File has been successfully created%s" % (fg(11), bg(0), attr(0)))
