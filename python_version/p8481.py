# import urllib.request
import sys
import os

def result():
    i = input()
    url = "https://raw.githubusercontent.com/k-young-passionate/serveralfiles/master/genzaw/gen"+i+".out"
    os.system("wget " + url)
    print(f)
    # f = urllib.request.urlopen(url)
    # print(f.read().decode())