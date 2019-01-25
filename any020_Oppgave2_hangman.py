import random

def correct_guess(proposal, attempts, solution):
    if len(proposal) != 1 or proposal in attempts:
        return None

    elif proposal in solution:
        return True

    else:
        return False






