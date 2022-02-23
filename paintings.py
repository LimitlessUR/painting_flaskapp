from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.painting import Painting
from flask_app.models.user import User



@app.route('/new/painting')
def new_painting():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":session['user_id']
    }
    return render_template('new.html',user=User.get_by_id(data))


@app.route('/create/painting',methods=['POST'])
def create_painting():
    if 'user_id' not in session:
        return redirect('/logout')
    
    data = {
        "title": request.form["title"],
        "description": request.form["description"],
        "price": request.form["price"],
        "user_id": session["user_id"]
    }
    Painting.save(data)
    return redirect('/dashboard')


@app.route('/painting/<int:id>')
def show_painting(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template('show.html',painting=Painting.get_one(data),user=User.get_by_id(user_data))

@app.route('/edit/painting/<int:id>')
def edit_painting(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("edit.html",painting=Painting.get_one(data),user=User.get_by_id(user_data))

@app.route('/update/painting',methods=['POST'])
def update_painting():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Painting.validate_painting(request.form):
        return redirect('/new/painting')
    data = {
        "title": request.form["title"],
        "description": request.form["description"],
        "price": request.form["price"],
        "id": request.form['id']
    }
    Painting.update(data)
    return redirect('/dashboard')

@app.route('/destroy/painting/<int:id>')
def destroy_painting(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    Painting.destroy(data)
    return redirect('/dashboard')