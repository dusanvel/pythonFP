from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
 
engine = create_engine('sqlite:///output.db', echo=True)
Base = declarative_base()

########################################################################
class Output(Base):
    """"""
    __tablename__ = "output"
 
    id = Column(Integer, primary_key=True)
    text = Column(String)
 
    #----------------------------------------------------------------------
    def __init__(self, text):
        """"""
        self.text = text
 
# create tables
Base.metadata.create_all(engine)
