from sqlalchemy_utils import database_exists, create_database
from user_details import username, password

if not database_exists(f'postgresql://{username}:{password}@localhost/ipl_db'):
    create_database(f'postgresql://{username}:{password}@localhost/ipl_db')
