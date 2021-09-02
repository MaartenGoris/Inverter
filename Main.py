from waitress           import serve
from flask_restful      import Resource, Api
from flask              import Flask, render_template, make_response, request
import Inverter, time, threading

app= Flask('__main__', template_folder="templates")
api= Api(app)

QPIGS= bytes([0x51, 0x50, 0x49, 0x47, 0x53, 0xB7, 0xA9, 0x0D])

inverter1= Inverter.Inverter('Inverter1', "/dev/hidraw0")


@app.route('/')
def index():
    return make_response(render_template('index.html'))
    
def runApp():
    serve(app, host="0.0.0.0", port=8001)             #For production
    #app.run(host='0.0.0.0', port=8001, debug=False)  #For debugging

#Main loop
def runMain():
    print(str(QPIGS))
    while True:
        data= inverter1.query(QPIGS)
        print (data.decode('unicode_escape'))
        time.sleep(5)

#Entrypoint for program
if __name__ == '__main__':
    threading.Thread(target=runApp).start()
    runMain()

