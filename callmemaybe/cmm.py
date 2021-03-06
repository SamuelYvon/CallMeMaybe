import getopt
import json
import os.path as paths
import sys
from sys import stdin as stdin
from os import linesep as newline
from callmemaybe import VERSION as CMM_VERSION
from callmemaybe.Communicator import LogCommunicator, TwilioTextCommunicator, ALL_COMMUNICATORS

CONFIG_FILE = ".callmemaybe"
QUICK_ARG = "vhltc"


def usage(quick=True):
    """
    Print the usage message
    :param quick: whether we only want the call signature if you will (or not)
    :return: nothing, prints to STDOUT
    """
    print("cmm [-vhltc]")
    if not quick:
        print("Call me maybe (CMM) is a command line utility to send you results of shell script commands.")
        print("Options:")
        print(f"{newline}".join(map(lambda l: f"\t{l}", ["-h : this help menu.",
                                                         "-l : the log communicator that logs to a file.",
                                                         "-t : the Twilio communicator that sends you a text message.",
                                                         "-v : print the version.",
                                                         "-c : print the config file."])))
        print(
            "Observe that the {-h, -c, -v} parameters will NOT execute any communications and are mutually exclusive.")


def print_sample_config():
    """
    Prints the sample config file
    :return: nothing, prints to STDOUT
    """
    keys = set()
    for comm in ALL_COMMUNICATORS:
        for k in comm.KEYS:
            keys.add(k)

    print("{")
    lines = [f"\t\"{k}\" : \"value\"" for k in keys]
    print(",\n".join(lines))
    print("}")


def open_config():
    """
    Open the config file and parse it as a key-value dict
    :return: the KV-dict
    """
    path = paths.join(paths.expanduser("~"), CONFIG_FILE)

    content = ""
    try:
        with open(path, "r") as fh:
            content = "\n".join(fh.readlines())
    except FileNotFoundError as e:
        print(f"Config file not found at {e.filename}. Aborting.")
        exit(-1)

    try:
        d = json.loads(content)
    except json.JSONDecodeError:
        d = {}

    return d


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    config = open_config()

    try:
        opts, args = getopt.getopt(argv, QUICK_ARG)

        communicators = []

        for opt, arg in opts:
            if opt == "-h":
                usage(False)
                exit()
            elif opt == "-c":
                print_sample_config()
                exit()
            elif opt == "-l":
                communicators.append(LogCommunicator(config))
            elif opt == "-t":
                communicators.append(TwilioTextCommunicator(config))
            elif opt == "-v":
                print(f"CallMeMaybe Version {CMM_VERSION}")
                exit()

        text = stdin.read()
        results = map(lambda c: c.send(text), communicators)

        if not all(results):
            pass  # print err

        print(text)
    except getopt.GetoptError:
        usage()
        exit(-1)


if __name__ == '__main__':
    main(sys.argv[1:])
