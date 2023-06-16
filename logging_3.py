#try and expect block under logging

import logging
logging.basicConfig(filename="test3.log", level=logging.INFO ,format='%(asctime)s %(name)s %(levelname)s %(message)s')
def devide (a,b):
    logging.info("the value entered by user are %s and %s" ,a,b)
    try:
        logging.info("we are into functon")
        div= a/b
        logging.info("we have done the division and the answer is %s",div)
        return div
    except Exception as e:
        logging.exception(e)

print(devide(3,97))
print(devide(3,0))

"""
log file contains
2023-06-17 00:30:01,182 root INFO the value entered by user are 3 and 97
2023-06-17 00:30:01,182 root INFO we are into functon
2023-06-17 00:30:01,182 root INFO we have done the division and the answer is 0.030927835051546393
2023-06-17 00:30:01,183 root INFO the value entered by user are 3 and 0
2023-06-17 00:30:01,183 root INFO we are into functon
2023-06-17 00:30:01,183 root ERROR division by zero
Traceback (most recent call last):
