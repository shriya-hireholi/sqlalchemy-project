from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from user_details import username, password


Base = declarative_base()
engine = create_engine(f'postgresql://{username}:{password}@localhost/ipl_db')

conection = engine.connect()

Session = sessionmaker(bind=engine)
session = Session()


class Deliveries(Base):
    __tablename__ = 'deliveries'

    delivery_id = Column(Integer, primary_key=True)
    id = Column(Integer)
    inning = Column(Integer)
    batting_team = Column(String(50))
    bowling_team = Column(String(50))
    over = Column(Integer)
    ball = Column(Integer)
    batsman = Column(String(30))
    non_striker = Column(String(30))
    bowler = Column(String(30))
    is_super_over = Column(Integer)
    wide_runs = Column(Integer)
    bye_runs = Column(Integer)
    legbye_runs = Column(Integer)
    noball_runs = Column(Integer)
    penalty_runs = Column(Integer)
    batsman_runs = Column(Integer)
    extra_runs = Column(Integer)
    total_runs = Column(Integer)
    player_dismissed = Column(String(50))
    dismissal_kind = Column(String(50))
    fielder = Column(String(50))


class Matches(Base):
    __tablename__ = 'matches'

    match_id = Column(Integer, primary_key=True)
    season = Column(String(20))
    city = Column(String(20))
    date = Column(Date)
    first_team = Column(String(50))
    second_team = Column(String(50))
    toss_winner = Column(String(50))
    toss_decision = Column(String(10))
    result = Column(String(10))
    dl_applied = Column(Integer)
    winner = Column(String(50))
    win_by_runs = Column(Integer)
    win_by_wickets = Column(Integer)
    player_of_match = Column(String(20))
    venue = Column(String(150))
    umpire1 = Column(String(30))
    umpire2 = Column(String(30))
    umpire3 = Column(String(30))


class Umpires(Base):
    __tablename__ = 'umpires'

    umpire_id = Column(Integer, primary_key=True)
    umpire = Column(String(30))
    nationality = Column(String(20))
    first_officiated = Column(Integer)
    last_officiated = Column(Integer)
    no_of_matches = Column(Integer)


Base.metadata.create_all(engine)
