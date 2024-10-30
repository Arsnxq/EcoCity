from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"Article('{self.title}', '{self.content}')"

with app.app_context():
    db.create_all()

@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")

@app.route('/create_article', methods=['GET', 'POST'])
def create_article():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        
        article = Article(title=title, content=content)
        db.session.add(article)
        db.session.commit()
        
        return redirect(url_for('articles'))
    return render_template("states.html")

@app.route('/articles')
def articles():
    all_articles = Article.query.all()  
    return render_template("stateList.html", articles=all_articles)

@app.route('/delete_article/<int:article_id>', methods=['POST'])
def delete_article(article_id):
    article = Article.query.get_or_404(article_id)
    db.session.delete(article) 
    db.session.commit()  
    return redirect(url_for('articles'))   

if __name__ == "__main__":
    app.run(debug=True)
