from flask import Blueprint,render_template,request, jsonify, redirect, url_for, session
from exts import mail,db
from models import UserModel
from .forms import RegisterForm, LoginForm,ForgetForm
from flask_mail import Message

bp = Blueprint("users",__name__,url_prefix="/users")

# 登录
@bp.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template("登录注册界面/登录.html")
    else:
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            user = UserModel.query.filter_by(email=email).first()
            if not user:
                print("邮箱在数据库中不存在！")
                return redirect(url_for("users.login"))
            if user.password == password:
                session['user_id'] = user.id
                return redirect("/")
            else:
                print(form.errors)
                return redirect(url_for("users.login"))

# 退出登录
@bp.route("/logout")
def logout():
    session.clear()
    return redirect("/")

# 注册
@bp.route("/register",methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template("登录注册界面/注册.html")
    else:
        form = RegisterForm(request.form)
        if form.validate():
            email = form.email.data
            phone = form.phone.data
            username = form.username.data
            password = form.password.data
            user = UserModel(email=email, username=username, password=password,phone=phone)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("users.login"))
        else:
            print(form.errors)
            return redirect(url_for("users.register"))

# 忘记密码
@bp.route("/forget",methods=['GET','POST'])
def forget():
    if request.method == 'GET':
        return render_template("登录注册界面/忘记密码.html")
    else:
        form = ForgetForm(request.form)
        if form.validate():
            email = form.email.data
            phone = form.phone.data
            username = form.username.data
            password = form.password.data
            user = UserModel.query.filter_by(email=email).first()
            if not user:
                print("邮箱在数据库中不存在！")
                return redirect(url_for("users.forget"))

            if user.username == username and user.phone == phone and user.email == email:
                user.password = password
                db.session.commit()
                return redirect(url_for("users.login"))
            else:
                print(form.errors)
                return redirect(url_for("users.forget"))

# 邮件发送测试（已经取消此功能）
# @bp.route("/mail/test")
# def mail_test():
#     message = Message(subject="测试邮箱", recipients=["2906523984@qq.com"], body="test")
#     mail.send(message)
#     return "邮件发送成功！"
    # message = Message('测试邮件', recipients=['2906523984@qq.com'])
    # message.html = '<h1>Hello World!</h1><p>This is a test email sent from Flask.</p>'
    # mail.send(message)
    # return '邮件发送成功！'