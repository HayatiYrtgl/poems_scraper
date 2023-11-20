from bs4 import BeautifulSoup as beauty
import requests as re


# class for scraping
class ScrapPoems:
    
    # initialize
    def __init__(self):
        
        self.web_address = "https://siir.sitesi.web.tr/sairler.html"
        
        # poet lşst
        self.poet_list =[]
        
        # poet's poems_list
        self.poem_list = []
        
    # requester
    def requester(self, address):
         
         # get request
         req = re.get(address)
         
         # inspect the status code
         status_code = req.status_code
         
         # control it
         if status_code == 200:
             print("connected ", address)
             return req.content
         else:
             print(f"{status_code} Error")
    
    # parser
    def parser(self,content, tag=None, object=None):
         
         # parse the content
         parsed_content = beauty(content, "lxml")
         
         # select the tag
         tag = tag
         
         # for loop
         parsed_content = parsed_content.findAll("div", attrs={"class":"siir"})
         
         # get all hrefs
         for i in parsed_content:
             for x in i:
                 object.append(x.get(tag))
             
             
c = ScrapPoems()
s = c.requester(c.web_address)
c.parser(s, tag="href", object=c.poet_list)

# parse and write the file

for i in c.poet_list:
    s2 = c.requester(i)
    c.parser(s2, tag="href", object=c.poem_list)
    
print(c.poet_list, c.poem_list, sep="\n")

with open("poems_list.txt", "a", encoding="utf-8") as file:
    file.write(str(c.poem_list))
    
