import logging
import os
from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

class ElasticsearchHandler(logging.Handler):
    def __init__(self, es_client, index):
        logging.Handler.__init__(self)
        self.es_client = es_client
        self.index = index

    def emit(self, record):
        log_entry = self.format(record)
        self.es_client.index(index=self.index, body=log_entry)

es = Elasticsearch(['http://localhost:9200'])

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger()
es_handler = ElasticsearchHandler(es, 'logs')
es_handler.setFormatter(logging.Formatter("[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"))
logger.addHandler(es_handler)

# Example usage
logger.info("This is an info message")

