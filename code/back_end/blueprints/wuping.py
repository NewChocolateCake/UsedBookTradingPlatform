from flask import Blueprint,render_template,request,g,redirect,url_for
from .forms import ESObjectForm,AnswerForm
from models import ESObjectModel,AnswerModel
from exts import db
from decorators import login_required
import io

bp = Blueprint("wuping",__name__,url_prefix="/")

@bp.route('/')
def index():
    return render_template("主页面.html")

# 发布闲置
@bp.route("/wuping/public",methods=['GET','POST'])
@login_required
def public_wuping():
    if request.method == 'GET':
        return render_template("二手/发布闲置.html")
    else:
        form = ESObjectForm(request.form)
        if form.validate():
            f = request.files['image']
            img_byte_arr = io.BytesIO()
            f.save(img_byte_arr)
            image = img_byte_arr.getvalue()

            title = form.title.data
            content = form.content.data
            price = form.price.data
            ESobject = ESObjectModel(title=title, content=content, price=price,image = image, author=g.user)
            db.session.add(ESobject)
            db.session.commit()
            # 可以跳转到商品的详情页
            return render_template("二手/商品详情页.html")
        else:
            print(form.errors)
            return redirect(url_for("wuping.public_wuping"))

# 二手交易商品详情页
@bp.route("/wuping/detail/<wuping_id>")
def wuping_detail(wuping_id):
    wuping = ESObjectModel.query.get(wuping_id)
    return render_template("二手/商品详情页.html",wuping=wuping)

# 二手商品详情页评论
@bp.route("/answer/public",methods=['POST'])
@login_required
def public_answer():
    form = AnswerForm(request.form)
    if form.validate():
        content = form.content.data
        wuping_id = form.wuping_id.data
        answer = AnswerModel(content=content,wuping_id=wuping_id,author_id=g.user.id)
        db.session.add(answer)
        db.session.commit()
        return redirect(url_for("wuping.wuping_detail.",wuping_id=wuping_id))
    else:
        print(form.errors)
        return redirect(url_for("wuping.wuping_detail",wuping_id=request.form.get("wuping_id")))


# 搜索功能
@bp.route("/search")
def search():
    # /search?q=flask
    # /search/<q>
    # post,request.form
    q = request.args.get("search")
    wupings = ESObjectModel.query.filter(ESObjectModel.title.contains(q)).all()
    return render_template("二手/商品搜索结果页面.html",wupings=wupings)



