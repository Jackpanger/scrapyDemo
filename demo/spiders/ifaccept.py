import json

import scrapy


def modify(toBeReplaced):
    for i in range(len(toBeReplaced)):
        toBeReplaced[i] = toBeReplaced[i].replace('”', '"').replace(" ", " ").replace("’", "'").replace("•",'')
    return toBeReplaced


class IfacceptSpider(scrapy.Spider):
    name = 'ifaccept'
    allowed_domains = ['scholars.cityu.edu.hk']
    with open("professor.json", 'r') as f:
        data = json.load(f)
    num = 0
    # start_urls = ["https://scholars.cityu.edu.hk/en/persons/chunyi-zhi(0c84bc59-0cf9-462f-8fb9-01c3c8dc6e3b).html"]
    start_urls = [data[num]["url"]]
    with open('accept.json', 'w') as f:
        f.write("[")

    # output = []

    def parse(self, response):
        ifAccept = response.xpath('//div[@class = "person-options"]').xpath("string(.)").get(2)
        if str(ifAccept).strip() == "Willing to take PhD students: yes":
            key = self.data[self.num]
            box = response.xpath('//div[@class="col-1-1 content"]/div[2]/div')
            print(box.css("h2::text").getall())
            for i, j in enumerate(box.css("h2::text").getall()):
                if j == "Research Interests/Areas":
                    content = modify(box.xpath("//div[@class='textblock'][{}]//*/text()".format(i + 1)).getall())
                    if content:
                        while '\n' in content:
                            content.remove('\n')
                        key["interests"] = content
                    else:
                        key["interests"] = []
                else:
                    content = modify(box.css(".textblock").xpath("string(.)").getall())
                    if content and len(content) > i:
                        key[j] = content[i]
                    else:
                        key[j] = []
                # elif j == 'Biography':
                #     # print(i)
                #     content = box.css("div>div").xpath("string(.)").getall()
                #     if content and len(content) > i:
                #         key["biography"] = content[i]
                #     else:
                #         key["biography"] = []
                # elif j == 'Teaching':
                #     content = box.css("div>div").xpath("string(.)").getall()
                #     if content and len(content) > i:
                #         key["teaching"] = content[i]
                #     else:
                #         key["teaching"] = []
            # print(key)
            # print(box.css("div>div li > *::text").getall())
            # print(box.css(".textblock").getall()[1])
            # print(box.xpath("//div[@class='textblock'][{}]/*/text()".format(1)).getall())
            # print(box.xpath("//div[@class='textblock'][2]//*/text()").getall())
            # print(len(box.css(".textblock").getall()))
            # print(box.css("div>div").xpath("string(.)").getall())
            # print(box.css("div>div").xpath("string(.)").getall()[1])
            # print(len(box.css("div>div").getall()))
            # print(len(box.css("h2,div").getall()))
            # key['Biography'] =
            # print(response.xpath('//div[@class = "textblock"]').xpath("string(.)").getall())
            with open('accept.json', 'a') as f:
                # json.dump(key, f)
                json.dump(key, f, indent=4)
                f.write(",")
            # with open('accept_de.json', 'a') as f:
            #     json.dump(key, f, indent=4)
            #     f.write(",")
            # self.output.append(json.dumps(self.data[self.num]))
        self.num += 1
        if self.num < len(self.data):
            yield scrapy.Request(url=self.data[self.num]['url'], callback=self.parse)
        else:
            with open('accept.json', 'a') as f:
                f.write("]")
        #     with open('accept.json', 'w') as f:
        #         json.dump(self.output, f, indent=4)
