from flask import Flask, render_template, jsonify, make_response, request, Response, json
import ip_header_decode
import jinja2
import json

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/",  methods=['POST', 'GET'])
def spawn():
    #coordarrx, coordarry = [list(c) for c in zip(*ip_header_decode.coordarr)]
    #print "coordinates: %s" % coordarrx, coordarry

    return render_template('index.html')#, coordarrx=coordarrx, coordarry=coordarry, malarr=malarr)

@app.route("/locate.html",  methods=['POST', 'GET'])
def showmap():
    coordarr, malarr = ip_header_decode.main()

    coordarrx, coordarry = [list(c) for c in zip(*coordarr)]

    coordjsonx = json.dumps(coordarrx)
    coordjsony = json.dumps(coordarry)

    print malarr
    #coordict = dict(coordjson)
    #print 'coordict: %s' % coordict


    return render_template('locate.html', coordarrx=coordjsony, coordarry=coordjsonx, malarr=malarr)#, arry=list(coordarry))

if __name__ == "__main__":
    app.run()