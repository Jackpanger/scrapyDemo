import json

if __name__ == '__main__':
    with open("select_F.json", 'r') as f:
        content = json.load(f)
    print(len(content))
    a = []
    for i in content:
        if i["willing"] != 0:
            a.append(i)
    print(len(a))
    for i in sorted(a, key=lambda i: i['willing'], reverse=True):
        if i["willing"] != 0:
            print(i['url'])
            print(i['count'])
    # print(sorted(a, key=lambda i: i['count'], reverse=True))
