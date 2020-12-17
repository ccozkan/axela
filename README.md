
# AXELA

Telegram Bot for controlling your Raspberry Pi and make it perform on custom voice commands. It is like Alexa, but not really.


### installation

#### set up credentials

```
git clone https://github.com/ccozkan/axela
cd axela
cp credentials.py_example credentials.py
```

1) go to @botfather at Telegram and create yourself a bot
2) save your api token next to `API_TOKEN=` on credentials.py (with surrounding quotes)
3) go to @rawdatabot and type something, grab ["message"]["from"]["id"]
4) save this next to `CHAT_ID=` on credentials.py (without quotes)

#### minimum a.k.a. 'I am going to implement my own auxillary scripts'

```
bash setup_minimum.sh
```

#### complete a.k.a. 'I might use present auxillary scripts as well'

```
bash setup_complete.sh
```

