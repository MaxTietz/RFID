from pirc522 import RFID
import time
import datetime
from server_settings import socketio


class RfidReader:
    '''Represents the RFID-Reader'''
    # Create new instance for the RFID reader
    rfid_reader = RFID() 
    uid = 0

    def read(self):
        '''Read the current RFID-Chip'''
        self.uid = 0
        while True:
            #wait for 1.5 seconds till next read
            socketio.sleep(1.5)
            #Wait for the tag
            self.rfid_reader.wait_for_tag()
            message = ''
            #Requests for tag.
            #Returns (False, None) if no tag is present, otherwise returns (True, tag type)
            (error, tag_type) = self.rfid_reader.request()
            if not error:
                # Read UID is saved here as a list of bytes to the tuple field uid        
                (error, _uid) = self.rfid_reader.anticoll()
                #Check if chip is completely read: UID of RFID Chips consists of exactly 5 bytes
                if not error and len(_uid) == 5:          
                    message = "Read new RFID-Chip: "
                    uidstring = ''
                    for uidvalue in _uid:
                        uidstring += str(uidvalue)                    
                    uidint = int(uidstring)
                    self.rfid_reader.stop_crypto()
                    print(message + str(uidint))
                    self.uid = uidint
                    #Send the new uid to the websocket
                    socketio.emit('save_rfid',  {'uid': str(self.uid)})
                else:
                    message = "Chip not correctly read."
                    print(message)
                    self.uid = 0  
            else:
                print("err")
                self.uid = 0
        #Calls GPIO cleanup    
        self.rfid_reader.cleanup()
