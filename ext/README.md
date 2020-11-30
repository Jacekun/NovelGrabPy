# Extension Model

See [*ReadLNOrg.py*](/readlnorg.py) to start.

## Package Info
```
page = "https://www.readlightnovel.org/"
name = "ReadLightNovel"
version = "1.0.0"
author = "Jace"
```

## def basePage():
**Required. Don't change** <br>
```
def basePage():
    return page
```

## def extInfo(stringVal):
**Change how you want to display Package info**
```
def extInfo(stringVal):
    string = "Name: " + name + "\nVersion: " + version + "\nAuthor: " + author
    return stringVal + string
```

## def novelDetails(URL)
```
def novelDetails(URL)
    :param URL: Base Link of the webnovel
    :returns: List of strings
        [0] Alt. Names
        [1] Author
        [2] Artist
        [3] Desc
        [4] Year
        [5] Genre
```

## def chapterLinks(URL):
```
def chapterLinks(URL)
    :param URL: Base URL of Webnovel
    :returns: List of URLs of Chapter links
```

## def getChapterInfo(URL):
```
def getChapterInfo(URL):
    :param URL: Link of the chapter
    :returns: List
        -[0] Title
        -[1] Content 
```