#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-17 14:42:50
# @Author  : Funyn (461547449@qq.com)
# @Link    : none
# @Version : $0.0.1$

from flask import Flask
from exts import db
import config

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

from views import *

if __name__ == '__main__':
  app.run(port=80)
