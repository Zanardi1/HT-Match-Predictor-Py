class Config:
    """Configurarea serverului"""
    TESTING = True
    SECRET_KEY = 'L1gwHsZZuGneTUwZKUevgBUe3HKIMBDiJv7DHwf1RjI'

    """Configurarea bazei de date"""
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db/matches.db'
