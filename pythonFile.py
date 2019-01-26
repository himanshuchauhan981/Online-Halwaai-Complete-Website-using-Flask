from flask import Flask,request,redirect,url_for,render_template,flash
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager,UserMixin,login_user,current_user,logout_user

app=Flask(__name__);

app.config['SECRET_KEY']='random string';
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///online_halwaai_data.db';
login_manager = LoginManager(app);
db=SQLAlchemy(app);


@login_manager.user_loader
def load_user(user_id):
    return sign_up_data.query.get(int(user_id));

class user_food(db.Model,UserMixin):
    food = db.Column(db.String(20),primary_key=True,nullable=False);
    price = db.Column(db.Integer,nullable=False);
    quantity = db.Column(db.Integer, nullable=False);
    total_price = db.Column(db.Integer,nullable=False);

class food_data(db.Model,UserMixin):
    foodName = db.Column(db.String(20),primary_key=True,nullable=False);
    foodValue = db.Column(db.Integer,default=100,nullable=False);


class sign_up_data(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True);
    firstName = db.Column(db.String(20),nullable=False);
    lastName = db.Column(db.String(20),nullable=False);
    imageFile = db.Column(db.String(20),nullable=False,default='default.jpg');
    mobileNumber = db.Column(db.String(10),unique=True,nullable=False);
    emailAddress = db.Column(db.String(20),unique=True, nullable=False);
    emailPassword = db.Column(db.String(60),nullable=False);

    def __repr__(self):
        return f"User('{self.firstName}','{self.lastName}','{self.mobileNumber}','{self.emailAddress}','{self.emailPassword}')";


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    print("Sign up");
    if request.method == "POST":
        firstname = request.form['first_name']
        lastname = request.form['last_name']
        phone = request.form['phoneno']
        emailid = request.form['email_id']
        password = request.form['pwd']
        return redirect(url_for('sign_up_data_check', first_1=firstname, last_1=lastname, mobile_1=phone, id_1=emailid,passw_1=password))
    else:
        firstname = request.args.get('first_name')
        lastname = request.args.get('last_name')
        phone = request.args.get('phoneno')
        emailid = request.args.get('email_id')
        password = request.args.get('pwd')
        return redirect(url_for('sign_up_data_check', first_1=firstname, last_1=lastname, mobile_1=phone, id_1=emailid,passw_1=password))


@app.route('/sign_up_data_check/<first_1>/<last_1>/<mobile_1>/<id_1>/<passw_1>')
def sign_up_data_check(first_1, last_1, mobile_1, id_1, passw_1):
    emailList = sign_up_data.query.filter_by(emailAddress=id_1).all();
    mobileList = sign_up_data.query.filter_by(mobileNumber=mobile_1).all();
    if emailList is None:
        if mobileList is None:
            return redirect(url_for('signup_data_add',first=first_1,last=last_1,mobile=mobile_1,id=id_1,passw=passw_1));
        else:
            flash('Mobile number already existed');
            return redirect(url_for('signup_online_halwaai'));
    else:
        flash('Email Address already existed');
        return redirect(url_for('signup_online_halwaai'));


@app.route('/signup_data_add/<first>/<last>/<mobile>/<id>/<passw>')
def signup_data_add(first, last, mobile, id, passw):
    bcrypt = Bcrypt(app);
    hashed_password=bcrypt.generate_password_hash(passw).decode('utf-8');
    newUser = sign_up_data(firstName=first,lastName=last,mobileNumber=mobile,emailAddress=id,emailPassword=hashed_password);
    db.session.add(newUser);
    db.session.commit();
    return 'data is added successfully';


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print("Post Method");
        email_id = request.form['emailID']
        email_pass = request.form['pwd']
        return redirect(url_for('login_data_check', id=email_id, epass=email_pass));
    else:
        print("Get Method");
        email_id = request.args.get('emailID')
        email_pass = request.args.get('pwd')
        return redirect(url_for('login_data_check', id=email_id, epass=email_pass));


@app.route('/login_data_check/<id>/<epass>')
def login_data_check(id, epass):
    bcrypt = Bcrypt(app);
    emailList = sign_up_data.query.filter_by(emailAddress=id).first();
    if emailList is not None and bcrypt.check_password_hash(emailList.emailPassword,epass):
        login_user(emailList);
        return redirect(url_for('home_online_halwaai'));
    else:
        flash('Username or Password is incorrect');
        return redirect(url_for('login_online_halwaai'));


@app.route('/foodData',methods=['GET','POST'])
def foodData():
    if current_user.is_active:
        if request.method=='POST':
            food_item = request.form['foods'];
        else:
            food_item = request.args.get('foods');
        return redirect(url_for('food_data_add',item=food_item));
    else:
        return redirect(url_for('login_online_halwaai'));

@app.route('/food_data_add/<item>')
def food_data_add(item):
    ifData = user_food.query.filter_by(food=item).first();
    if ifData:
        ifData.quantity = ifData.quantity + 1;
        ifData.total_price = ifData.price*ifData.quantity;
        db.session.commit();
    else:
        itemList = food_data.query.filter_by(foodName=item).first();
        itemData = user_food(food=item,price=itemList.foodValue,quantity=1,total_price=100);
        db.session.add(itemData);
        db.session.commit();
    return '0',204;


@app.route('/checkout_online_halwaai')
def checkout_online_halwaai():
    if current_user.is_active:
        foodList = [];
        foodPrice = [];
        foodQuantity = [];
        foodTotalPrice =[];
        for user in db.session.query(user_food).distinct():
            foodList.append(user.food);
            foodPrice.append(user.price);
            foodQuantity.append(user.quantity);
            foodTotalPrice.append(user.total_price);
        length=len(foodList);
        payment=sum(foodTotalPrice);
        return render_template('checkoutPage.html', heading='Checkout - online Halwaai',
        foodList=foodList,foodPrice=foodPrice,foodQuantity=foodQuantity,
        foodTotalPrice=foodTotalPrice,length=length,sum=sum,payment=payment);
    else:
        return redirect(url_for('login_online_halwaai'));

@app.route('/remove_items_online_halwaai',methods=['GET','POST'])
def remove_items_online_halwaai():
    if request.method=='POST':
        data = request.form['information'];
    else:
        data = request.args.get('information');
    user_food.query.filter_by(food=data).delete();
    db.session.commit();
    return redirect(url_for('checkout_online_halwaai'));

@app.route('/deleteAll_online_halwaai',methods=['GET','POST'])
def deleteAll_online_halwaai():
    db.session.query(user_food).delete();
    db.session.commit();
    return '0',204;

@app.route('/order_online_halwaai')
def order_online_halwaai():
    return render_template('order.html', heading='Order - online Halwaai')


@app.route('/signup_online_halwaai')
def signup_online_halwaai():
    if current_user.is_authenticated:
        return redirect(url_for('home_online_halwaai'));
    return render_template('signUpPage.html', heading='Sign Up - online Halwaai')



@app.route('/login_online_halwaai')
def login_online_halwaai():
    if current_user.is_authenticated:
        return redirect(url_for('home_online_halwaai'));
    return render_template('loginPage.html', heading='Login - online Halwaai')


@app.route('/logout_online_halwaai')
def logout_online_halwaai():
    logout_user();
    return redirect(url_for('home_online_halwaai'));


@app.route('/account_online_halwaai')
def account_online_halwaai():
    return render_template('account.html',heading='Account - online Halwaai');
    

@app.route('/home_online_halwaai')
@app.route('/')
def home_online_halwaai():
    return render_template('main.html', heading='online Halwaai - Taste the Myth')


if __name__=='__main__':
    app.run(debug=True);
