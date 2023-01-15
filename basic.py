from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
import bcrypt
import jwt
from datetime import datetime, timedelta

app = Flask(__name__)
app.config['SECRET_KEY'] = "secretkeythatisverysecret"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"


db = SQLAlchemy()
db.init_app(app)

#Model For User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String,unique=True, nullable=False)
    password = db.Column(db.String)
with app.app_context():
    db.create_all()


#Route For Sign-Up
@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json() #get the data from user
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    #check email and password
    if not name or not email or not password:
        return make_response('Please enter all fields', 401)


    salt = bcrypt.gensalt()
    bytePwd = password.encode('utf-8')
    #Generating Hashed Password Before Saving Into DataBase
    hashed_password = bcrypt.hashpw(bytePwd, salt)


    user = User(
            username=name,
            email=email,
            password=hashed_password
        )


    db.session.add(user)
    db.session.commit()

    #Create token
    token = jwt.encode({'user': name, 'exp': datetime.utcnow() + timedelta(minutes=30)}, app.config['SECRET_KEY'])

    return jsonify({'token': token})


#Route For Login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json() #get the data from user
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    password = password.encode('utf-8')


    #check name and password
    if not name or not password:
        return make_response('Please enter all fields', 401)

    #Check Database For User
    user = db.one_or_404(db.select(User).filter_by(email=email))

    #Check Database For Password
    if not (bcrypt.checkpw(password, user.password)):
        return make_response("Wrong Password", 402)
   
    
    #Create token
    token = jwt.encode({'user': name, 'exp': datetime.utcnow() + timedelta(minutes=30)}, app.config['SECRET_KEY'])

    return jsonify({'token': token})



#Route For Validiting Token
@app.route('/protected', methods=['GET'])
def protected():
    token = request.headers.get('Token')
    #Looking For Token
    if not token:
        return make_response('Token is missing', 401)

    #Validiting Token
    try:
        data = jwt.decode(token, app.config['SECRET_KEY'], algorithms="HS256")
        print(data)
    except :
        return make_response('Token is invalid', 401)

    return 'Welcome ' + data['user']



if __name__ == '__main__':
    app.run(debug=True)