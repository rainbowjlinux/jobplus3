#coding=utf-8


import os

# 项目运行环境
CURRENT_ENV = "dev"

class BaseConfig(object):
    """配置基类"""
    SECRET_KEY = os.urandom(24)


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://jobplus:jobplus@localhost:3306/jobplus_dev?charset=utf8'


class ProductionConfig(BaseConfig):
    """ 生产环境配置 """
    SQLALCHEMY_DATABASE_URI = "mysql+mysqldb://jobplus:jobplus@localhost:3306/jobplus?charset=utf8"


class TestingConfig(BaseConfig):
    """ 测试环境配置 """
    SQLALCHEMY_DATABASE_URI = "mysql+mysqldb://jobplus:jobplus@localhost:3306/jobplus_test?charset=utf8"


configs = {
    "dev": DevelopmentConfig,
    "prod": ProductionConfig,
    "test": TestingConfig
}