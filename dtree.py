# -*- coding:utf-8 -*-
from math import log
import uniout  # 列表打印能够输出中文


def cnt_majority(data):
    cnt = {}
    for item in data:
        f = item[-1]
        if f not in cnt:
            cnt[f] = 1
        else:
            cnt[f] += 1
    max_times = -1
    ans = None
    for key in cnt.keys():
        if cnt[key] > max_times:
            max_times = cnt[key]
            ans = key
    return ans


def create_decision_tree(data_set, labels):
    # if all the vectors in data_set belong to the same class,return
    class_list = [vector[-1] for vector in data_set]
    class_set = set(class_list)
    if len(class_set) == 1:
        return class_list[0]
    # no labels to cut. return
    if len(labels) == 0:
        return cnt_majority(data_set)
    label_id = find_best_label(data_set)
    label = labels[label_id]
    print 'the label we get:', label
    tree_node = {label: {}}
    val_set = set([val[label_id] for val in data_set])
    print 'val set', val_set
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
            tmp.extend(vector[label_id + 1:])
            new_data_set.append(tmp)
    return new_data_set


def find_best_label(data_set):
    ans = find_by_best_gain(data_set)
    return ans


def find_by_best_gain(data_set):
    print 'data_set:', data_set
    num_features = len(data_set[0]) - 1
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
        info_gain = info_ent - new_ent
        if info_gain > max_info_gain:
            max_info_gain = info_gain
            best_label = i
    print 'best label in this round:', best_label
    return best_label


def cal_info_ent(data_set):
    '''
    cal the Shannon ent value
    '''
    feature_cnt = {}
    size = len(data_set)
    total_ent = 0.0
    for vector in data_set:
        cur = vector[-1]
        if cur in feature_cnt.keys():
            feature_cnt[cur] += 1
        else:
            feature_cnt[cur] = 1
    for key in feature_cnt.keys():
        prob = float(feature_cnt[key]) / size
        print 'prob ', prob
        total_ent -= prob * log(prob, 2)
    return total_ent


def create_data_set(path):
    i_file = open(path, 'r')
    data = []
    label = []
    first_line = True
    for line in i_file:
        vector = line.strip().split(',')
        if first_line:
            first_line = False
            label = vector
        else:
            data.append(vector)
    i_file.close()
    return data, label


if __name__ == '__main__':
    f_path = r'C:\Users\User\MLpractice\datasets\wm2no_id.txt'
    print 'd-tree algorithm start!'
    print 'read data set where path = ', f_path
    my_data_set, my_labels = create_data_set(f_path)
    # test of create data_set
    # print data_set
    # print labels
    d_tree = create_decision_tree(my_data_set, my_labels)
    print d_tree


