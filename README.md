# Call Me Maybe

_Call Me Maybe_ (cmm) is a command line tool to send the results of a command line (shell) script to _you_, whatever
_you_ might be.

```shell script
 ./compute_some_big_stuff.sh | awk "{some magic}" | cmm -t >> result.txt
```

And you will get, having configured the `twilio` settings, a text message with the results of your big compute.


## Getting started

`> pip3 install callmemaybe`

You will need to create a configuration file, so `cmm` knows who it has to send the information too. You can generate
a sample config file by simply doing:

`> cmm -c >> ~.callmemaybe`

After filling the fields you want to use, you're good to go!

## Supported "Communicators"

Right now, `cmm` supports the following:

-[X] Twilio Text Messages
-[X] Log Files (of course)
-[ ] Telegram Bots (WIP)

You can open up an issue with the label "NCommunicator" to suggest a new way of talking to you.

