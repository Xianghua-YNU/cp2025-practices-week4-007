"""
最小二乘拟合和光电效应实验
"""

import numpy as np
import matplotlib.pyplot as plt

def load_data(filename):
    """
    加载数据文件
    
    参数:
        filename: 数据文件路径
        
    返回:
        x: 频率数据数组
        y: 电压数据数组
    """
    x = [];y = []           #建立空列表存数据
    with open(filename,'r') as file:    #打开文件
        for i in file:                  #将文件按行读取
            x.append(float(i.split()[0]))
            y.append(float(i.split()[1]))
    return np.array(x),np.array(y)

def calculate_parameters(x, y):
    """
    计算最小二乘拟合参数
    
    参数:
        x: x坐标数组
        y: y坐标数组
        
    返回:
        m: 斜率
        c: 截距
        Ex: x的平均值
        Ey: y的平均值
        Exx: x^2的平均值
        Exy: xy的平均值
    """
    if len(x) == 0 or len(y) == 0:
        raise ValueError("输入数据不能为空")
    if len(x) != len(y):
        raise ValueError("x和y数组长度必须相同")
    Ex = x.mean()                       #使用numpy的函数计算平均数
    Ey = y.mean()
    Exx = (x**2).mean()
    Exy = (x*y).mean()
    m = (Exy - Ex*Ey)/(Exx -Ex**2)      #按公式计算
    c = (Exx*Ey - Ex*Exy)/(Exx -Ex**2)
    return  m,c,Ex,Ey,Exx,Exy

def plot_data_and_fit(x, y, m, c):
    """
    绘制数据点和拟合直线
    
    参数:
        x: x坐标数组
        y: y坐标数组
        m: 斜率
        c: 截距
    
    返回:
        fig: matplotlib图像对象
    """
    if np.isnan(m) or np.isnan(c):
        raise ValueError("斜率和截距不能为NaN")
    fig = plt.figure()              #创建图像对象
    plt.scatter(x,y)                #画散点图
    x_fit = np.linspace(min(x), max(x),100) #按拟合直线生成数据
    y_fit = m*x_fit + c
    plt.polar(x_fit, y_fit)         #画拟合直线
    plt.xlabel('频率')                #给出坐标轴
    plt.ylabel('电压')
    plt.rcParams['font.sans-serif']=['SimHei']
    return fig

def calculate_planck_constant(m):
    """
    计算普朗克常量
    
    参数:
        m: 斜率
        
    返回:
        h: 计算得到的普朗克常量值
        relative_error: 与实际值的相对误差(%)
    """
    if m <= 0:
        raise ValueError("斜率必须为正数")
    # 电子电荷
    e = 1.602e-19  # C
    h = m*e
    relative_error = abs(h - 6.626e-34)/6.626e-34
    # 提示: 实际的普朗克常量值为 6.626e-34 J·s
    return h,relative_error

def main():
    """主函数"""
    # 数据文件路径
    filename = r"millikan.txt"
    
    # 加载数据
    x, y = load_data(filename)
    
    # 计算拟合参数
    m, c, Ex, Ey, Exx, Exy = calculate_parameters(x, y)
    
    # 打印结果
    print(f"Ex = {Ex:.6e}")
    print(f"Ey = {Ey:.6e}")
    print(f"Exx = {Exx:.6e}")
    print(f"Exy = {Exy:.6e}")
    print(f"斜率 m = {m:.6e}")
    print(f"截距 c = {c:.6e}")
    
    # 绘制数据和拟合直线
    fig = plot_data_and_fit(x, y, m, c)
    
    # 计算普朗克常量
    h, relative_error = calculate_planck_constant(m)
    print(f"计算得到的普朗克常量 h = {h:.6e} J·s")
    print(f"与实际值的相对误差: {relative_error:.2f}%")
    
    # 保存图像
    fig.savefig("millikan_fit.png", dpi=300)
    plt.show()

if __name__ == "__main__":
    main()
