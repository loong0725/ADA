import math
import time
import psutil
import numpy as np
import threading
from manim import *

# 改进的DFT实现
def native_dft(signal):
    N = len(signal)
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(M, signal)

# 优化的递归FFT
def recursive_fft(signal):
    N = len(signal)
    if N <= 32:
        return native_dft(signal)
    even = recursive_fft(signal[::2])
    odd = recursive_fft(signal[1::2])
    factor = np.exp(-2j * np.pi * np.arange(N) / N)
    return np.concatenate([even + factor[:N//2] * odd,
                         even + factor[N//2:] * odd])

# 优化的迭代FFT
def iterative_fft(x):
    N = len(x)
    x = np.asarray(x, dtype=complex)
    
    # Bit-reversal permutation
    j = 0
    for i in range(1, N):
        bit = N >> 1
        while j >= bit:
            j -= bit
            bit >>= 1
        j += bit
        if i < j:
            x[i], x[j] = x[j], x[i]
    
    # Cooley-Tukey算法
    L = 2
    while L <= N:
        angle = -2j * np.pi / L
        w = np.exp(angle * np.arange(L//2))
        for i in range(0, N, L):
            ix = i + L//2
            x[i:ix], x[ix:i+L] = (
                x[i:ix] + w * x[ix:i+L],
                x[i:ix] - w * x[ix:i+L]
            )
        L <<= 1
    return x

def measure_performance(fft_func, signal):
    process = psutil.Process()
    cpu_samples = []
    
    def monitor_cpu():
        while monitor_cpu.running:
            cpu_samples.append(process.cpu_percent(interval=0.1))
    
    # 预热运行
    for _ in range(2):
        _ = fft_func(signal.copy())
    
    # 启动监控线程
    monitor_cpu.running = True
    monitor_thread = threading.Thread(target=monitor_cpu)
    monitor_thread.start()
    
    # 正式测量
    start_memory = process.memory_info().rss 
    times = []
    for _ in range(5):
        start_time = time.perf_counter()
        result = fft_func(signal.copy())
        end_time = time.perf_counter()
        times.append(end_time - start_time)
    
    # 停止监控
    monitor_cpu.running = False
    monitor_thread.join()
    
    return {
        'time': np.mean(times),
        'cpu_avg': np.mean(cpu_samples),
        'cpu_max': np.max(cpu_samples),
        'memory': (process.memory_info().rss - start_memory)/1024**2
    }

def generate_realistic_signal(size):
    t = np.linspace(0, 1, size)
    signal = (0.5 * np.sin(2 * np.pi * 50 * t) + 
             1.0 * np.sin(2 * np.pi * 120 * t) +
             0.8 * np.sin(2 * np.pi * 300 * t))
    return signal + 0.1 * np.random.randn(size)

class BasePerformanceScene(Scene):
    def get_performance_data(self):
        signal_sizes = [2**n for n in range(6, 13)]
        algorithms = {
            "Native DFT": native_dft,
            "Recursive FFT": recursive_fft,
            "Iterative FFT": iterative_fft
        }
        
        performance = {name: {'time': [], 'cpu': []} for name in algorithms}
        for size in signal_sizes:
            signal = generate_realistic_signal(size)
            for name, func in algorithms.items():
                try:
                    res = measure_performance(func, signal)
                    performance[name]['time'].append((size, res['time']))
                    performance[name]['cpu'].append((size, res['cpu_avg']))
                except Exception as e:
                    print(f"{name} @ {size} error: {e}")
        return performance

class TimeAnalysis(BasePerformanceScene):
    def construct(self):
        performance = self.get_performance_data()
        
        axes = Axes(
            x_range=[0, 4096*1.1, 1024],
            y_range=[0, max(v[1] for data in performance.values() for v in data['time'])*1.1],
            x_length=9,
            y_length=6,
            axis_config={"font_size": 24}
        )
        
        labels = axes.get_axis_labels(
            x_label=Text("Input Size (N)", font_size=28),
            y_label=Text("Execution Time (s)", font_size=28)
        )
        
        colors = [RED, BLUE, GREEN]
        graphs = []
        legend_items = VGroup()
        
        for idx, (name, data) in enumerate(performance.items()):
            graph = axes.plot_line_graph(
                x_values=[p[0] for p in data['time']],
                y_values=[p[1] for p in data['time']],
                line_color=colors[idx],
                stroke_width=4
            )
            graphs.append(graph)
            
            dot = Dot(color=colors[idx], radius=0.1)
            label = Text(name, font_size=24).next_to(dot, RIGHT)
            legend_items.add(VGroup(dot, label))
        
        title = Text("Time Complexity Analysis", font_size=36).to_edge(UP)
        legend_items.arrange(DOWN, buff=0.3).to_corner(UL)
        complexity_note = Text("O(N²) vs O(N log N)", font_size=24).to_edge(DOWN)
        
        self.play(Write(title))
        self.play(Create(axes), Write(labels))
        self.wait(0.5)
        
        for graph in graphs:
            self.play(Create(graph), run_time=2)
        
        self.play(FadeIn(legend_items), Write(complexity_note))
        self.wait(3)

class CPUAnalysis(BasePerformanceScene):
    def construct(self):
        performance = self.get_performance_data()

        # 坐标轴定义
        axes = Axes(
            x_range=[0, 4096 * 1.1, 1024],
            y_range=[0, 100, 20],
            x_length=10,
            y_length=6,
            x_axis_config={
                "stroke_width": 2,
                "include_numbers": False,  # 不使用默认数字
            },
            y_axis_config={
                "stroke_width": 2,
                "font_size": 18
            }
        )

        # 自定义 x 轴标签
        x_labels = VGroup()
        sizes = [64, 256, 512, 1024, 2048, 4096]
        for size in sizes:
            label = Text(f"N={size}", font_size=18)
            label.rotate(45 * DEGREES)
            label.next_to(axes.c2p(size, 0), DOWN, buff=0.25)
            x_labels.add(label)

        # 坐标轴标签
        axis_labels = axes.get_axis_labels(
            x_label=Text("Input Size", font_size=24).next_to(axes.x_axis, DOWN, buff=0.8),
            y_label=Text("CPU Usage (%)", font_size=24)
        )

        # 曲线颜色与图例
        colors = [RED, BLUE, GREEN]
        graphs = []
        legend_items = VGroup()
        for idx, (name, data) in enumerate(performance.items()):
            graph = axes.plot_line_graph(
                x_values=[p[0] for p in data['cpu']],
                y_values=[p[1] for p in data['cpu']],
                line_color=colors[idx],
                stroke_width=3
            )
            graphs.append(graph)

            # 图例
            dot = Dot(color=colors[idx], radius=0.08)
            text = Text(name, font_size=20)
            legend_item = VGroup(dot, text).arrange(RIGHT, buff=0.2)
            legend_items.add(legend_item)

        # 图例布局
        legend_items.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        legend_items.to_corner(UL)

        # 标题和注释
        title = Text("CPU Utilization Analysis", font_size=36)
        title.to_edge(UP, buff=0.8)

        # 动画
        self.play(Write(title))
        self.play(Create(axes), Write(axis_labels), run_time=2)
        self.play(Write(x_labels))
        self.wait(0.5)

        for graph in graphs:
            self.play(Create(graph), run_time=1.5)

        self.play(
            FadeIn(legend_items, shift=RIGHT),
            run_time=2
        )
        self.wait(3)
