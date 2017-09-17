#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-14 19:42:50
# @Author  : Funyn (461547449@qq.com)
# @Link    : none
# @Version : $0.0.1$

from app import app
from exts import db
from models import User

@app.route('/')
@app.route('/index/')
def index():
  return 'hello web'

@app.route('/registe/')
def register():
  user = User('测试用名','测试邮箱')
  db.session.add(user)
  db.session.commit()
  return 'clear'
  
