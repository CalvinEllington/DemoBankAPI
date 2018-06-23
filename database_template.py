import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

#DB Models.
class Account(Base):
    __tablename__ = 'accounts'

    aid = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    hodlings = Column(Integer, nullable=True)

    @property
    def serialize(self):
        return {
            'aid' : self.aid,
            'name' : self.name,
            'hodlings' : self.hodlings,
        }

class Transaction(Base):
    __tablename__ = 'transactions'

    txid = Column(Integer, primary_key=True, autoincrement=True)
    aid = Column(Integer, ForeignKey('accounts.aid'))
    amount = Column(Integer, nullable=False)
    account = relationship(Account)

    @property
    def serialize(self):
        return {
            'txid' : self.txid,
            'aid' : self.aid,
            'amount' : self.amount,
        }

#DB Engine.
engine = create_engine('postgresql:///bankapi.db')
Base.metadata.create_all(engine)
