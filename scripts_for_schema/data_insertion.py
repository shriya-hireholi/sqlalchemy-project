import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from create_tables import Deliveries, Matches, Umpires
from user_details import username, password


engine = create_engine(f'postgresql://{username}:{password}@localhost/ipl_db')

conection = engine.connect()

Session = sessionmaker(bind=engine)
session = Session()

with open('data_source/deliveries.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for row in csv_reader:
        data = Deliveries(
            id=row[0],
            inning=row[1],
            batting_team=row[2],
            bowling_team=row[3],
            over=row[4],
            ball=row[5],
            batsman=row[6],
            non_striker=row[7],
            bowler=row[8],
            is_super_over=row[9],
            wide_runs=row[10],
            bye_runs=row[11],
            legbye_runs=row[12],
            noball_runs=row[13],
            penalty_runs=row[14],
            batsman_runs=row[15],
            extra_runs=row[16],
            total_runs=row[17],
            player_dismissed=row[18],
            dismissal_kind=row[19],
            fielder=row[20]
        )
        session.add(data)
    session.commit()


with open('data_source/matches.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for row in csv_reader:
        data = Matches(
            match_id=row[0],
            season=row[1],
            city=row[2],
            date=row[3],
            first_team=row[4],
            second_team=row[5],
            toss_winner=row[6],
            toss_decision=row[7],
            result=row[8],
            dl_applied=row[9],
            winner=row[10],
            win_by_runs=row[11],
            win_by_wickets=row[12],
            player_of_match=row[13],
            venue=row[14],
            umpire1=row[15],
            umpire2=row[16],
            umpire3=row[17]
        )
        session.add(data)
    session.commit()

with open('data_source/umpires.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for row in csv_reader:
        data = Umpires(
            umpire=row[0],
            nationality=row[1],
            first_officiated=row[2],
            last_officiated=row[3],
            no_of_matches=row[4]
        )
        session.add(data)
    session.commit()

# conection.execute('commit')
