import os
from time import strftime

class Log:

    fl_path = ''

    def _report(self):
        fl_path = "./log/report_%s" % strftime("%Y_%m_%d_%H_%M_%S")
        os.mkdir(fl_path)
        Log.fl_path = fl_path
