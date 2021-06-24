import json
import pandas as pd

if __name__ == '__main__':
    with open("accept.json", 'r') as f:
        content = json.load(f)
    print(len(content))
    a = []
    for i in content:
        count = 0
        for j in i.keys():
            if i[j] is not None:
                count += len(i[j])
        i["count"] = count
        i["willing"] = 0
        a.append(i)
    for i in sorted(a, key=lambda i: i['count'], reverse=True):
        print(i['url'])
        print(i['count'])
    # print(sorted(a, key=lambda i: i['count'], reverse=True))
    with open("select_F.json", 'w') as f:
        for i in sorted(a, key=lambda i: i['count'], reverse=True):
            json.dump(i, f, indent=4)
    # print(len(content))
    # print(pd.DataFrame(content).to_csv("data.csv"))
