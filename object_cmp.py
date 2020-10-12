import functools
import random
import enum
import operator

@enum.unique
class ExpressionType(enum.Enum):
    """
    Filter condition name definition.

    `EQ` means `==`. `LT` means `<`. `GT` means `>`. `LE` means `<=`. `GE` means
    `>=`. `IN` means filter value in the specified list.
    """
    EQ = 'eq'
    LT = 'lt'
    GT = 'gt'
    LE = 'le'
    GE = 'ge'
    IN = 'in'

    @classmethod
    def is_valid_exp(cls, key):
        """
        Judge that the input param is one of filter condition names in the class.

        Args:
            key (str): The input filter condition name.

        Returns:
            bool, `True` if the input filter condition name in the class,
            else `False`.
        """
        return key in cls._value2member_map_

    @classmethod
    def is_match(cls, except_key, except_value, actual_value):
        """
        Determine whether the value meets the expected requirement.

        Args:
            except_key (str): The expression key.
            except_value (Union[str, int, float, list, tuple]): The expected
                value.
            actual_value (Union[str, int, float]): The actual value.

        Returns:
            bool, `True` if the actual value meets the expected requirement,
            else `False`.
        """
        if actual_value is None and except_key in [cls.LT.value, cls.GT.value,
                                                   cls.LE.value, cls.GE.value]:
            return False

        try:
            if except_key == cls.IN.value:
                state = operator.contains(except_value, actual_value)
            else:
                state = getattr(operator, except_key)(actual_value, except_value)
        except TypeError:
            # actual_value can not compare with except_value
            return False
        return state


class LineageObj:
    def __init__(self, value):
        self.value = value
        self.summary_dir = "./" + str(value)

    def get_value(self, name):
        if name == "summary_dir":
            return self.summary_dir


def _cmp(obj1: LineageObj, obj2: LineageObj):
    value1 = obj1.value
    value2 = obj2.value

    if value1 is None and value2 is None:
        cmp_result = 0
    elif value1 is None:
        cmp_result = -1
    elif value2 is None:
        cmp_result = 1
    else:
        try:
            cmp_result = (value1 > value2) - (value1 < value2)
        except TypeError:
            type1 = type(value1).__name__
            type2 = type(value2).__name__
            cmp_result = (type1 > type2) - (type1 < type2)

    return cmp_result


objects = [
    LineageObj(random.random()) for _ in range(5)
]
objects.insert(3, LineageObj('NaN'))
objects.insert(4, LineageObj(0))

for object in objects:
    print(object.value)

print("===")

results = sorted(objects, key=functools.cmp_to_key(_cmp), reverse=False)

for result in results:
    # print(type(result))
    print(result.value)

print("===")

lineages = {}
for result in objects:
    lineages.update({result.summary_dir: result})
print(lineages)

condition = {
    'summary_dir': {
        "in": ["./0", "./NaN"]
    }
}


def _filter(lineage_obj: LineageObj):
    for condition_key, condition_value in condition.items():
        value = lineage_obj.get_value(condition_key)
        for exp_key, exp_value in condition_value.items():
            if not ExpressionType.is_valid_exp(exp_key):
                print("op is invalid")
            if not ExpressionType.is_match(exp_key, exp_value, value):
                return False
    return True


results = list(filter(_filter, lineages.values()))
for result in results:
    # print(type(result))
    print(result.value)
