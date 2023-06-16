import logging
#datw and time of certian edit 
#learned format
#asctime
#name
#levelname
#message

logging.basicConfig(filename="test2.log", level=logging.DEBUG, format='%(asctime)s %(name)s %(levelname)s %(message)s')
logging.info("this is the message with time stamp")


#test2.log----------
#2023-06-16 23:41:31,040 this is the message with time stamp
#2023-06-16 23:42:25,680 root this is the message with time stamp
#2023-06-16 23:42:57,023 root INFO this is the message with time stamp
