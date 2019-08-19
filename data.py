from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, User, Category, CategoryItem

engine = create_engine('postgresql://catalog:catalog@localhost:5432/catalog')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Items for T-SHIRTS
category1 = Category(name="T-SHIRTS")

session.add(category1)
session.commit()

categoryItem1 = CategoryItem(name="HOME T-SHIRT", description="Official collaboration with Bob Dylan",
                             price="$40.00", color="Black", size="Large", category=category1)

session.add(categoryItem1)
session.commit()

categoryItem2 = CategoryItem(name="DARTS T-SHIRT", description="Official collaboration with Bob Dylan",
                             price="$40.00", color="White", size="Large", category=category1)

session.add(categoryItem2)
session.commit()


# Items For SWEATSHIRTS
category2 = Category(name="SWEATSHIRTS")

session.add(category2)
session.commit()


categoryItem1 = CategoryItem(name="RIDE HOODY", description="Official collaboration with Bob Dylan",
                             price="$90.00", color="Black", size="Large", category=category2)

session.add(categoryItem1)
session.commit()


# Items for HEADWEAR
category3 = Category(name="HEADWEAR")

session.add(category1)
session.commit()


categoryItem1 = CategoryItem(name="FOREVER HAT", description="Official collaboration with Bob Dylan, low profile trucker snapback with patch",
                             price="$36.00", color="Black", size="Large", category=category3)

session.add(categoryItem1)
session.commit()


# Items for FOOTWEAR
category4 = Category(name="FOOTWEAR")

session.add(category1)
session.commit()


categoryItem1 = CategoryItem(name="TYPHOON PANTS", description="All over custom printed denim pant",
                             price="$100.00", color="Black", size="Medium", category=category4)

session.add(categoryItem1)
session.commit()


print("added category items!")
