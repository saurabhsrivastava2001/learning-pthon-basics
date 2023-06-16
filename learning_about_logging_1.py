import logging
logging.basicConfig(filename="test.log", level=logging.INFO)
logging.info("this is my(saurabh sriv's )first logging")
logging.warning("first warning")
logging.error("this is a system massage from system")
l=[2,34,35,325,5,5,52,33]
for i in l:
    if (i==325):
        logging.info(i)
        logging.warning("value found")
logging.shutdown()
