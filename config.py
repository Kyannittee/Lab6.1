import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-key-for-local')
    
    if os.environ.get('DATABASE_URL'):
        # Для Render - используем PostgreSQL
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace('postgres://', 'postgresql://')
    else:
        # Для локальной разработки - MySQL
        SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:password@localhost/lab6'
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
