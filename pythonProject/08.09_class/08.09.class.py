import matplotlib.pyplot as plt
import pandas as pd


def read_csv(filename):
    list_of_data = pd.read_csv(filename)
    return list_of_data


def plot(dataset):
    dates = list(dataset.Date)
    sunspot = list(dataset['Monthly Mean Total Sunspot Number'])
    plt.figure(figsize=(60, 10))
    n = 25
    # res = pd.DataFrame(sunspot)
    # rolling_mean = res.rolling(window=n).mean()
    # plt.plot(rolling_mean, color='r')
    alpha = 0.5
    result = [sunspot[0]]
    for i in range(1, len(sunspot)):
        result.append(alpha * sunspot[i] + (1 - alpha) * result[i-1])
    plt.plot(dates, result, color='r')
    plt.plot(dates, sunspot)
    plt.show()


if __name__ == '__main__':
    file = 'Sunspots.csv'
    data = read_csv(file)
    plot(data)