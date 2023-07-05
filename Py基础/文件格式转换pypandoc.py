"""
@author: JerryYang
@file: 文件格式转换pypandoc.py
@time: 2023/6/14 17:17
@desc:
"""
import pypandoc

"""
　　pypandoc.convert_file(source_file, to, format=None, extra_args=(), encoding='utf-8',
                 outputfile=None, filters=None, verify_format=True)
    参数说明：
    source_file:源文件路径
    to：输入应转换为的格式；可以是'pypandoc.get_pandoc_formats（）[1]`之一
    format：输入的格式；将从具有已知文件扩展名的源_文件推断；可以是“pypandoc.get_pandoc_formats（）[1]”之一（默认值= None)
    extra_args：要传递给pandoc的额外参数（字符串列表）(Default value = ())
    encoding：文件或输入字节的编码 (Default value = 'utf-8')
    outputfile：转换后的内容输出路径+文件名，文件名的后缀要和to的一致，如果没有，则返回转换后的内容（默认值= None)
    filters – pandoc过滤器，例如过滤器=['pandoc-citeproc']
    verify_format：是否对给定的格式参数进行验证，（pypandoc根据文件名截取后缀格式，与用户输入的format进行比对）

    pypandoc.convert_text(source, to, format, extra_args=(), encoding='utf-8',
                     outputfile=None, filters=None, verify_format=True):
    参数说明：
    source：字符串       
    其余和canvert_file()相同      
    
    支持输入格式：
biblatex, bibtex, commonmark, commonmark_x, creole, csljson, csv, docbook, docx, dokuwiki, epub, fb2, gfm, haddock, html, ipynb, jats, jira, json, latex, man, markdown, markdown_github, markdown_mmd, markdown_phpextra, markdown_strict, mediawiki, muse, native, odt, opml, org, rst, rtf, t2t, textile, tikiwiki, twiki, vimwiki 
支持输出格式：
asciidoc, asciidoctor, beamer, biblatex, bibtex, commonmark, commonmark_x, context, csljson, docbook, docbook4, docbook5, docx, dokuwiki, dzslides, epub, epub2, epub3, fb2, gfm, haddock, html, html4, html5, icml, ipynb, jats, jats_archiving, jats_articleauthoring, jats_publishing, jira, json, latex, man, markdown, markdown_github, markdown_mmd, markdown_phpextra, markdown_strict, mediawiki, ms, muse, native, odt, opendocument, opml, org, pdf, plain, pptx, revealjs, rst, rtf, s5, slideous, slidy, tei, texinfo, textile, xwiki, zimwiki
"""

# 将当前目录下html目录中的1.html网页文件直接转换成.docx文件，文件名为file1.docx，并保存在当前目录下的doc文件夹中
pypandoc.convert_file('D:\下载\白夜行 (东野圭吾) (Z-Library).epub', 'pdf', outputfile="D:\下载\白夜行 (东野圭吾) (Z-Library).pdf")

# # 将当前目录下html目录中的1.html网页文件 读取出来，然后转换成.docx文件，文件名为file2.docx，并保存在当前目录下的doc文件夹中
# with open('D:\下载\白夜行 (东野圭吾) (Z-Library).epub', encoding='ISO-8859-1') as f:
#     f_text = f.read()
# pypandoc.convert_text(f_text, 'epub', 'pdf', outputfile="D:\下载\白夜行 (东野圭吾) (Z-Library).pdf")