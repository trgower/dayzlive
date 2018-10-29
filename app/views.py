import socket
import struct
from datetime import datetime, tzinfo, timedelta
from flask import render_template, jsonify
from app import app, models, time_badge_sm


def ip_to_uint32(ip):
   t = socket.inet_aton(ip)
   return struct.unpack("!I", t)[0]


def uint32_to_ip(ipn):
   t = struct.pack("!I", ipn)
   return socket.inet_ntoa(t)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/servers")
def servers():
    thirty_seconds_ago = datetime.utcnow() - timedelta(seconds=180)
    rservers = models.Servers.query.filter(models.Servers.last_updated >= thirty_seconds_ago).all()
    jservers = [{
        "v": s.version[3:4],
        "l": s.country.lower(),
        "n": s.name,
        "p": s.max_players,
        "t": s.hours,
        "h": s.hive,
        "m": s.mode,
        "a": s.num_players,
        "b": time_badge_sm(s.hours),
        "c": '%02d' % s.minutes,
        "s": s.time_speed,
    } for s in rservers]
    return jsonify({"data": jservers})


@app.route("/players/<ip>/<port>")
def players(ip, port):
    if not port.isdigit():
        return jsonify({"data"}, [{}])

    rplayers = models.Players.query.filter_by(ip=ip_to_uint32(ip), port=int(port)).all()
    jplayers = [{
        "i": p.index,
        "n": p.name,
        "d": str(p.duration)
    } for p in rplayers]
    return jsonify({"data": jplayers})
