
import requests
import json
from time import sleep
from iirc_codes import *

### Create TV Class ###

class TV:

    def __init__(self, name, local_ip, public_ip, endpoint, security_token):
        self.name = name = name
        self.local_ip = local_ip
        self.public_ip = public_ip
        self.endpoint = endpoint
        self.security_token = security_token

### Sony Bravia Smart TV Control Modules ###

class Bravia(TV):
    def send(service, method, params, id=1):
        headers = {'X-Auth-PSK': Bravia.security_token}
        body = {"method": method, "version": "1.0", "id": id,
                "params": [params]}
        return requests.post(
            Bravia.endpoint+service, data=json.dumps(body), headers=headers)

    def send_irc_code(ircc_code):

        if Bravia.public_ip:
            ip = Bravia.public_ip
        else:
            ip = Bravia.local_ip

        url = 'http://'+ip+'/sony/ircc'
        payload = ('<?xml version="1.0"?>'
                   '<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/" s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">'
                   '<s:Body>'
                   '<u:X_SendIRCC xmlns:u="urn:schemas-sony-com:service:IRCC:1">'
                   '<IRCCCode>%s</IRCCCode>'
                   '</u:X_SendIRCC>'
                   '</s:Body>'
                   '</s:Envelope>') % ircc_code

        response = requests.post(
            url,
            data=payload,
            headers={
                'X-Auth-PSK': Bravia.security_token,
                'SOAPAction': '"urn:schemas-sony-com:service:IRCC:1#X_SendIRCC"'
            }
        )

        if response.status_code != 200:
            raise RuntimeError(response)
        else:
            print(response)
            return response

    def setVol(val):
        Bravia.send('audio', 'setAudioVolume', {
                    "target": "speaker", "volume": val})
        # setVol("10")

    def setMute(val):
        Bravia.send('audio', 'setAudioMute', {"status": val})
        # setMute(False)

    def setPower(val):
        Bravia.send('system', 'setPowerStatus', {"status": val})
        # setPower(True)

    def setExtInput(kind, port):
        uri = "extInput:"+kind+"?port="+port
        Bravia.send('avContent', 'setPlayContent', {"uri": uri})
        # setExtInput('hdmi', '1')
    

    def getPowerStatus():
        return Bravia.send('system','getPowerStatus',None,50).json()['result']


    def getApplicationList():
        return Bravia.send('appControl', 'getApplicationList', None).json()['result']


    def setActiveApplication(app_name):
        app_list = Bravia.getApplicationList()
        for apps in app_list:
            for i in apps:
                title = i["title"]
                uri = i["uri"]
                app = {"title": title, "uri": uri}
                if app_name == app['title'].lower():
                    Bravia.send('appControl', 'setActiveApp', {"uri": uri})
                    sleep(10)
                    
    def getRemoteControllerInfo():
        Bravia.send('system', 'getRemoteControllerInfo', None)

    def pause():
        Bravia.send_irc_code(Pause)

    def play():
        Bravia.send_irc_code(Play)

    def home():
        Bravia.send_irc_code(Home)

    def back():
        Bravia.send_irc_code(Return)

    def volUp():
        Bravia.send_irc_code(VolumeUp)

    def volDown():
        Bravia.send_irc_code(VolumeDown)

    def mute():
        Bravia.send_irc_code(Mute)

    def power():
        Bravia.send_irc_code(TvPower)

    def confirm():
        Bravia.send_irc_code(Confirm)

    def next():
        Bravia.send_irc_code(Next)

    def prev():
        Bravia.send_irc_code(Prev)

    def rewind():
        Bravia.send_irc_code(Rewind)

    def forward():
        Bravia.send_irc_code(Forward)
    
    def up():
        Bravia.send_irc_code(Up)
        sleep(.25)

    def down():
        Bravia.send_irc_code(Down)
        sleep(.25)

    def left():
        Bravia.send_irc_code(Left)
        sleep(.25)

    def right():
        Bravia.send_irc_code(Right)
        sleep(.25)

    def exit():
        Bravia.send_irc_code(Exit)


# bravia = Bravia('<device_name>', '<ip_address>', '<public_ip>',
#                 'http://<ip_address>/sony/', '<security_token>')