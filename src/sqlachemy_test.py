# セッション変数の取得
from sqlachemy_setting import session
# モデルの取得
from sqlachemy_model import *

# 全件取得
models = session.query(Model).all()
for model in models:
    print(model.name)