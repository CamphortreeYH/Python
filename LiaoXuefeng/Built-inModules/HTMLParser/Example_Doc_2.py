from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start tag:", tag)
        for attr in attrs:
            print("     attr:", attr)

    def handle_endtag(self, tag):
        print("End tag  :", tag)

    def handle_data(self, data):
        print("Data     :", data)

    def handle_comment(self, data):
        print("Comment  :", data)

    def handle_entityref(self, name):
        c = chr(name2codepoint[name])
        print("Named ent:", c)

    def handle_charref(self, name):
        if name.startswith('x'):
            c = chr(int(name[1:], 16))
        else:
            c = chr(int(name))
        print("Num ent  :", c)

    def handle_decl(self, data):
        print("Decl     :", data)

parser = MyHTMLParser()

#解析doctype：
parser.feed('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" '
            '"http://www.w3.org/TR/html4/strict.dtd">')

#解析具有几个属性和标题的元素：
parser.feed('<img src="python-logo.png" alt="The Python logo">')
parser.feed('<h1>Python</h1>')

#script和style元素的内容按原样返回，无需进一步解析：
parser.feed('<style type="text/css">#python { color: green }</style>')
parser.feed('<script type="text/javascript">'
            'alert("<strong>hello!</strong>");</script>')

#解析注释：
parser.feed('<!-- a comment -->'
            '<!--[if IE 9]>IE-specific content<![endif]-->')

#解析命名和数字字符引用并将它们转换为正确的char（注意：这3个引用都等效于'>'）：
parser.feed('&gt;&#62;&#x3E;')

向feed()提供不完整的块可以工作，但handle_data()可能会被调用多次（除非convert_charrefs设置为True）：
for chunk in ['<sp', 'an>buff', 'ered ', 'text</s', 'pan>']:
    parser.feed(chunk)

#解析无效的HTML（例如无参数属性）也工作：
parser.feed('<p><a class=link href=#main>tag soup</p ></a>')