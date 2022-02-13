import numpy as np
import pandas as pd
import eland as ed
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from elasticsearch import Elasticsearch
from eland.conftest import *

es = Elasticsearch(['https://metrics:korsar@192.168.250.2:9200'],  verify_certs=False)

#x = ed.DataFrame(es, 'fritzbox', columns=['Datum', 'Dauer', 'Rufnummer']).query('Rufnummer == "0223377973"').to_csv(path_or_buf="export2.csv" )
ed.DataFrame(es, 'fritzbox', columns=['Datum', 'Dauer', 'Rufnummer']).query('Rufnummer == "0223377973"')