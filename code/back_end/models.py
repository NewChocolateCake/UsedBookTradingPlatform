from exts import db
from datetime import datetime

# 用户信息数据库
class UserModel(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    join_time = db.Column(db.DateTime, default=datetime.now)

# 二手物品发布信息
class ESObjectModel(db.Model):
    __tablename__ = "esobject"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    price = db.Column(db.String(10), nullable=False)
    creat_time = db.Column(db.DateTime,default=datetime.now)
    image = db.Column(db.LargeBinary)
    # 外键
    author_id = db.Column(db.Integer,db.ForeignKey("user.id"))
    # 关系
    author = db.relationship(UserModel,backref="wuping")


# 评论数据库
class AnswerModel(db.Model):
    __tablename__ = "answer"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text, nullable=False)
    creat_time = db.Column(db.DateTime, default=datetime.now)
    # 外键
    wuping_id = db.Column(db.Integer,db.ForeignKey("esobject.id"))
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    # 关系
    wuping = db.relationship(ESObjectModel,backref=db.backref("answers",order_by=creat_time.desc()))
    author = db.relationship(UserModel,backref="answers")

# 邮箱验证码数据库
# class EmailCaptchaModel(db.Model):
#     __tablename__ = "emali_captcha"
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     email = db.Column(db.String(100), nullable=False)
#     captcha = db.Column(db.String(100), nullable=False)
#     # tage = db.Column(db.Boolean,default=False)  可以用来判断验证码是否被使用了

