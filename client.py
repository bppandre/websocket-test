import sys, getopt
import requests 
import json

class Client:
    """
    client class for application
    """

    def __init__(self):
        self.uid = 1
        self.hostname = "http://127.0.0.1:5000/"

    def start(self,args):
        print('-h for help')
        opts, arguments = getopt.getopt(args,"hrc:")
        for opt, val in opts:
            if opt == '-h':
                print('-c <number>\n-r request the result\n-t for chat\n-h for hostname')
            if opt == '-c':
                data_load = {'number':val}
                r = requests.post(self.hostname+'/submit', data =data_load)
                print(r)
            if opt == '-r':
                r =requests.get(self.hostname+'/result')
                print(r.content)



if __name__ == "__main__":
    client = Client()
    client.start(sys.argv[1:])