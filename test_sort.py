class Person(object):

    def __init__(self,age,name):
        self.age = age
        self.name = name


def personSort():
    persons = [Person(age,name) for (age,name) in [(12,"lili"),(18,"lulu"),(16,"kaka"),(12,"xixi")]]
    persons.sort(key=lambda x:x.age,reverse=True)
    for element in persons:
        print(element.age,":",element.name)
    print("=======================")


def operatorSort():
    persons = [Person(age,name) for (age,name) in [(12,"lili"),(18,"lulu"),(16,"kaka"),(12,"xixi")]]
    try:
        import operator
    except ImportError:
        cmpfun = lambda x:x.age
    else:
        key_set = ["age", "name"]
        cmpfun = operator.attrgetter(*key_set)

    persons.sort(key=cmpfun, reverse=True)
    for element in persons:
        print(element.age, ":", element.name)


personSort()
operatorSort()

import re
def _sorted_summary_files(summary_files, reverse):
    """Sort by timestamp increments and filename decrement."""
    sorted_files = sorted(summary_files,
                          key=lambda filename: (-int(re.search(r'summary\.(\d+)', filename)[1]), filename),
                          reverse=reverse)
    return sorted_files


files_name = [
    'test2.summary.12',
    'test1.summary.12',
    'test2.summary.15',
    'test1.summary.16'
]
sorted_files = _sorted_summary_files(files_name, True)
print(sorted_files)


hyper_parameters = [
    {"importance": 0.5, "name": "epoch"},
    {"importance": 0.9, "name": "batch_size"},
    {"importance": 0.5, "name": "batch"},
    {"importance": 0.0, "name": "[U]a"},
    {"importance": 0.0, "name": "[U]b"},
    {"importance": 0.0, "name": "[U]1"},
    {"importance": 0.0, "name": "[U]10"},
    {"importance": 0.0, "name": "[U]9"},
    {"importance": 0.0, "name": "batch"},
]

hyper_parameters.sort(key=lambda hyper_param: (-hyper_param.get("importance"),
                                               hyper_param.get("name").startswith('['),
                                               hyper_param.get("name")))

print(hyper_parameters)


# hyper_parameters.sort(key=lambda hyper_param: (hyper_param.get("importance"), hyper_param.get("name")), reverse=True)
