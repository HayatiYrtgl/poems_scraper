# poems_scraper
# Web Scraping Poems

This Python script is designed for web scraping poems and poet information from a poetry website. It utilizes the BeautifulSoup and requests libraries for web scraping.

## ScrapPoems Class

### Initialization

```python
class ScrapPoems:
    def __init__(self):
        self.web_address = "https://siir.sitesi.web.tr/sairler.html"
        self.poet_list = []
        self.poem_list = []
```

### Requester Method

```python
    def requester(self, address):
        req = re.get(address)
        status_code = req.status_code
        if status_code == 200:
            print("Connected to", address)
            return req.content
        else:
            print(f"{status_code} Error")
```

### Parser Methods

#### Link Parser

```python
    def parser(self, content, tag=None, object=None):
        parsed_content = beauty(content, "lxml")
        tag = tag
        parsed_content = parsed_content.findAll("div", attrs={"class": "siir"})
        for i in parsed_content:
            for x in i:
                object.append(x.get(tag))
```

#### Text Parser

```python
    def text_parser(self, content):
        parsed_content = beauty(content, "lxml")
        parsed_content = parsed_content.findAll("div", attrs={"class": "text"})
        for i in parsed_content:
            with open("siirler.txt", "a", encoding="utf-8") as file:
                file.write(i.text)
```

## Usage

### Part 1

```python
c = ScrapPoems()
s = c.requester(c.web_address)
c.parser(s, tag="href", object=c.poet_list)

# Parse and write the file
for i in c.poet_list:
    s2 = c.requester(i)
    c.parser(s2, tag="href", object=c.poem_list)

print(c.poet_list, c.poem_list, sep="\n")

with open("poems_list.txt", "a", encoding="utf-8") as file:
    file.write(str(c.poem_list))
```

### Part 2

```python
with open("poems_list.txt", "r", encoding="utf-8") as file:
    f = file.read()
    f = eval(f)

c = ScrapPoems()

# Parse and get text
progress = 0
for link in f:
    progress += 1
    if progress < 0:
        pass
    else:
        s = c.requester(link)
        c.text_parser(s)
        print(f"{progress}/{len(f)}")
```

## Note

- Use this script responsibly and ensure compliance with the terms of service of the website you are scraping.
