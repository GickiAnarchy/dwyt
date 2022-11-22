
import os
from pytube import YouTube, Search

def Get_YT(url):
    return YouTube(url)

def Do_Search(typed):
    ret = []
    if typed in (None, ""):
        return False
    sch = Search(typed)
    lst = sch.results
    for r in lst:
        t = r.title
        a = r.author
        u = r.watch_url
        x = (t,a,u)
        ret.append(x)
    return ret
