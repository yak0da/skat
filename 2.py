def speed(path, stops, times):
    from itertools import cycle
    
    stops_iter = cycle(stops)
    times_iter = iter(times)
    
    distance = 0
    stops_needed = next(stops_iter)
    stop_count = 0
    
    path_iter = iter(path)
    
    try:
        while True:
            try:
                segment = next(path_iter)
                distance += segment
                stop_count += 1
                
                if stop_count == stops_needed:
                    time = next(times_iter)
                    if time != 0:
                        yield distance / time
                    else:
                        yield 0.0
                    
                    distance = 0
                    stop_count = 0
                    stops_needed = next(stops_iter)
                    
            except StopIteration:
                if stop_count > 0 and distance > 0:
                    try:
                        time = next(times_iter)
                        if time != 0:
                            yield distance / time
                        else:
                            yield 0.0
                    except StopIteration:
                        return
                return
                
    except StopIteration:
        return

print(*list(speed([2, 3, 4] * 11, [3, 4, 5], [1, 2, 4, 8] * 3)))
