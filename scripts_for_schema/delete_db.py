from sqlalchemy_utils import drop_database
from user_details import username, password


drop_database(f'postgresql://{username}:{password}@localhost/ipl_db')
