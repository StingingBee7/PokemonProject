from sqlalchemy import create_engine
import pandas as pd
from config import *

engine = create_engine('mysql+pymysql://' + USERNAME + ':' + PASSWORD + '@' + ENDPOINT + ':' + str(PORT) + '/' + DBNAME)

df = pd.read_csv('top10s.csv')

df.to_sql('top10', con=engine)
