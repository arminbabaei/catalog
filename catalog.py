from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Catalog, CatalogItem

app = Flask(__name__)

engine = create_engine('sqlite:///catalogitems.db',
                       connect_args={'check_same_thread': False})
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
@app.route('/catalog/')
def showCategories():
    catalogs = session.query(Catalog)
    return render_template(
        'categories.html', catalogs=catalogs)


@app.route('/catalog/new', methods=['GET', 'POST'])
def newCategory():
    if request.method == 'POST':
        newCategory = Catalog(name=request.form['name'])
        session.add(newCategory)
        session.commit()
        return redirect(url_for('showCategories'))
    else:
        return render_template('newCategory.html')


@app.route('/catalog/<int:catalog_id>/edit', methods=['GET', 'POST'])
def editCategory(catalog_id):
    editedCatalog = session.query(Catalog).filter_by(id=catalog_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedCatalog.name = request.form['name']
            return redirect(url_for('showCategories'))
    else:
        return render_template('editCategory.html', catalog=editedCatalog)


@app.route('/catalog/<int:catalog_id>/delete', methods=['GET', 'POST'])
def deleteCategory(catalog_id):
    catalogToDelete = session.query(Catalog).filter_by(id=catalog_id).one()
    if request.method == 'POST':
        session.delete(catalogToDelete)
        session.commit()
        return redirect(url_for('showCategories', catalog_id=catalog_id))
    else:
        return render_template('deleteCategory.html', catalog=catalogToDelete)


@app.route('/catalog/<int:catalog_id>/items')
def showCategoryItems(catalog_id):
    catalog = session.query(Catalog).filter_by(id=catalog_id).one()
    items = session.query(CatalogItem).filter_by(catalog_id=catalog_id).all()
    return render_template('items.html', catalog=catalog, items=items, catalog_id=catalog_id)


@app.route('/catalog/<int:catalog_id>/items/new', methods=['GET', 'POST'])
def newCategoryItem(catalog_id):
    if request.method == 'POST':
        newItem = CatalogItem(name=request.form['name'], description=request.form['description'],
                              price=request.form['price'], size=request.form['size'], color=request.form['color'], catalog_id=catalog_id)
        session.add(newItem)
        session.commit()
        return redirect(url_for('showCategoryItems', catalog_id=catalog_id))
    else:
        return render_template('newCategoryItem.html', catalog_id=catalog_id)


@app.route('/catalog/<int:catalog_id>/items/<int:item_id>/edit', methods=['GET', 'POST'])
def editCategoryItem(catalog_id, item_id):
    editedCategoryItem = session.query(CatalogItem).filter_by(id=item_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedCategoryItem.name = request.form['name']
        session.add(editedCategoryItem)
        session.commit()
        return redirect(url_for('showCategoryItems', catalog_id=catalog_id, item_id=item_id))
    else:
        return render_template('editCategoryItem.html', catalog_id=catalog_id, item_id=item_id, item=editedCategoryItem)


@app.route('/catalog/<int:catalog_id>/items/<int:item_id>/delete', methods=['GET', 'POST'])
def deleteCategoryItem(catalog_id, item_id):
    itemToDelete = session.query(CatalogItem).filter_by(id=item_id).one()
    if request.method == 'POST':
        session.delete(itemToDelete)
        session.commit()
        return redirect(url_for('showCategoryItems', catalog_id=catalog_id, item_id=item_id))
    else:
        return render_template('deleteCategoryItem.html', catalog_id=catalog_id, item_id=item_id, item=itemToDelete)


if __name__ == '__main__':
    app.debug = True
    app.run(host= '0.0.0.0', port=8000)
