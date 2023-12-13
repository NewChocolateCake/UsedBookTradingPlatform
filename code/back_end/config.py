# cookie中的scret_key
SECRET_KEY = "abcdefghijklmn;if"

# 数据库的配置信息
HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = 'es'
USERNAME = 'root'
PASSWORD = '123456'
DB_URL   = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URL

# 邮箱配置
MAIL_SERVER = "smtp.qq.com"
MAIL_USE_SSL = True
MAIL_PORT = 465
MAIL_USERNAME = "2122465349@qq.com"
MAIL_PASSWORD = "yofikeiheftlddfa" # 开启SMTP服务时生成的授权码
MAIL_DEFAULT_SENDER = "2122465349@qq.com"