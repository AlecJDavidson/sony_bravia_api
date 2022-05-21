
import requests
import json
from time import sleep
from .iirc_codes import *

### Create TV Class ###

class TV:

    def __init__(self, name, ip_address, endpoint, security_token):
        self.name = name = name
        self.ip_address = ip_address
        self.endpoint = endpoint
        self.security_token = security_token

### Sony Bravia Smart TV Control Modules ###


class Bravia(TV):

    def send(self, service, method, params, id=1):
        headers = {'X-Auth-PSK': self.security_token}
        body = {"method": method, "version": "1.0", "id": id,
                "params": [params]}
        return requests.post(
            self.endpoint+service, data=json.dumps(body), headers=headers)

    def send_iirc_code(self, ircc_code):

        url = 'http://'+self.ip_address+'/sony/ircc'
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
                'X-Auth-PSK': self.security_token,
                'SOAPAction': '"urn:schemas-sony-com:service:IRCC:1#X_SendIRCC"'
            }
        )

        if response.status_code != 200:
            raise RuntimeError(response)
        else:
            print(response)
            return response

    def setVol(self, val):
        self.send('audio', 'setAudioVolume', {
                  "target": "speaker", "volume": val})
        # setVol("10")

    def setMute(self, val):
        self.send('audio', 'setAudioMute', {"status": val})
        # setMute(False)

    def setPower(self, val):
        self.send('system', 'setPowerStatus', {"status": val})
        # setPower(True)

    def setExtInput(self, kind, port):
        uri = "extInput:"+kind+"?port="+port
        self.send('avContent', 'setPlayContent', {"uri": uri})
        # setExtInput('hdmi', '1')

    def getPowerStatus(self):
        return self.send('system', 'getPowerStatus', None, 50).json()['result']

    def getApplicationList(self):
        return self.send('appControl', 'getApplicationList', None).json()['result']

    def setActiveApplication(self, app_name):
        app_list = self.getApplicationList()
        for apps in app_list:
            for i in apps:
                title = i["title"]
                uri = i["uri"]
                app = {"title": title, "uri": uri}
                if app_name == app['title'].lower():
                    self.send('appControl', 'setActiveApp', {"uri": uri})
                    sleep(10)

    def getRemoteControllerInfo(self):
        self.send('system', 'getRemoteControllerInfo', None)

    def pause(self):
        self.send_iirc_code(Pause)

    def play(self):
        self.send_iirc_code(Play)

    def home(self):
        self.send_iirc_code(Home)

    def back(self):
        self.send_iirc_code(Return)

    def volUp(self):
        self.send_iirc_code(VolumeUp)

    def volDown(self):
        self.send_iirc_code(VolumeDown)

    def mute(self):
        self.send_iirc_code(Mute)

    def power(self):
        self.send_iirc_code(TvPower)

    def confirm(self):
        self.send_iirc_code(Confirm)

    def next(self):
        self.send_iirc_code(Next)

    def prev(self):
        self.send_iirc_code(Prev)

    def rewind(self):
        self.send_iirc_code(Rewind)

    def forward(self):
        self.send_iirc_code(Forward)

    def up(self):
        self.send_iirc_code(Up)
        sleep(.25)

    def down(self):
        self.send_iirc_code(Down)
        sleep(.25)

    def left(self):
        self.send_iirc_code(Left)
        sleep(.25)

    def right(self):
        self.send_iirc_code(Right)
        sleep(.25)

    def exit(self):
        self.send_iirc_code(Exit)


# bravia = Bravia('<device_name>', '<ip_address>',
#                 'http://<ip_address>/sony/', '<security_token>')
