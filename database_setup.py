import sys

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Catalog(Base):
    __tablename__ = 'catalog'

    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)

class CatalogItem(Base):
    __tablename__ = 'catalog_item'

    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    color = Column(String(250))
    size = Column(String(250)) 
    price = Column(String(8))
    description = Column(String(250))
    catalog_id = Column(Integer, ForeignKey('catalog.id'))
    catalog = relationship(Catalog)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'color': self.color,
            'size': self.size,
            'price': self.price,
            'description': self.description
        }



engine = create_engine('sqlite:///catalogitems.db')
Base.metadata.create_all(engine)
