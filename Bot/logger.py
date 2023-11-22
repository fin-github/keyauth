from time import time

class LoggerClass:
    def log(self,txt:str,extranl:bool = False):
        with open("logs.txt",'a') as file:
            file.write(f"{txt}, (time:{int(time())})\n")

    def start(self):
        self.log("------NEW SESSION!!!------")
