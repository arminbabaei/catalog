from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Catalog, CatalogItem

app = Flask(__name__)

engine = create_engine('sqlite:///catalogitems.db', connect_args={'check_same_thread': False})
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/catalog/')
def showCategories():
    return 'show All Categories'

@app.route('/catalog/new')
def newCategory():
    return 'new Category'

@app.route('/catalog/<int:catalog_id>/edit')
def editCategory():
    return 'edit Category'

@app.route('/catalog/<int:catalog_id>/delete')
def deleteCategory():
    return 'delete Category'

@app.route('/catalog/<int:catalog_id>/items')
def showCategoryItems():
    return 'show a selected Category Items'

@app.route('/catalog/<int:catalog_id>/items/new')
def newCategoryItem():
    return 'add a New Item in a selceted Category Item'

@app.route('/catalog/<int:catalog_id>/items/<int:item_id>/edit')
def editCategoryItem():
    return 'edit an Item from a selceted Category Item'

@app.route('/catalog/<int:catalog_id>/items/<int:item_id>/delete')
def celeteCategoryItem():
    return 'delete an Item from a selceted Category Item'

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port=8000)