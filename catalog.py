from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, CategoryItem

app = Flask(__name__)

engine = create_engine('sqlite:///categoryitems.db',
                       connect_args={'check_same_thread': False})
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/catalog/JSON')
def showCategoriesJSON():
    categories = session.query(Category)
    return jsonify(categoryItems=[i.serialize for i in categories]) 

@app.route('/catalog/<int:category_id>/items/JSON')
def showCategoryItemsJSON(category_id):
    categoryItems = session.query(CategoryItem).filter_by(category_id=category_id).all()
    return jsonify(categoryItems=[i.serialize for i in categoryItems])


@app.route('/')
@app.route('/catalog/')
def showCategories():
    categories = session.query(Category)
    return render_template('categories.html', categories=categories)


@app.route('/catalog/new', methods=['GET', 'POST'])
def newCategory():
    if request.method == 'POST':
        newCategory = Category(name=request.form['name'])
        session.add(newCategory)
        session.commit()
        return redirect(url_for('showCategories'))
    else:
        return render_template('newCategory.html')


@app.route('/catalog/<int:category_id>/edit', methods=['GET', 'POST'])
def editCategory(category_id):
    editedCategory = session.query(Category).filter_by(id=category_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedCategory.name = request.form['name']
            return redirect(url_for('showCategories'))
    else:
        return render_template('editCategory.html', category=editedCategory)


@app.route('/catalog/<int:category_id>/delete', methods=['GET', 'POST'])
def deleteCategory(category_id):
    categoryToDelete = session.query(Category).filter_by(id=category_id).one()
    if request.method == 'POST':
        session.delete(categoryToDelete)
        session.commit()
        return redirect(url_for('showCategories', category_id=category_id))
    else:
        return render_template('deleteCategory.html', category=categoryToDelete)


@app.route('/catalog/<int:category_id>/items')
def showCategoryItems(category_id):
    category = session.query(Category).filter_by(id=category_id).one()
    categoryItems = session.query(CategoryItem).filter_by(category_id=category_id).all()
    return render_template('categoryItems.html', category=category, categoryItems=categoryItems, category_id=category_id)


@app.route('/catalog/<int:category_id>/items/new', methods=['GET', 'POST'])
def newCategoryItem(category_id):
    if request.method == 'POST':
        newCategoryItem = CategoryItem(name=request.form['name'], description=request.form['description'],
                              price=request.form['price'], size=request.form['size'], color=request.form['color'], category_id=category_id)
        session.add(newItem)
        session.commit()
        return redirect(url_for('showCategoryItems', category_id=category_id))
    else:
        return render_template('newCategoryItem.html', category_id=category_id)


@app.route('/catalog/<int:category_id>/items/<int:item_id>/edit', methods=['GET', 'POST'])
def editCategoryItem(category_id, item_id):
    editedCategoryItem = session.query(CategoryItem).filter_by(id=item_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedCategoryItem.name = request.form['name']
        session.add(editedCategoryItem)
        session.commit()
        return redirect(url_for('showCategoryItems', category_id=category_id, item_id=item_id))
    else:
        return render_template('editCategoryItem.html', category_id=category_id, item_id=item_id, item=editedCategoryItem)


@app.route('/catalog/<int:category_id>/items/<int:item_id>/delete', methods=['GET', 'POST'])
def deleteCategoryItem(category_id, item_id):
    categoryItemToDelete = session.query(CategoryItem).filter_by(id=item_id).one()
    if request.method == 'POST':
        session.delete(categoryItemToDelete)
        session.commit()
        return redirect(url_for('showCategoryItems', category_id=category_id, item_id=item_id))
    else:
        return render_template('deleteCategoryItem.html', category_id=category_id, item_id=item_id, item=itemToDelete)


if __name__ == '__main__':
    app.debug = True
    app.run(host= '0.0.0.0', port=8000)
