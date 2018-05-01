from sqlalchemy import Column, DateTime, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from db.database import Base

device_streams_association_table = Table('device_streams', Base.metadata,
    Column('device_id', Integer, ForeignKey('devices.id')),
    Column('stream_id', Integer, ForeignKey('streams.id'))
)

class Parent(Base):
    __tablename__ = 'left'
    id = Column(Integer, primary_key=True)

class Device(Base):
    __tablename__ = 'devices'

    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    mac = Column(String(17))
    last_seen = Column(DateTime)
    streams = relationship("Stream",
                    secondary=device_streams_association_table)

    def __init__(self, id=None, name=None, mac=None):
        self.id = id
        self.name = name
        self.mac = mac

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'mac': self.mac,
            'last_seen': self.last_seen,
            'streams': [s.serialize() for s in self.streams],
        }

class Stream(Base):
    __tablename__ = 'streams'

    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    url = Column(String(255))
    width = Column(Integer)
    height = Column(Integer)

    def __init__(self, id=None, name=None, url=None):
        self.id = id
        self.name = name
        self.url = url

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'url': self.url,
            'width': self.width,
            'height': self.height,
        }
