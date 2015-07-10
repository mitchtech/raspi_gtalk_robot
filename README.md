## What is it?
[**Spanish version**](https://github.com/UlisesGascon/raspi_gtalk_robot/blob/master/README_es.md)

This script will allow you to communicate directly with your Raspberry Pi using Gtalk / Google Hangouts.

You can run it in any device that supports google hangouts

[Check the video](http://youtu.be/vd6RlkAXWRs)

## How can I install it?

**1.** Install Python 2.7
```bh
sudo apt-get install python-pip git-core python2.7-dev
```
**2.** Update easy_install
```bh
sudo easy_install -U distribute
```
**3.** Install GPIO, xmpppy and pydns modules.
```bh
sudo pip install RPi.GPIO xmpppy pydns
```
**4.** Clone this repository.
```bh
git clone https://github.com/UlisesGascon/raspi_gtalk_robot.git
```
**5** Enter in the folder.
```bh
cd raspi_gtalk_robot
```
**6.** Edit raspiBot.py.
```bh
sudo nano raspiBot.py
```
**7.** Search for (BOT_GTALK_USER, BOT_GTALK_PASS, and BOT_ADMIN) in lines 31-33. Edit them and save all the changes.
```bh
raspi_bot_setup
```
**8.** Run the script.
```bh
sudo python ./raspiBot.py
```

## Main commands:

As [mitchtech](https://github.com/mitchtech) said in [this blog entry](http://mitchtech.net/raspberry-pi-google-talk-robot/):
> 
```
[pinon|pon|on|high] [pin] : turns on the specified GPIO pin
[pinoff|poff|off|low] [pin] : turns off the specified GPIO pin
[write|w] [pin] [state] : writes specified state to the specified GPIO pin
[read|r] [pin]: reads the value of the specified GPIO pin
[available|online|busy|dnd|away|idle|out|xa] [arg1] : set gtalk state and status message to specified argument
[shell|bash] [arg1] : executes the specified shell command argument after ‘shell’ or ‘bash’
```
>

## Additional resources

- [Raspberry Pi y Google Hangouts (Spanish)](http://www.blog.ulisesgascon.com/raspberry-pi-y-google-hangouts) by [Ulises Gascon](https://github.com/UlisesGascon)
- [Raspberry Pi Google Talk Robot (English)](http://mitchtech.net/raspberry-pi-google-talk-robot/) by [Michael Mitchell](https://github.com/mitchtech)
