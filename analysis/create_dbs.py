import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from tables_ import Base, State, Tornado, Industry, Gdp
from data_processing import get_dataset

dataset = get_dataset()
metadata = db.MetaData()
engine = db.create_engine('sqlite:///test.db', echo=True)
connection = engine.connect()
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()
session.bulk_insert_mappings(State,dataset.states)
session.bulk_insert_mappings(Tornado, dataset.tornados)
session.bulk_insert_mappings(Industry, dataset.industries)
session.bulk_insert_mappings(Gdp, dataset.gdp)
session.commit()
session.close()

connection.close()
engine.dispose()