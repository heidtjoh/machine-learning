#!/usr/bin/python

from operator import itemgetter

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    split = int(9/10. * len(ages))
    
    errors = [pred - net_worth for pred, net_worth in zip(predictions, net_worths)]
    data = [(age, net_worth, error) for age, net_worth, error in zip(ages, net_worths, errors)]
 
    sorted_data = sorted(data,key=itemgetter(2))
    
    cleaned_data = sorted_data[:split]

    
    return cleaned_data

