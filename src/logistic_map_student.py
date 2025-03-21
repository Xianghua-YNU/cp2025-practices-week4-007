"""
Logistic映射与混沌系统研究
"""

import numpy as np
import matplotlib.pyplot as plt

def iterate_logistic(r, x0, n):
    """
    迭代Logistic映射
    """
    x = np.zeros(n)
    x[0] = x0
    for i in range(1, n):
        x[i] = r * x[i-1] * (1 - x[i-1])
    return x

def plot_multiple_time_series(r_values, x0, n):
    """
    绘制多个时间序列子图
    """
    fig, axs = plt.subplots(2, 2, figsize=(10, 8))
    axs = axs.flatten()
    for i, r in enumerate(r_values):
        x = iterate_logistic(r, x0, n)
        axs[i].plot(range(n), x, 'b-', linewidth=1)
        axs[i].set_title(f'r = {r}')
        axs[i].set_xlabel('迭代次数')
        axs[i].set_ylabel('x值')
        axs[i].grid(True, alpha=0.3)
    plt.tight_layout()
    return fig

def plot_bifurcation(r_min, r_max, step, n_iterations, n_discard):
    """
    绘制分岔图
    """
    r_values = np.arange(r_min, r_max + step, step)
    x0 = 0.5
    r_list = []
    x_list = []
    
    for r in r_values:
        x = x0
        # 舍弃前n_discard次迭代
        for _ in range(n_discard):
            x = r * x * (1 - x)
        # 记录后续迭代
        for _ in range(n_iterations - n_discard):
            x = r * x * (1 - x)
            r_list.append(r)
            x_list.append(x)
    
    fig = plt.figure(figsize=(12, 6))
    plt.plot(r_list, x_list, 'k.', markersize=0.1, alpha=0.3)
    plt.title('Logistic映射分岔图 (Feigenbaum Plot)')
    plt.xlabel('r')
    plt.ylabel('x')
    plt.grid(True, alpha=0.2)
    plt.tight_layout()
    return fig

def main():
    """主函数"""
    # 任务1：绘制四个子图
    r_values = [2.0, 3.2, 3.45, 3.6]
    x0 = 0.5
    n = 60
    
    fig = plot_multiple_time_series(r_values, x0, n)
    fig.savefig("task1_results.png", dpi=300)
    plt.close(fig)
    
    # 任务2：绘制分岔图
    fig = plot_bifurcation(2.6, 4.0, 0.001, 250, 100)
    fig.savefig("task2_feigenbaum.png", dpi=300)
    plt.close(fig)

if __name__ == "__main__":
    main()
