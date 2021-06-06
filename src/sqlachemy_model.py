import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from sqlachemy_setting import Base, ENGINE

class Model(Base):
    """
    モデル
    """
    __tablename__ = 'm_news'
    id = Column('id', Integer, primary_key = True)
    name = Column('name', String(100))
    description = Column('description', String(255))
    create_time = Column('create_time', DateTime)
    update_time = Column('update_time', DateTime)

def main(args):
    """
    メイン関数
    """
    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
    main(sys.argv)