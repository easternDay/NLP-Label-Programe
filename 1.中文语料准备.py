# encoding = utf-8
import jieba
import codecs
import re
import zhconv

stopwords = [line.strip() for line in open(
    'Chines_stopwords.txt', encoding='UTF-8').readlines()]


# 去除停用词
def remove_stopwords(list):
    return [word for word in list if word not in stopwords]

# 保留字母、数字、汉字和标点符号(),.!?":


def remove_others(s):
    return re.sub(r'[^a-zA-Z0-9\u4e00-\u9fa5(),.!?":]', ' ', s)


# 删除多余的空白(including spaces, tabs, line breaks)'''
def remove_whitespaces(s):
    return re.sub(r'\s{2,}', ' ', s)


# 删除社交文本中@某人的记录
def remove_atpeople(s):
    '''删除文本中@与其后面第一个空格之间的内容'''
    s = re.sub(r'@', ' @', s)
    s = re.sub(r':', ': ', s)
    ls = s.split()
    nls = []
    for t in ls:
        if t[0] == '@':
            continue
        else:
            nls.append(t)

    return ' '.join(nls)


# 主函数
if __name__ == '__main__':
    f = codecs.open('待标注分词字典.txt', "a+", 'utf-8')

    for line in codecs.open("zhwiki-latest-pages-articles.xml_2", "r", 'utf-8'):
        for i in re.sub('[a-zA-Z0-9]', '', line).split(' '):
            if i != '':
                content = zhconv.convert(i, 'zh-cn')
                content = remove_atpeople(content)
                content = remove_others(content)
                content = remove_whitespaces(content)
                data = list(jieba.cut(content, cut_all=False))
                readline = ' '.join(data) + '\n'
                f.write(readline)

    while(True):
        content = input("输入待分词句子：")
        if(content == '.exit'):
            break
        content = zhconv.convert(content, 'zh-cn')
        content = remove_atpeople(content)
        content = remove_others(content)
        content = remove_whitespaces(content)
        print(content)
        data = list(jieba.cut(content, cut_all=False))
        data = [i.strip() for i in data if str(i).strip() != ""]
        data = remove_stopwords(data)
        print(data)
        f.write(' '.join(data)+'\n')
    f.close()
