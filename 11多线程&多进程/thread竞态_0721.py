import logging
import time
import concurrent.futures

class FakeDtabase:

    def __init__(self):
        self.value = 0

    def updage(self, name):
        logging.info("Thread %s:starting update", name)
        local_copy = self.value
        local_copy += 1
        time.sleep(0.1)
        self.value = local_copy
        logging.info("Thread %s: finishing update", name)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    database = FakeDtabase()
    logging.info("Testing update.Starting bvalue is %d.", database.value)
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(2):
            executor.submit(database.updage, index)
    logging.info("Testing update. Ending value is %d.", database.value)