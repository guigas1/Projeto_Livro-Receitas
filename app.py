from flask import Flask, render_template, redirect, url_for, flash, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_bcrypt import Bcrypt
from models import db, User, Recipe

app = Flask(__name__)
app.config['SECRET_KEY'] = '981838467gui'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipes.db'

db.init_app(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'erro'

with app.app_context():
    db.create_all()

@app.route('/')
@login_required
def index():
    recipes = current_user.recipes
    return render_template('index.html', recipes=recipes)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        existing_user = User.query.filter_by(username=username).first()

        if existing_user:
            flash(f'Esse nome de usuário já existe, por favor escolha outro.', 'erro')
            return redirect(url_for('login'))

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User(username=username, password_hash=hashed_password)

        db.session.add(new_user)
        db.session.commit()
        
        flash(f'Conta criada com sucesso! Pode realizar o Login.', 'sucesso')

        return redirect(url_for('register'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    
    if request.method == 'POST':
        username_digitado = request.form.get('username')
        password_digitada = request.form.get('password')
        user = User.query.filter_by(username=username_digitado).first()

        if user and bcrypt.check_password_hash(user.password_hash, password_digitada):
            login_user(user)
            flash(f'Login feito com sucesso', 'sucesso')
            return redirect(url_for('index'))   
        
        else:
            flash(f'Usuário não encontrado. Tente novamente ou faça o Registro.','erro')
            return redirect(url_for('login'))
        
    return render_template('login.html')

@app.route('/logout')
def logout():
    logout_user()
    flash(f'Você saiu da sua conta', 'sucesso')
    return redirect(url_for('login'))

@app.route('/nova_receita', methods=['GET','POST'])
@login_required 
def nova_receita():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        new_recipe = Recipe(title=title, content=content, author=current_user)

        db.session.add(new_recipe)
        db.session.commit()

        flash(f'Receita adicionada com Sucesso!', 'sucesso')
        return redirect(url_for('index'))
    
    return render_template('nova_receita.html')

@app.route('/deletar_receita/<int:recipe_id>')
@login_required
def deletar_receita(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)

    if recipe.author != current_user:
        abort(403)

    db.session.delete(recipe)
    db.session.commit()

    flash(f'Receita deletada com sucesso!', 'sucesso')
    return redirect(url_for('index'))

@app.route('/editar_receita/<int:recipe_id>', methods=['GET','POST'])
def editar_receita(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)

    if recipe.author != current_user:
        abort(403)
    
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        recipe.title = title
        recipe.content = content
        db.session.commit()
        flash(f'Receita atualizada com sucesso!', 'sucesso')
        return redirect(url_for('index'))
    return render_template('editar_receita.html', recipe=recipe)

@app.route('/receita/<int:recipe_id>')
@login_required
def ver_receita(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    if recipe.author != current_user:
        abort(403)

    return render_template('receita_detalhe.html', recipe=recipe)


if __name__ == "__main__":
    app.run(debug=True) 

