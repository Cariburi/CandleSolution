def birthdayCakeCandles(candles: list[int]) -> int:
    if len(candles) == 0:
        return 0
    
    big_candle = []
    biggest_candle = max(candle)
    
    for i in candles:
        if i == biggest_candle:
            biggest_candle.append(i)
        
        else:
            continue
    
    return len(biggest_candle)
