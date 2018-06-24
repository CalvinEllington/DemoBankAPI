import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
import sqlalchemy_utils

#Drop DB if it exists.
if sqlalchemy_utils.database_exists('postgresql:///bankapi.db'):
    sqlalchemy_utils.drop_database('postgresql:///bankapi.db')
sqlalchemy_utils.create_database('postgresql:///bankapi.db')

Base = declarative_base()

#DB Models.
class UserWallet(Base):
    __tablename__ = 'wallet'

    uid = Column(Integer, primary_key=True, autoincrement=True)
    funds = Column(Integer, nullable=True)

    @property
    def serialize(self):
        return {
            'uid' : uid,
            'funds' : funds,
        }

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
