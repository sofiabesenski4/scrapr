from faktory import Worker
import faktory
import logging
from jobs.scrape_job import scrape 

logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    w = Worker(queues=['default'], concurrency=3)
    w.register('scrape_job', scrape)
    w.run()  # runs until control-c or worker shutdown from Faktory web UI

