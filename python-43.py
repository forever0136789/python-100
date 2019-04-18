class Num:
    #作用域在类内
    nNum = 1
    def inc(self):
        self.nNum += 1
        print( 'nNum = %d' % self.nNum)

if __name__ == '__main__':
    #作用域在主函数
    nNum = 2
    inst = Num()
    for i in range(3):
        nNum += 1
        print( 'The num = %d' % nNum)
        inst.inc()
