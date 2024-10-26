from flask import Flask, render_template, request
from models import *

app = Flask(__name__, template_folder='../static')

@app.route('/')
def home_page():
    return render_template('home_page.html')


@app.route('/registration_page')
def open_registration_page():
    return render_template('registration.html')


@app.route('/register')
def register_new_user():
    u_name = request.args.get('u_name')
    new_user = User(user_name=u_name)

    Session = sessionmaker(bind=engine)
    session = Session()

    session.add(new_user)
    session.commit()

    session.close()

    return {'status': 200, 'data': 'Successful!!'}


@app.route('/user/<user_id>')
def get_user(user_id: int):
    Session = sessionmaker(bind=engine)
    session = Session()

    data = session.execute(select(User).where(User.id == user_id)).first()[0]

    return render_template('profile.html',
                           user_name=data.user_name,
                           health = data.health,
                           manna = data.manna,
                           points = data.points,
                           level = data.level)


if __name__ == '__main__':
    app.run(debug=True)
