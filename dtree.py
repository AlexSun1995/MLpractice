from math import log
def create_decision_tree(data_set, labels):
    # if all the vectors in data_set belong to the same class,return
    class_list = [vector[-1] for vector in data_set]
    class_set = set(class_list)
    if len(class_set) == 1:
        return
    # no labels to cut. return
    if len(labels) == 0:
        return
    label_id = find_best_label(data_set)
    label = lables[label_id]
    tree_node = {label:{}}
    val_set = set([val for val in data_set[label_id]])
    del(labels[label_id])
    for val in val_set:
        new_label = labels[:]
        new_data_set = split_data_set(data_set, label_id, val)
        tree_node[label][val] = create_decision_tree(new_data_set, new_label)
    return tree_node


def split_data_set(data_set, label_id, val):
    new_data_set = []
    for vector in data_set:
        if vector[label_id] == val:
            tmp = vector[:label_id]
            tmp.extend(data_set[label_id + 1 : ])
            new_data_set.append(tmp)
    return new_data_set


def find_best_label(data_set):
    ans = find_by_best_gain(dataset)
    return ans

def find_by_best_gain(data_set):
    num_features = len(data_set) - 1
    info_ent = cal_info_ent(data_set)
    best_label = -1
    max_info_gain = -1
    for i in range(num_features):
        new_ent = 0.0
        feature_val = [vector[i] for vector in data_set]
        unique_features = set(feature_val)
        for val in unique_features:
            sub_set = split_data_set(data_set, i, val)
            new_ent += cal_info_ent(sub_set)
        info_gain = new_ent - info_ent
        if info_gain > max_info_gain:
            max_info_gain = info_gain
            best_label = i
    return best_label


def cal_ent(data_set):
    '''cal the Shannon ent value'''
    feature_cnt = {}
    size = len(data_set)
    total_ent = 0.0
    for vector in data_set:
        cur = vector[-1]
        if cur in feature_cnt.keys():
            feature_cnt[cur] += 1
        else:
            feature_cnt[cur] = 0
    for key in feature_cnt.keys():
        prob = float(feature_cnt[key]) / size
        total_ent -= prob * log(prob,2)
    return total_ent

def create_data_set(path):
    ifile = open(path,'r')
    data_set = []
    for line in ifile:
        vector = line.splict(',')

    ifile.close()


if __name__ != '__main__':
    print 'd_tree algorithm'
    print "test of giiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiit"