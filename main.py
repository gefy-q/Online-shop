from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# 'sqlite:///D:/проги/PyCharm Community Edition 2020.1.1/web/shop.db'
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# manager = Manager(app)
db = SQLAlchemy(app)


class Items(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    isActive = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return self.title


# engine = create_engine('sqlite:///shop.db, convert_unicode=True')
# session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
# db.query = session.query_property()


@app.route('/')
def index():
    # items = Items.query.order_by(Items.price).all()
    return render_template('index.html') # , data=items


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/create', methods=['POST', 'GET'])
def create():
    # if request.method == 'POST':
    #     title = request.form['title']
    #     price = request.form['price']
    #
    #     item = Items(title=title, price=price)
    #     try:
    #         db.session.add(item)
    #         db.session.commit()
    #         return redirect('/')
    #     except:
    #         return 'Error'
    # else:
    return render_template('create.html')


if __name__ == '__main__':
    app.run(debug=True)
