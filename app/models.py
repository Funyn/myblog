from exts import db 
from hashlib import md5
from datetime import datetime

class User(db.Model):
  __tablename__ = 'users'
  
  id = db.Column(db.String(100),primary_key=True)
  nickname = db.Column(db.String(100),unique=True)
  email = db.Column(db.String(100),unique=True)
  create_time = db.Column(db.DateTime,default=datetime.now)
  last_time = db.Column(db.DateTime,default=datetitme.ctime)
  
  def __init__(self,nickname,email):
      self.nickname = nickname
      self.email = email
      self.id = self.hash_id()
  
  #---------- 生成唯一密文的id-----------#
  def hash_id(self):
      md = md5()
      md.update(str(self.nickname)+str(create_time)).encode('utf-8'))
      self.id = md.hexdigest()
      return self.id
      
      
  
