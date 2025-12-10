import json
from random import choice, randint

if __name__ == '__main__':

    num_variants = 5

    f = open("net_types.json")
    net_types = json.loads(f.read())
    f.close()

    task_types = ["klasifikace", "regrese", "multilabel klasifikace"]

    num_types = len(net_types)

    f = open("variants.json", "w")
    all_variants = []

    for i in range(num_variants):
        # choose the variant
        net_type = choice(net_types)
        task_type = choice(task_types)

        selection = {
            "figure_file": net_type["figure"],
            "task_type": task_type,
            "num_classes": net_type["classes"],
            "parameter_index1": randint(1, net_type["first_layer"]),
            "parameter_index2": randint(1, 2)
        }

        all_variants.append(selection)

    f.write(json.dumps(all_variants, indent=4))
    f.close()