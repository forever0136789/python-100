#dateutil是个第三方库
from dateutil import parser
dt = parser.parse("Aug 28 2015 12:00AM")
print (dt)
#输出应为——2015-08-28 00:00:00
