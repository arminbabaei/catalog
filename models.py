from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from passlib.apps import custom_app_context as pwd_context
import random, string
from itsdangerous import(
    TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)

Base = declarative_base()
secret_key = ''.join(random.choice(
    string.ascii_uppercase + string.digits) for x in range(32))

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    creation_date = Column(Date)
    username = Column(String(32), index=True)
    picture = Column(String(250))
    email = Column(String(250), index=True)
    password_hash = Column(String(64))

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    def generate_auth_token(self, expiration=600):
        s = Serializer(secret_key, expires_in=expiration)
        return s.dumps({'id': self.id})

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(secret_key)
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None
        except BadSignature:
            return None
        user_id = data['id']
        return user_id

    @property
    def serialize(self):
        return {
            'id': self.id,
            'creation_date': self.creation_date,
            'username': self.username,
            'picture': self.picture,
            'email': self.email
        }


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    creation_date = Column(Date)
    name = Column(String(80), nullable=False)
    

    @property
    def serialize(self):
        return {
            'id': self.id,
            'creation_date': self.creation_date,
            'name': self.name
        }


class CategoryItem(Base):
    __tablename__ = 'category_item'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    creation_date = Column(Date)
    color = Column(String(250))
    size = Column(String(250))
    price = Column(String(8))
    description = Column(String(250))
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'creation_date': self.creation_date,
            'name': self.name,
            'color': self.color,
            'size': self.size,
            'price': self.price,
            'description': self.description
        }


engine = create_engine('postgresql://catalog:catalog@localhost:5432/catalog')
Base.metadata.create_all(engine)
