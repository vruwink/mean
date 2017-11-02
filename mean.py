def mean(num_list):
    for i in num_list:
	if isinstance(i, complex):
	  return NotImplemented
    try:
        return sum(num_list) *1.0/len(num_list)
    except ZeroDivisionError as detail :
        msg = "The algebraic mean of an empty list is undefined."
        msg += "Please provide a list of numbers."
        raise ZeroDivisionError(detail.__str__() + "\n" +  msg)
    except TypeError as detail :
        msg = "The algebraic mean of an non-numerical list is undefined."
        msg += "Please provide a list of numbers."
        raise TypeError(detail.__str__() + "\n" +  msg)
