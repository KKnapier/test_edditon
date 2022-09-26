from . import name

class Lr_team_member():
  
  def __init__(self, family_name, personal_name, age, rank):
    self.family_name = family_name
    self.personal_name = personal_name
    self.age = age 
    self.rank = rank
    
  def greed(self):
    print('hello {} my name is {}'.format(name,self.name))

  def __call__(self):
    print('call関数内ではこの関数の使用方法について説明を書くことで説明文を簡単に呼び出すことができます。')
  
#やってみたいこと＿ランクを分ける関数、mmrが低い高いを判別してくれる関数、ここのページに名前を書かずに他のファイルに名前を書いておいて内容がバレないように関数を呼び起こす
