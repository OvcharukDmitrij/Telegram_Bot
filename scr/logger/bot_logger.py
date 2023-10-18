import logging

logging.basicConfig(
    level=logging.INFO,
    filename='logger/program.log',
    format='%(asctime)s - %(filename)s - %(funcName)s - %(lineno)s - %(levelname)s - %(message)s'
)
