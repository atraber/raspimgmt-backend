from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(
    'mysql+pymysql://raspimgmt:raspberrypi@192.168.0.150/raspimgmt?charset=utf8',
    connect_args = {
        'port': 3306
    },
    echo='debug',
    echo_pool=True
)

db_session = scoped_session(
    sessionmaker(
        bind=engine,
        autocommit=False,
        autoflush=False
    )
)

Base = declarative_base()

def init_db():
    import db.models
    Base.metadata.create_all(engine)

    from db.models import Device, Stream
    db_session.add_all([
        Device(name='admin'),
        Device(name='test'),
        Stream(name='test'),
        Stream(name='test2'),
        Stream(name='test4'),
    ])
    db_session.commit()

    print('Initialized the database.')
