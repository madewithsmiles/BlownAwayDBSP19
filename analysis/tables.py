from sqlalchemy import Column, INTEGER, CHAR, FLOAT, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# -------------------------------- State #
class State(Base):
    __tablename__ = 'state'

    StateID = Column(INTEGER, primary_key=True, nullable=False)
    StateName = Column(CHAR(50), nullable=False)

# -------------------------------- Tornado Info #
class Tornado(Base):
    __tablename__ = 'tornado'

    TornadoID = Column(INTEGER, primary_key=True, nullable=False)
    Yr = Column(INTEGER, nullable=False)
    Mo = Column(INTEGER, nullable=False)
    Dy = Column(INTEGER, nullable=False)
    Magnitude = Column(INTEGER, nullable=False)
    Latitude = Column(FLOAT, nullable=False)
    Longitude = Column(FLOAT, nullable=False)
    StateID = Column(INTEGER, ForeignKey("state.StateID"), nullable=False)


# -------------------------------- Industry #
class Industry(Base):
    __tablename__ = 'industry'

    IndustryID = Column(INTEGER, primary_key=True, nullable=False)
    IndustryName = Column(CHAR(50), nullable=False)

# -------------------------------- GDP #
class Gdp(Base):
    __tablename__ = 'gdp'

    GdpID = Column(INTEGER, primary_key=True,nullable=False)
    GDP = Column(FLOAT, nullable=False)
    Yr = Column(INTEGER, nullable=False)
    StateID = Column(INTEGER, ForeignKey("state.StateID"), nullable=False)
    IndustryID = Column(INTEGER, ForeignKey("industry.IndustryID") ,nullable=False)
    