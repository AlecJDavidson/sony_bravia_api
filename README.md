# Sony Bravia Smart TV Control API

This api uses the private rest api as well as the envelope api that processes the remote's iirc input.

Using this api is virtually the same as using the remote.


## Installation

Install from pypi:

```
pip install sony-bravia-api==1.01
```

Download and install the latest release using pip:

```
pip3 install sony_bravia_api-1.01.tar.gz
```

## Usage

```
### Import the module ###
from sony_bravia_api import Bravia

### Create your tv instance to be controlled ###
bravia = Bravia('<device_name>', '<ip_address>','http://<ip_address>/sony/', '<security_token>')

### Note: The security token is the token set in the ip control settings.

### Set TV Volume ###
### Takes an integer in the form of a string between 0 and 100 ###
bravia.setVol("10")

### Set TV Mute ###
### Takes a Boolean ###
bravia.setMute(True)

### Set Power ###
### Takes a Boolean ###
bravia.setPower(True)

### Set Active Input ###
### Takes the input type and it's number ###
bravia.setExtInput('hdmi', '1') ### Sets input to HDMI 1

### Get Power State ###
bravia.getPowerStatus() ### Returns power status,'active','inactive', and 'standby'

### Get Application list ###
bravia.getApplicationList() ### Returns the installed applications on the TV for use with the setActiveApplication function

### Set Active Application ###
bravia.setActiveApplication('netflix') ### Opens app

### Get Remote Info ###
bravia.getRemoteControllerInfo() ### Returns IIRC codes and remote status

### Play Button ###
bravia.play()

### Pause Button ###
bravia.pause()

### Home Button ###
bravia.home() ### Returns to tv home screen

### Back Button ###
bravia.back()

### Vol Up Button ###
bravia.volUp() ### Raises volume by 1

### Vol Down Button ###
bravia.volDown() ### Lowers volume by 1

### Mute Button ###
bravia.mute() ### Mutes the tv

### Power Button ###
bravia.power() ### Turns tv on or off

### Confirm Button ###
bravia.confirm()

### Next Button ###
bravia.next()

### Previous Button ###
bravia.prev()

### Rewind Button ###
bravia.rewind()

### Forward Button ###
bravia.forward()

### Up Button ###
bravia.up()

### Down Button ###
bravia.down()

### Left Button ###
bravia.left()

### Right Button ###
bravia.right()

### Exit Button ###
bravia.exit()



```
