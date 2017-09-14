#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-14 19:42:50
# @Author  : Funyn (461547449@qq.com)
# @Link    : none
# @Version : $0.0.1$

from app import app

@app.route('/')
@app.route('/index/')
def index():
  return 'hello web'
