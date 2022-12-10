from lxml import etree
import requests

'''
    Xpath:节点选取
        nodeName    选取此节点的所有子节点
        /           从根节点选取
        //          从匹配选的的当前节点选择文档中的节点，不考虑他们的位置
        .           选取当前节点
        ..          选取当前节点的父节点
        @           选取属性
        *           匹配任何元素节点
        @*          匹配任何属性节点
        Node()      匹配任何类型的节点
        
        谓语：
        /classroom/student[1]           选取classroom子元素的第一个student元素
        /classroom/student[last()]      选取classroom子元素的最后一个student元素
        /classroom/student[last()-1]    选取classroom子元素的倒数第二个student元素
        /classroom/student[position()<<3]    选取最前面的两个属于classroom子元素的student元素
        //name[@lang]                   选取所有name元素且拥有lang属性
        
        通配符：
        /classroom/*            选取classroom元素的所有子元素
        //*                     选取文档中所有元素
        //name[@*]              选取所有带属性的name元素
        //student/name|//student/age        选取student元素的所有name和age元素
        /classroom/student/name|//age       选取属于classroom元素的student元素的所有name元素，以及文档中所有的age元素
    
        内建函数：
        text()              ./text()                            文本匹配，表示取当前节点中的文本内容
        contains()          //div[contains(@id,'stu')]          模糊匹配，表示选择id中包含'stu'的所有div节点
        last()              //*[@lass='web'][last()]            位置匹配，表示选择@class='web'的最后一个节点
        position()          //*【@lass='site'][position()<=2]    位置匹配，表示选择@class='site'的前两个节点
        start-with()        “//input[start-with(@id,'st')]"      匹配id以st开头的元素
        ends-with()         “//input[ends-with(@id,'st')]"      匹配id以st结尾的元素
        concat(string1,string2)     concat('C语言中文网',.//*[@class='site']/@href)      C语言中文与标签类别属性为”site"的href地址做拼接
        
    CSS：
        .class              .intro      选择class='intro'的所有元素
        #:raise             #firstname  选择id='firstname'的所有元素
        *                   *           选择所有元素
        element             p           选择所有<p>元素
        element,element     div,p       选择所有<div>元素和<p>元素
        element element     div p       选择所有<div>元素内部的所有<p>元素
        [attribute]         [target]    选择带有target属性的所有元素
        [attribute=value]   [target=_blank]    选择target='_blank'的所有元素
        
'''


# 拿到源代码
url = "https://movie.douban.com/top250"

headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62"
}
resp = requests.get(url, headers=headers)
page_content = resp.text

print(page_content)

tree = etree.HTML(page_content)
result = tree.xpath('//title/text()')
print(result)