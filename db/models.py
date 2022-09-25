from sqlalchemy import Column, Integer, VARCHAR, CHAR, DATETIME
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
#from sqlalchemy_utils import relationships
from database import BASE

class Realms(BASE):
    __tablename__ = "realms"
    
    id = Column(Integer, autoincrement = True, primary_key = True)
    realm_id = Column(Integer)
    realm_name = Column(VARCHAR(255))
    region = Column(CHAR(2))
    locale = Column(CHAR(18))
    namespace = Column(CHAR(5))
    items = relationship("Items", backref="realms")
    auctionhouse = relationship("AuctionHouse", backref="realms")

class AuctionHouse(BASE):
    __tablename__ = "auctionhouse"
    
    id = Column(Integer, autoincrement = True, primary_key = True)
    realm_id = Column(Integer, ForeignKey("realms.id"))
    auction_house_id = Column(Integer)
    faction = Column(VARCHAR(255))
    prices = relationship("Prices", backref="auctionhouse")

class Items(BASE):
    __tablename__ = "items"
    
    id = Column(Integer, autoincrement = True, primary_key = True)
    item_id = Column(Integer)
    realm_id = Column(Integer, ForeignKey("realms.id"))
    item_name = Column(VARCHAR(255))
    prices = relationship("Prices", backref="items")

class Prices(BASE):
    __tablename__ = "prices"
    
    id = Column(Integer, autoincrement = True, primary_key = True)
    item_id = Column(Integer, ForeignKey("items.id"))
    price = Column(Integer)
    date_time = Column(DATETIME)
    auction_house_id = Column(Integer, ForeignKey("auctionhouse.id"))
