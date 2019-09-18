#!/usr/bin/python
# -*- coding: utf-8 -*-
from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, Category, CategoryItem, User

engine = \
    create_engine('postgresql://catalog:catalog@localhost:5432/catalog')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

user1 = User(id=1, name='Armin', email='armin.babaei@icloud.com',
             creation_date=datetime.now())

session.add(user1)
session.commit()

category1 = Category(name='TOP')

session.add(category1)
session.commit()

categoryItem1 = CategoryItem(
    name="ARMIN's Shirt",
    description="ARMIN's Embroidered logo",
    price='$400.00',
    color='Custom',
    size='Custom',
    user_id=1,
    creation_date=datetime.now(),
    category=category1,
    )

session.add(categoryItem1)
session.commit()

category2 = Category(name='BOTTOM')

session.add(category2)
session.commit()

categoryItem1 = CategoryItem(
    name="ARMIN's Pants",
    description="ARMIN's Embroidered logo",
    price='$900.00',
    color='Custom',
    size='Custom',
    user_id=1,
    creation_date=datetime.now(),
    category=category2,
    )

session.add(categoryItem1)
session.commit()

print 'added category items!'
