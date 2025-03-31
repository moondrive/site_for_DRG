from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def main():
    return render_template('glav.html')


@app.route('/warthog')
def warthog():
    return render_template('guns/engineer/warthog/gun.html')


@app.route('/stubby')
def stubby():
    return render_template('guns/engineer/stubby/gun.html')


@app.route('/lok-1')
def lok_1():
    return render_template('guns/engineer/LOK-1/gun.html')


@app.route('/pgl_40mm')
def pgl():
    return render_template('guns/engineer/PGL/gun.html')


@app.route('/breach_cutter')
def breach():
    return render_template('guns/engineer/BC/gun.html')


@app.route('/shard')
def shard():
    return render_template('guns/engineer/shard/gun.html')


@app.route('/crspr')
def crspr():
    return render_template('guns/driller/crspr/gun.html')


@app.route('/cryo')
def cryo():
    return render_template('guns/driller/cryo/gun.html')


@app.route('/sludge')
def sludge():
    return render_template('guns/driller/sludge/gun.html')


@app.route('/subata')
def subata():
    return render_template('guns/driller/subata/gun.html')


@app.route('/epc')
def epc():
    return render_template('guns/driller/epc/gun.html')


@app.route('/cwc')
def cwc():
    return render_template('guns/driller/cwc/gun.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
