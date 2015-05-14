from sqlalchemy import create_engine, Column, String, Integer, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker
import pymysql

engine = create_engine('mysql+pymysql://root:root@localhost:8889/accesslog-orm', echo=True)
Base = declarative_base()

class Request(Base):
	__tablename__ = 'requests'

	id = Column(Integer, primary_key=True)
	name = Column(String(20))
	surname = Column(String(20))

	def __repr__(self):
		return "User -> name = '%s', surname = '%s'" % (self.name, self.surname)

Base.metadata.create_all(engine)

if __name__ == "__main__":

	test_request = Request(name="Pietje", surname="Piet")
	Session = sessionmaker(bind=engine)
	sess = Session()
	sess.add(test_request)
	sess.commit()
	test_request_fetched = sess.query(Request).first()
	print(test_request_fetched)


