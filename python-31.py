weekt={'u':'tuesday','h':'thurseday'}
weeks={'a':'saturday','u':'sunday'}
week={'m':'monday','w':'wednesday','f':'friday','t':weekt,'s':weeks}


a=week[(input('输入第一个字母：')).lower()]
if a==weekt or a==weeks:
    print(a[input('输入第二个字母：').lower()])
else:
    print(a)
