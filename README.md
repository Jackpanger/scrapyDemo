## Scrapy Demo
This is the first experience on scrapy. This demo is used for collecting professors information in cityU search page, which mainly focus on those who are willing to take phd students. The default urls are pages for professors in Department of Computer Science, Data Science and Information System.
### Related codes
1. **Path to the demo**

```
cd demo
```
2. **Collect the information of all professors and store to json file**

```
scrapy crawl professor -o professors.json
```
3. **Keep those who are willing to take phd students**
```
scrapy crawl ifaccept
```
4. Sort by number of characters
```
python extract.py 
```
#### As for simple usage, extra modification may not be added in the future.  