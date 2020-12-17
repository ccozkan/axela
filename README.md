
# AXELA

Telegram Bot for controlling your Raspberry Pi and make it perform on custom voice commands. It is like Alexa, but not really.


### installation

#### set up credentials

```
git clone https://github.com/ccozkan/axela
cd axela
```

1) `cp credentials.py_example credentials.py`
2) go to @botfather at Telegram and create yourself a bot
3) save your api token on credentials.py
4) go to @rawdatabot and type something, grab ["message"]["from"]["id"]
5) save this on credentials.py as chat id

#### minimum a.k.a. 'I am going to implement my own auxillary scripts'

```
bash setup_minimum.sh
```

#### complete a.k.a. 'I might use present auxillary scripts as well'

```
bash setup_complete.sh
```

