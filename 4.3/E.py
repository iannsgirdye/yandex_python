# Накопление результата


def result_accumulator(f):
    results = []
    
    def decorator(*args, method="accumulate"):
        nonlocal results
    
        result = f(*args)    
        results.append(result)
        
        if method == "accumulate":
            return None
        else:
            drop_results = results
            results = []
            return drop_results
    
    return decorator
    