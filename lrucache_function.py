def lru_cache(limit):
    def decorator(func):
        cache = {}
        def wrapper(*args):
            key = args
            if key not in cache:
                if (limit is None) or (limit is not None and len(cache) < limit):
                    cache[key] = func(*args)
                else:
                    del cache[next(iter(cache))]
                    cache[key] = func(*args)

            return cache[key]

        return wrapper

    return decorator

