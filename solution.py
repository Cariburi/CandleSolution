def birthdayCakeCandles(candles: list[int]) -> int:
    if len(candles) == 0:
        return 0
    
    big_candles = []
    biggest_candle = max(candles)
    
    for i in candles:
        if i == biggest_candle:
            big_candles.append(i)
        
        else:
            continue
    
    return len(big_candles)
