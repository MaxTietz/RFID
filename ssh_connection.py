from paramiko import client

class ssh:
    client = None

    def __init__(self, address, username, password):
        print("Connecting to server.")
        self.client = client.SSHClient()
        self.client.set_missing_host_key_policy(client.AutoAddPolicy())
        self.client.connect(hostname=address, username=username, password=password, look_for_keys=False)

    def sendCommand(self, command):
        if(self.client):
            stdin, stdout, stderr = self.client.exec_command(command)
            while not stdout.channel.exit_status_ready():
                # Print data when available
                if stdout.channel.recv_ready():
                    alldata = stdout.channel.recv(1024)
                    prevdata = b"1"
                    while prevdata:
                        prevdata = stdout.channel.recv(1024)
                        alldata += prevdata

                    print(str(alldata, "utf8"))
        else:
            print("Connection not opened.")

connectionWin = ssh("172.17.123.249", "DZ", "root")
#connectionWin.sendCommand(r'start "C:\Program Files\Mozilla Firefox\firefox.exe"')
#connection = ssh("172.17.124.7", "danielbeck", "A9d978e5.")
#connection.sendCommand("open -a /Applications/Firefox.app -g https://www.youtube.com/")
#connection.sendCommand("open -a /Applications/Spotify.app")
#connection.sendCommand("open -a /Applications/Bear.app")
