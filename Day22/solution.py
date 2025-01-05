import re
import copy
import numpy as np
import multiprocessing

def op1(price):
    return np.bitwise_xor(price*64, price) % 16777216

def op2(price):
    return np.bitwise_xor(int(price/32), price) % 16777216

def op3(price):
    return np.bitwise_xor(price*2048, price) % 16777216

def q1(prices):
    new_prices = {}
    for price in prices:
        new_price = price
        for i in range(2000):
            new_price = op3(op2(op1(new_price)))
        new_prices[price] = int(new_price)
    print(sum(new_prices.values()))

def get_banana(new_prices, new_prices_delta_str, seq):
    banana = 0
    for k, v in new_prices_delta_str.items():
        full_str = v
        if seq in full_str:
            index = full_str.index(seq)
            price_index = str.count(full_str[:index], ',') + 4
            banana += new_prices[k][price_index]
    #print("done for", seq)
    return banana

def run_parallel(new_prices, new_price_delta, new_price_delta_str):
    pool = multiprocessing.Pool()
    results = []
    total = len(new_price_delta)
    count = 1
    searched = set()
    for k, v in new_price_delta.items():
        print("progress: ", count, "/", total, sep='')
        count += 1
        for i in range(len(v) - 3):
            seq = "," + ",".join(v[i:i+4]) + ","
            if seq in searched:
                continue
            else:
                searched.add(seq)
            result = pool.apply_async(get_banana, (new_prices, new_price_delta_str, seq,))
            results.append(result)

    pool.close()
    pool.join()

    return [result.get() for result in results]

def q2(prices):
    new_prices = {}
    new_price_delta = {}
    seq_price_map = {}
    searched = set()
    for price in prices:
        new_price = price
        for i in range(2000):
            new_price = int(op3(op2(op1(new_price))))
            if price in new_prices:
                new_prices[price].append(new_price%10)
                new_price_delta[price].append(str(new_prices[price][-1] - new_prices[price][-2]))
            else:
                new_prices[price] = [new_price%10]
                new_price_delta[price] = []

    most_banana = 0
    total = len(new_price_delta)
    count = 1
    new_price_delta_str = {}
    max_banana = 0
    for k, v in new_price_delta.items():
        #new_price_delta_str[k] = "," + ",".join(v) + ","
        for i in range(len(v) - 3):
            seq = "," + ",".join(v[i:i+4]) + ","
            price_map = {}
            if seq in seq_price_map:
                price_map = seq_price_map[seq]
            if k not in price_map:
            #if True:
                price_index = i + 4
                price_map[k] = new_prices[k][price_index]
            seq_price_map[seq] = price_map
            max_banana = max(max_banana, sum(price_map.values()))
    
    #result = run_parallel(new_prices, new_price_delta, new_price_delta_str)
    #most_banana = result.sort()[-1]
    print(seq_price_map)
    print(max_banana)
"""
    for k, v in new_price_delta.items():
        print("progress: ", count, "/", total, sep='')
        count += 1
        for i in range(len(v) - 3):
            seq = "," + ",".join(v[i:i+4]) + ","
            if seq in searched:
                continue
            else:
                searched.add(seq)
            banana = get_banana(new_prices, new_price_delta_str, seq)
            #print(banana, ":", seq)
            most_banana = max(most_banana, banana)
"""
if __name__ == '__main__':
    with open("./input1.txt", "r") as file:
        prices = []
        for line in file:
            line = line.strip()
            prices.append(int(line))
        q2(prices)
