from functools import reduce
import operator

class deep_nest(object):
    def __init__(self, input_dict=dict()):
        self.__plain_dict = input_dict.copy()

    def __query_nested_dict(self, dataDict, mapList=[]):
        if mapList:
            return reduce(operator.getitem, mapList, dataDict)
        else:
            return self.__plain_dict

    def __getitem__(self, keys):
        if type(keys) is not tuple: keys = (keys, )
        try:
            return self.__query_nested_dict(self.__plain_dict, keys[:-1])[keys[-1]]
        except:
            return None

    def __setitem__(self, keys, value):
        if type(keys) is not tuple: keys = (keys, )
        try:
            self.__query_nested_dict(self.__plain_dict, keys[:-1])[keys[-1]] = value
        except (KeyError, TypeError) as e:
            tmp = reduce(lambda x, y: dict({y: x}), reversed(list(keys)), value)
            self.__plain_dict.update(tmp)

    def __deep_delete__(self, keys, dict=None):
        if not dict: dict = self.__plain_dict
        if type(keys) is not tuple: keys = (keys,)
        if len(keys) > 1:
            empty = self.__deep_delete__(dict=dict[keys[0]], keys=keys[1:])
            if empty:
                del dict[keys[0]]
        else:
            del dict[keys[0]]
        return len(dict) == 0

    def __delitem__(self, keys, dict=None):
        try:
            self.__deep_delete__(keys, dict=dict)
        except:
            return None

    def __repr__(self):
        return str(self.__plain_dict)

    def keys(self):
        return self.__plain_dict.keys()

    def to_dict(self):
        return self.__plain_dict