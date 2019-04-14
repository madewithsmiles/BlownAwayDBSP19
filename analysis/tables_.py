from sqlalchemy import Column, INTEGER, CHAR, FLOAT, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# -------------------------------- State #
class State(Base):
    __tablename__ = 'state'

    StateID = Column(INTEGER, primary_key=True)
    StateName = Column(CHAR(50))

# -------------------------------- Tornado Info #
class Tornado(Base):
    __tablename__ = 'tornado'

    TornadoID = Column(INTEGER, primary_key=True)
    Yr = Column(INTEGER)
    Mo = Column(INTEGER)
    Dy = Column(INTEGER)
    Magnitude = Column(INTEGER)
    Latitude = Column(FLOAT)
    Longitude = Column(FLOAT)
    StateID = Column(INTEGER)


# -------------------------------- Industry #
class Industry(Base):
    __tablename__ = 'industry'

    IndustryID = Column(INTEGER, primary_key=True)
    IndustryName = Column(CHAR(50))

# -------------------------------- GDP #
class Gdp(Base):
    __tablename__ = 'gdp'

    GdpID = Column(INTEGER, primary_key=True,nullable=False)
    GDP = Column(FLOAT)
    Yr = Column(INTEGER)
    StateID = Column(INTEGER)
    IndustryID = Column(INTEGER)
    