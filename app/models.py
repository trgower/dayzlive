from app import db, app


class Servers(db.Model):
    __tablename__ = 'information'
    ip = db.Column("ip", db.Integer, primary_key=True)
    port = db.Column("port", db.Integer, primary_key=True)
    name = db.Column("name", db.String(64))
    num_players = db.Column("players", db.Integer)
    max_players = db.Column("max_players", db.Integer)
    hours = db.Column("hours", db.Integer)
    minutes = db.Column("minutes", db.Integer)
    environment = db.Column("env", db.String(1))
    protected = db.Column("protected", db.Boolean)
    battleye = db.Column("battleye", db.Boolean)
    version = db.Column("version", db.String(32))
    mode = db.Column("mode", db.String(1))
    hive = db.Column("hive", db.String(1))
    time_speed = db.Column("time_speed", db.Integer)
    last_updated = db.Column("last_updated", db.DateTime)
    country = db.Column("country", db.String(2))


class Players(db.Model):
    __tablename__ = 'players'
    ip = db.Column("ip", db.Integer, primary_key=True)
    port = db.Column("port", db.Integer, primary_key=True)
    index = db.Column("i", db.Integer, primary_key=True)
    name = db.Column("name", db.String(64))
    duration = db.Column("duration", db.DateTime)
    last_updated = db.Column("last_updated", db.DateTime)
