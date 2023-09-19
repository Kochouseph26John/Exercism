EXPECTED_BAKE_TIME = 40


def bake_time_remaining(c:int):
    """ This functon returns remaining bake time
    it is calculated as 40-current time
    """
    return EXPECTED_BAKE_TIME-c

def preparation_time_in_minutes(l:int):
    """ This functon returns total preparation time
    it is calculated as 2*number of layers time
    """
    return l*2

def elapsed_time_in_minutes(number_of_layers:int,elapsed_bake_time:int):
    """ This functon returns total time elapsed
    it is calculated
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
