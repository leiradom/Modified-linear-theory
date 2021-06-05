程序使用方法

无升力计算方法

首先，在程序外部获得体积分布，体积分布存入volume.txt中。

然后通过Sec_D求解二阶导数，放入se.txt中。

然后通过F_function求解F函数与未修正的压力信号

最后通过Shock_correction来确定激波位置


model1有三个状态  一个是Ma=1.26 Ma=1.41 Ma=2.01 提取位置均为h=10l=20
model2和model3

       '''
    for k in range(1,b0):
        X = np.insert(X,i+k,x0[k])
        Y = np.insert(Y,i+k,y0[k])
        '''
