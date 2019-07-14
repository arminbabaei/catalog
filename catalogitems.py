from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Catalog, Base, CatalogItem

engine = create_engine('sqlite:///catalogitems.db')
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
catalog1 = Catalog(name="T-SHIRTS")

session.add(catalog1)
session.commit()

catalogItem1 = CatalogItem(name="HOME T-SHIRT", description="Official collaboration with Bob Dylan",
                     price="$40.00", color="Black", size="Large", catalog=catalog1)

session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(name="DARTS T-SHIRT", description="Official collaboration with Bob Dylan",
                     price="$40.00", color="White", size="Large", catalog=catalog1)

session.add(catalogItem2)
session.commit()


# Items For SWEATSHIRTS
catalog2 = Catalog(name="SWEATSHIRTS")

session.add(catalog2)
session.commit()


catalogItem1 = CatalogItem(name="RIDE HOODY", description="Official collaboration with Bob Dylan",
                     price="$90.00", color="Black", size="Large", catalog=catalog2)

session.add(catalogItem1)
session.commit()


# Items for HEADWEAR
catalog3 = Catalog(name="HEADWEAR")

session.add(catalog1)
session.commit()


catalogItem1 = CatalogItem(name="FOREVER HAT", description="Official collaboration with Bob Dylan, low profile trucker snapback with patch",
                     price="$36.00", color="Black", size="Large", catalog=catalog3)

session.add(catalogItem1)
session.commit()


# Items for FOOTWEAR
catalog4 = Catalog(name="FOOTWEAR")

session.add(catalog1)
session.commit()


catalogItem1 = CatalogItem(name="TYPHOON PANTS", description="All over custom printed denim pant",
                     price="$100.00", color="Black", size="Medium", catalog=catalog4)

session.add(catalogItem1)
session.commit()


print "added catalog items!"