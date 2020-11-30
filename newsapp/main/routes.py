from flask import Blueprint, render_template, redirect, url_for, request, flash
from newsapp.extensions import mongo
from bson.objectid import ObjectId
# Foi criado um blueprintMain como se fosse um controller isso facilita quando temos muitas regras de negocios em um projeto com grandes players
main = Blueprint('main', __name__)

# Rota que retorna todas as noticias em index.html
@main.route('/')
def index():
  news_collection = mongo.db.news
  news = news_collection.find()
  return render_template('index.html', news=news)

# Rota que captura via form post valores dos inputs e faz um insert no DB
@main.route('/add_new', methods=["POST"])
def add_new():

  news_collection = mongo.db.news
  titulo = request.form.get('titulo')
  texto = request.form.get('texto')
  autor = request.form.get('autor')
  new = {
    "titulo": titulo,
    "texto": texto,
    "autor": autor,
    "deleted": False 
  }

  flash("A notícia foi adicionada")
  news_collection.insert_one(new)
  return redirect(url_for('main.index'))

# Rota que deleta uma noticia especifica capturando o ID da row e fazendo um de/para com o DB
@main.route('/delete_new/<oid>')
def delete_new(oid):
  news = mongo.db.news
  news.remove({"_id": ObjectId(oid)});
  return redirect(url_for('main.index'))

# Rota que procura por um unico elemento pelo parametro TITULO no db
@main.route('/search_new', methods=["POST", "GET"])
def search_new():
  
  news_collection = mongo.db.news
  search_titulo = request.form.get('search_titulo')
  one_new = news_collection.find_one({'titulo': search_titulo})
  print(search_titulo)
  if(one_new):
    # Como o retorno e um dic, tive que encapsular em um array para iterar com o  JINJA
    array = [one_new]
    return render_template('index.html', news=array)
  
  flash("Nenhum usuario encontrado")
  return redirect(url_for('main.index'))

# Faz o update e traz nos inputs os valores da noticia selecionada
@main.route('/update_new/<id>', methods=["POST", "GET"])
def update_new(id):
  news = mongo.db.news
  item_id_to_update = {"_id": ObjectId(id)}
  titulo = request.form.get('titulo')
  texto = request.form.get('texto')
  autor = request.form.get('autor')
  new_values = {
    "titulo": titulo,
    "texto": texto,
    "autor": autor,
    "deleted": False 
  }

  news.update(item_id_to_update, new_values)
  return redirect(url_for('main.index'))
  
 
