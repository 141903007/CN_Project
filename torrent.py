from bencoding import bencode
from bencoding import Decoder
from bencoding import *
import re
with open('Tree - Introduction.pptx.torrent', 'rb') as f:
    meta_info = f.read()
    torrent = Decoder(meta_info).decode()
    # print(torrent)

with open("../trackers.txt") as file:
    data = file.read()
    https = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', data)
    # print(https)
    udp = re.findall('udp?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', data)
    # print(udp)
    all_urls = https + udp
    print(all_urls)

vscode://vscode.github-authentication/did-authenticate?windowid=1&code=e264996e77aac8544108&state=3b2dbbf8-6f1b-4dbd-a25e-9627c3c03281



