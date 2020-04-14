class Config:
    """Configurarea serverului"""
    TESTING = True

    """Configurarea bazei de date"""
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db/matches.db'
