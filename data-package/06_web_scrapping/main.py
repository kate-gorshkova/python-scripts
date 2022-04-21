from lxml import html
import requests
import re

my_req = requests.get("http://www.columbia.edu/~fdc/sample.html")
text = my_req.text
result = re.findall(r'<*?>(.*)</.*?h3>', text)
print(result)

tree = html.fromstring(text)
my_list = [subtitle.text for subtitle in tree.xpath('//h3')]
print(my_list)

# зачёт!
