import sys
sys.path.append(r'C:\Users\gua\Documents\GitHub\test\agileone01\page')
sys.path.append(r'C:\Users\gua\Documents\GitHub\test\agileone01\common')
import unittest
from HTMLTestRunner import HTMLTestRunner as TR
from common.log import Log

log = Log()
log._report()
fl_name = "%s/report.html" % Log.fl_path

suite = unittest.defaultTestLoader.discover("./testcase/", pattern="test*.py")

fl = open(fl_name, "wb")
runner = TR(stream=fl, title="Agileone Test")

runner.run(suite)
fl.close()