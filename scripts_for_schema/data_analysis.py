from sqlalchemy import create_engine, func, desc
from sqlalchemy.orm import sessionmaker
from create_tables import Deliveries, Matches, Umpires
from user_details import username, password
import json


engine = create_engine(f'postgresql://{username}:{password}@localhost/ipl_db')

conection = engine.connect()

Session = sessionmaker(bind=engine)
session = Session()


def total_runs_scored():

    teams_and_runs = session.query(
        Deliveries.batting_team,
        func.count(Deliveries.total_runs).label('total_runs')).group_by(
            Deliveries.batting_team).order_by(Deliveries.batting_team).all()

    teams_and_runs = dict(teams_and_runs)

    with open("../json_data_files/TotalRunsScored.json", "w") as fp:
        json.dump(teams_and_runs, fp)


def top_batsman_rcb():

    batsman_rcb = session.query(
        Deliveries.batsman, func.sum(Deliveries.batsman_runs)
        ).filter(
            Deliveries.batting_team == 'Royal Challengers Bangalore'
            ).group_by(Deliveries.batsman).order_by(
                desc(func.sum(Deliveries.batsman_runs))).limit(17).all()

    batsman_rcb = dict(batsman_rcb)

    with open("../json_data_files/TopRcbBatsmen.json", "w") as fp:
        json.dump(batsman_rcb, fp)


def foreign_umpire():

    umpires_data = session.query(
        Umpires.nationality, func.count(Umpires.umpire).label('umpires_count')
        ).filter(Umpires.nationality != 'India').group_by(
            Umpires.nationality).all()

    umpires_data = dict(umpires_data)

    with open("../json_data_files/ForeignUmpires.json", "w") as fp:
        json.dump(umpires_data, fp)


def matches_team_season():

    seasons = session.query(
        Matches.season, Matches.first_team, Matches.second_team).all()

    teams_season = {}

    for data in seasons:
        season = int(data[0])
        team_one = data[1]
        team_two = data[2]

        if season not in teams_season:
            teams_season[season] = {}

        teams_season[season][team_one] = teams_season[season].get(
            team_one, 0)+1
        teams_season[season][team_two] = teams_season[season].get(
            team_two, 0)+1

    teams_season = dict(sorted(teams_season.items()))

    with open("../json_data_files/TeamsSeasonsGames.json", "w") as fp:
        json.dump(teams_season, fp)


def main():

    total_runs_scored()
    top_batsman_rcb()
    foreign_umpire()
    matches_team_season()


if __name__ == '__main__':
    main()
