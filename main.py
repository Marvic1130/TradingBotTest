import pyupbit
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

if __name__ == '__main__':
    _df = pyupbit.get_ohlcv("KRW-ETH", interval="minute1", count=60)
    plt.plot(_df.open)  # 시가
    plt.plot(_df.high)  # 고점
    plt.plot(_df.low)  # 저점
    plt.plot(_df.close)  # 종가
    # plt.plot(_df.volume)
    # plt.plot(_df.value)
    plt.ylabel("Price")
    plt.xlabel("Time")
    plt.legend(["Open", "High", "Low", "Close", "Volume", "Value"])

    x_val = []
    y_val = []

    def animate():
        price = pyupbit.get_current_price("KRW-ETH")
        y_val.append(price)
        df = pyupbit.get_ohlcv("KRW-ETH", interval="minute1", count=60)
        plt.cla()
        plt.plot(df.open)  # 시가
        plt.plot(df.high)  # 고점
        plt.plot(df.low)  # 저점
        plt.plot(df.close)  # 종가
        plt.ylabel("Price")
        plt.xlabel("Time")
        plt.legend(["Open", "High", "Low", "Close"])

    ani = FuncAnimation(plt.gcf(), animate, interval=60000)

    plt.tight_layout()
    plt.show()
