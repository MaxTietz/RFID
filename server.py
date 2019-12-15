from server_settings import app, socketio, mysql, request, render_template
from RfidReader import RfidReader
from threading import  Lock

# Connect to Database on localhost
app.config['MYSQL_HOST'] = '0.0.0.0'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'RFID2'


# create an instance of the RFID Reader
rfid_reader = RfidReader()   
saveduid = 2910494131168

####
read_thread = None
read_thread_lock = Lock()

@app.route("/", methods=['GET', 'POST'])
def index():
    uid = 0
    #render the index template
    return render_template('index.html')


@app.route("/administration", methods=['GET', 'POST'])
def administration():   
    # Insert Into Database
    if request.method == "POST":
        try:
            details = request.form
            actionID = details['action_id']
            rfid = details['rfid']
            name = details['name']
            lastname = details['lastname']
            password = details['password']
            print(str(name))
            print(str(actionID))
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO rfidaction(ActionID, RFID) VALUES (%s, %s)", (actionID, rfid))
            cur.execute("INSERT INTO user(Name, LastName, Password) VALUES (%s, %s, %s)", (name, lastname, password))
            #cur.execute("SELECT * FROM rfid")
            #rows = cur.fetchall()
            # for row in rows:
            #    print(row)
            mysql.connection.commit()
            cur.close()
            return 'success'
        except:
            print("Fail")
            return 'FAIL'
    #GET at Load
    else: 
        #colname = [ d[0] for d in query.description ]
        #result_list = [ dict(zip(colname, r)) for r in query.fetchall() ]
        cur = mysql.connection.cursor()
        val = cur.execute("SELECT * FROM rfid WHERE RFID =  " + str(saveduid))
        rows = cur.fetchall()
        mysql.connection.commit()
        cur.close()
        isInDB = False
        #In this case the rfid is saved in the database
        if len(rows) > 0:
            isInDB = True
            rfid= rows[0][0]
            print(rfid)
        #the chip is a new chip
        else: 
            pass
    return render_template('administration.html')

#Start the thread to read rfid chips permanently on connection
@socketio.on('connect')
def connect():
    global read_thread
    with read_thread_lock:
        if read_thread is None:
            read_thread = socketio.start_background_task(rfid_reader.read)
    socketio.emit('message', {'msg': 'Start reading card!'})


@socketio.on('save_rfid')
def save_rfid(uid):
    saveduid = uid
    print(str(uid))

@socketio.on('message')
def message(msg):
    print('Message: ' + msg)

if __name__ == "__main__":
    socketio.run(app, debug=True, host='0.0.0.0', use_reloader=True)
