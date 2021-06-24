## Scrapy Demo
This is the first experience on scrapy. This demo is used for collecting professors information in cityU search page, which mainly focus on those who are willing to accept phd students. The default urls are pages for professors in Department of Computer Science, Data Science and Information System.
### Related codes
```
cd spiders
scrapy crawl professor -o professors.json
scrapy crawl ifaccept
python extract.py 
```
As for simple usage, extra modification may not add in the future.  