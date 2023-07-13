from .database import Base
from sqlalchemy import Integer, String, Column, Boolean,Date
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text


class Vaccine(Base) :
    __tablename__ = "vaccine_table"
    id = Column(Integer,primary_key=True, nullable=False)
    name = Column(String, nullable = False)


class Vaccination(Base) :
    __tablename__ = "vaccination_table"
    id = Column(Integer,primary_key=True, nullable=False)
    user_id = Column(Integer, nullable=False)
    vaccine_id = Column(Integer, nullable=False, default=1)
    vaccination_date = Column(Date, nullable = False)
    verified = Column(Boolean, nullable=False, default=False)
    certificate_url = Column(String, nullable=True, default = None)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))


