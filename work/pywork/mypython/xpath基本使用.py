# 导入etree

from lxml import etree

# 1. xpath解析本地文件
tree = etree.parse("1.html")

# 通过xpath路径解析
list = tree.xpath("//body/div/ul/li/a/text()")

print(list)




