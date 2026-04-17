import os
from datetime import datetime
from idlelib import query

from flask import Blueprint, render_template, request, redirect, url_for

from pybo.models import Faq
from pybo import db
from pybo.forms import NoticeForm, AnswerForm
from pybo.models import Notice, Answer


bp = Blueprint('cs',__name__, url_prefix='/cs')

# notice_list
@bp.route("/notice/list")
def notice_list():
    page = request.args.get('page', type=int, default=1)

    notice_list = Notice.query.order_by(Notice.create_date.desc())

    notice_list = notice_list.paginate(page=page, per_page=15)  # 한페이지에 보여야할 게시물

    return render_template("cs/notice_list.html", notice_list=notice_list)

# notice_detail
@bp.route("/notice/detail/<int:notice_id>")
def notice_detail(notice_id):
    notice_detail = Notice.query.get(notice_id)
    prev_notice = Notice.query.get(notice_id - 1)
    next_notice = Notice.query.get(notice_id + 1)
    return render_template("cs/notice/notice_detail.html", notice=notice_detail, prev_notice=prev_notice, next_notice=next_notice)

@bp.route("/faq/list")
def faq_list():
    faq_list = Faq.query.all()
    print(faq_list)
    return render_template("cs/faq/faq.html" , faq_list=faq_list)

# 상세 페이지
# @bp.route("/faq/detail/<int:faq_id>")
# def faq_detail(faq_id):
#     faq = Faq.query.get(faq_id)
#
#     return render_template("cs/faq/faq.html", faq=faq)


