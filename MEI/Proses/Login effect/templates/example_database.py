from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ExampleTable(Base):
    __tablename__ = 'afakahiya'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)

engine = create_engine('sqlite:///example_database.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

username_input = input("Masukkan username: ")
password_input = input("Masukkan password: ")

try:
    new_row = ExampleTable(username=username_input, password=password_input)
    session.add(new_row)
    session.commit()
    print("Data baru berhasil disimpan.")
except Exception as e:
    print("Terjadi kesalahan saat menyimpan data baru:", e)
    session.rollback()

all_rows = session.query(ExampleTable).all()
for row in all_rows:
    print(row.id, row.username, row.password)
