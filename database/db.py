from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import configparser
import pathlib

config_path = pathlib.Path(__file__).parent.parent.joinpath('config.ini')
config = configparser.ConfigParser()
config.read(config_path)

username = config.get("DB", "USER")
password = config.get("DB", "password")
domain = config.get("DB", "host")
port = config.get("DB", "port")
dbname = config.get("DB", "database")

url = f'postgresql://{username}:{password}@{domain}:{port}/{dbname}'

engine = create_engine(url, echo=False)
DBsession = sessionmaker(bind=engine)
session = DBsession()
