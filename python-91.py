import time
#time.ctime([secs])作用相当于asctime(localtime(secs))，未给参数相当于asctime()
print (time.ctime(time.time()))
#time.asctime([tupletime])接受时间元组并返回一个可读的形式为"Tue Dec 11 18:07:14 2008"
#（2008年12月11日 周二18时07分14秒）的24个字符的字符串。
print (time.asctime(time.localtime(time.time())))
#time.gmtime([secs])接收时间戳（1970纪元后经过的浮点秒数）并返回格林威治天文时间下的时间元组t。
print (time.asctime(time.gmtime(time.time())))
