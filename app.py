from flask import Flask, request
from flask import jsonify
from flask import render_template
#import ip_header_decode

app = Flask(__name__)


@app.route("/",  methods=['POST', 'GET'])
def showMap(coordarr):
    coordarrx, coordarry = [list(c) for c in zip(*coordarr)]
    print coordarrx, coordarry
    return render_template('locate.html', coordarrx=coordarrx, coordarry=coordarry)

if __name__ == "__main__":
    app.run()