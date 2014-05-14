# simple function to convert
# base 10 integer into another base


def convert(value, newbase):
    places=[]
    while value > newbase:
      places.append(value % newbase)
      value = value/newbase
    places.append(value % newbase)
    places.reverse()
    return places

