if __name__ == '__main__':
    filename = input('输入文件名:\n')
    fp = open(filename,"w")
    ch = input('输入字符串:\n')
    while ch != '#':
        fp.write(ch)
        ch = input('')
    fp.close()
