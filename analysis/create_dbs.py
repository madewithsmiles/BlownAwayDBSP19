import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from tables import Base, State, Tornado, Industry, Gdp
from data_processing import get_dataset

dataset = get_dataset()
metadata = db.MetaData()
engine = db.create_engine('sqlite:///test.db', echo=True)
connection = engine.connect()
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()
sts = [State(**i) for i in dataset.states.to_dict(orient="records")]
session.add_all(sts)

tds = [Tornado(**i) for i in dataset.tornados.to_dict(orient="records")]
session.add_all(tds)

inds = [Industry(**i) for i in dataset.industries.to_dict(orient="records")]
session.add_all(inds)

gdps = [Gdp(**i) for i in dataset.gdp.to_dict(orient="records")]
session.add_all(gdps)

session.commit()
session.close()

connection.close()
engine.dispose()

""" Before
session.bulk_insert_mappings(State,dataset.states.to_dict(orient="records"))
session.bulk_insert_mappings(Tornado, dataset.tornados.to_dict(orient="records"))
session.bulk_insert_mappings(Industry, dataset.industries.to_dict(orient="records"))
session.bulk_insert_mappings(Gdp, dataset.gdp.to_dict(orient="records"))
"""