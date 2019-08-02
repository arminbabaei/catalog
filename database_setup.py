import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Category(Base):
    __tablename__ = 'category'

    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }

class CategoryItem(Base):
    __tablename__ = 'category_item'

    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    color = Column(String(250))
    size = Column(String(250)) 
    price = Column(String(8))
    description = Column(String(250))
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category)

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



engine = create_engine('sqlite:///categoryitems.db')
Base.metadata.create_all(engine)
