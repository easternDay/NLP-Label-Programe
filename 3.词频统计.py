#! python3
# -*- coding: utf-8 -*-
import os
import codecs
import jieba
from collections import Counter
import random


def get_words(content):
    seg_list = jieba.cut(content)
    c = Counter()
    for x in seg_list:
        if len(x) > 1 and x != '\r\n':
            c[x] -= 1
    print('不常用词频度统计结果')
    less_use_word = []
    for (k, v) in c.most_common(100):
        less_use_word.append(k)
    return less_use_word


if __name__ == '__main__':
    with codecs.open('待标注分词字典.txt', 'r', 'utf8') as f:
        content = f.read()
    less_use = get_words(content)
    print(less_use)
    word_num = random.randint(1, 3)
    random.shuffle(less_use)
    sentence = input("请用{}这{}个词进行造句：".format(
        "、".join(less_use[:word_num]), str(word_num)))
