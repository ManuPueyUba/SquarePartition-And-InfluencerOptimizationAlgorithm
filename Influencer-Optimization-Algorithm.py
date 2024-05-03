import sys


class Node:
    def __init__(self, current_list, rejected_list):
        self.current_list = []
        self.rejected_list = []

    def add_current_influencer(self, influencer):
        self.current_list.append(influencer)

    def add_rejected_influencer(self, influencer):
        self.rejected_list.append(influencer)

    def total_value(self):
        cant = sum(influ.pen_value for influ in self.current_list)
        return cant

    def unavailable_partners_count(self):
        return len(self.current_list)

    def copy_value_from(self, other_node):
        self.current_list = other_node.current_list.copy()
        self.rejected_list = other_node.rejected_list.copy()

    def return_current_list(self):
        return self.current_list.copy()

    def return_rejected_list(self):
        return self.rejected_list.copy()


class Influencer:
    def __init__(self, id, name, pen_value, uncompatible_partners):
        self.id = id
        self.name = name
        self.pen_value = pen_value
        self.uncompatible_partners = uncompatible_partners
        self.uncompatible_partners_count = len(uncompatible_partners)

    def add_denied_partner(self, influencer):
        self.denied_partners.append(influencer)

    def compatible_with(self, partners_list):
        if any(influencer.id in self.uncompatible_partners for influencer in partners_list):
            return False
        else:
            return True


def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j].pen_value <= pivot.pen_value:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1


def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)


def line_to_node(string_line):
    splitted_line = string_line.strip().split(",")
    uncompatible_partners = []

    for i in range(len(splitted_line)):

        if i == 0:
            id = int(splitted_line[i])
        elif i == 1:
            name = splitted_line[i]
        elif i == 2:
            pen_value = int(splitted_line[i])
        else:
            uncompatible_partners.append(int((splitted_line[i])))

    return Influencer(id, name, pen_value, uncompatible_partners)


def parse_influencer_file(file):
    list_size = 0

    with open(file, "r") as influencer_file:
        influencer_node_list = []
        for line in influencer_file:
            influencer_node_list.append(line_to_node(line))
            list_size = list_size + 1
        influencer_file.close()

    return influencer_node_list, list_size


def potential_value(influencer_list, node, cant_influencers, level):
    if cant_influencers == level + 1:
        return node.total_value()
    holes = cant_influencers - node.unavailable_partners_count() - (level + 1)
    return node.total_value() + (holes * influencer_list[level + 1].pen_value)


def bab(root_node_level, influencer_list, best_pen, best_combination, cant_influencers, root_node):
    if root_node_level == cant_influencers:
        if root_node.total_value() > best_pen:
            best_pen = root_node.total_value()
            best_combination = root_node.return_current_list()
        return best_combination, best_pen

    influencer_actual = influencer_list[root_node_level]

    left_node = right_node = Node([], [])
    right_node = Node([], [])

    right_node.copy_value_from(root_node)
    left_node.copy_value_from(root_node)

    left_node.add_current_influencer(influencer_actual)
    right_node.add_rejected_influencer(influencer_actual)

    potential_value_left = potential_value(influencer_list, left_node, cant_influencers, root_node_level)

    potential_value_right = potential_value(influencer_list, right_node, cant_influencers, root_node_level)

    if potential_value_left >= potential_value_right and influencer_actual.compatible_with(
            root_node.return_current_list()):
        best_combination, best_pen = bab(root_node_level + 1, influencer_list, best_pen, best_combination,
                                         cant_influencers, left_node)
        if best_pen < potential_value_right and influencer_actual.compatible_with(root_node.return_current_list()):
            best_combination, best_pen = bab(root_node_level + 1, influencer_list, best_pen, best_combination,
                                             cant_influencers, left_node)
    else:
        best_combination, best_pen = bab(root_node_level + 1, influencer_list, best_pen, best_combination,
                                         cant_influencers, right_node)
        if best_pen < potential_value_left and influencer_actual.compatible_with(root_node.return_current_list()):
            best_combination, best_pen = bab(root_node_level + 1, influencer_list, best_pen, best_combination,
                                             cant_influencers, left_node)

    return best_combination, best_pen


def branch_and_bound(influencer_node_list, cant_influencers):
    index = 0
    current_combination = []
    current_pen_value = 0

    best_combination = []
    best_pen_value = 0

    root_node_level = 0

    root_node = Node([], [])

    best_combination, best_pen_value = bab(root_node_level, influencer_node_list, best_pen_value, best_combination,
                                           cant_influencers, root_node)

    return best_combination, best_pen_value


def main():
    if len(sys.argv) == 1:
        print("To use the program, you must add a .csv file\n")
        print("example, 'python3 influencers.py example.csv'\n")
        return

    print("Executing using the file ", str(sys.argv[1]))

    influencer_list, list_size = parse_influencer_file(sys.argv[1])

    quickSort(influencer_list, 0, list_size - 1)
    influencer_list.reverse()

    best_combination_list, best_penetration_value = branch_and_bound(influencer_list, list_size)

    print("The best penetration is ", best_penetration_value)
    for x in best_combination_list:
        print("name: ", x.name)


main()
