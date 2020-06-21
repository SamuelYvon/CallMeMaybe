class Communicator:
    KEYS = []

    def __init__(self, config: dict):
        pass

    def send(self, text: str):
        """
        Send the text to you
        :param text: the text
        :return: if sending the content was successful
        """
        pass


class TwilioTextCommunicator(Communicator):
    SID = "TWILIO_SID"
    AUTH = "TWILIO_AUTH"
    FROM = "TWILIO_TEXT_FROM"
    TO = "TWILIO_TEXT_TO"

    KEYS = [SID, AUTH, FROM, TO]

    def __init__(self, config):
        super().__init__(config)

        if any(map(lambda k: k not in config, TwilioTextCommunicator.KEYS)):
            raise ValueError(f"Missing a Twilio mandatory parameter from {','.join(TwilioTextCommunicator.KEYS)}.")

        self._sid = config[TwilioTextCommunicator.SID]
        self._auth = config[TwilioTextCommunicator.AUTH]
        self._from = config[TwilioTextCommunicator.FROM]
        self._to = config[TwilioTextCommunicator.TO]

    def send(self, text: str):
        from twilio.rest import Client
        client = Client(self._sid, self._auth)
        client.messages.create(
            to=self._to,
            from_=self._from,
            body=text
        )


class LogCommunicator(Communicator):
    FILE = "LOG_COMM_FILE"
    MODE = "LOG_COMM_MODE"

    KEYS = [FILE, MODE]

    def __init__(self, config: dict):
        super().__init__(config)

        if LogCommunicator.FILE not in config:
            raise ValueError(f"Missing the key {LogCommunicator.FILE} in config file.")

        file = config[LogCommunicator.FILE]
        mode = config[LogCommunicator.MODE] if LogCommunicator.MODE in config else "a"

        self._file = file
        self._mode = mode

    def send(self, text: str):
        try:
            with open(self._file, self._mode) as fh:
                fh.write(text)
        except FileNotFoundError:
            return False
        return True


ALL_COMMUNICATORS = [LogCommunicator,
                     TwilioTextCommunicator]
