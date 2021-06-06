#!usr/bin/python2.7
# coding=utf-8
import os, re, sys, json
from bs4 import BeautifulSoup as parser
from datetime import datetime

def main(self, cookie, url, config):
    ask = raw_input('\n     \x1b[1;97m    [*]\x1b[1;97m Contoh Nama : BadruGanz \x1b[1;97m[*]\n\n \x1b[1;97m[?] Masukan Nama :\x1b[1;93m ')
    if ask.strip() == '':
        exit('\n \x1b[1;91m[!] Wajib Di Isi')
    try:
        max = int(raw_input('\x1b[1;97m [?] Limit : \x1b[1;93m'))
    except ValueError:
        exit('\n \x1b[1;91m[!] Wajib Di Isi')

    if max == 0:
        exit('\n \x1b[1;91m[!] Wajib Di Isi')
    url_search = url + '/search/people/?q=' + ask
    statusStop = False
    output = 'dump/' + ask.replace(' ', '_') + ('.json').strip()
    id = []
    print ''
    while True:
        try:
            response = config.httpRequest(url_search, cookie).encode('utf-8')
            html = parser(response, 'html.parser')
            find = html.find_all('a')
            for i in find:
                name = i.find('div')
                if '+' in str(name) or name == None:
                    continue
                else:
                    full_name = str(name.text.encode('utf-8'))
                    if 'profile.php?id=' in str(i):
                        uid = re.findall('\\?id=(.*?)&', str(i))
                    else:
                        uid = re.findall('/(.*?)\\?refid=', str(i))
                    if len(uid) == 1:
                        id.append({'uid': uid[0], 'name': full_name})
                    sys.stdout.write('\r\x1b[1;95m•  \r\x1b[1;95m• \x1b[1;97m%s\x1b[1;95m • \x1b[1;97m%s\x1b[1;95m • \x1b[1;97mSedang Dump ' % (
                     datetime.now().strftime('%H:%M:%S'), len(id)))
                    sys.stdout.flush()
                    if len(id) == max or len(id) > max:
                        statusStop = True
                        break

            if statusStop == False:
                if 'Lihat Hasil Selanjutnya' in str(html):
                    url_search = html.find('a', string='Lihat Hasil Selanjutnya')['href']
                else:
                    break
            else:
                break
        except KeyboardInterrupt:
            print '\n\n \x1b[1;91m[!] Error, Berhenti'
            break

    try:
        for filename in os.listdir('dump'):
            os.remove('dump/' + filename)

    except:
        pass

    print '\n\n\x1b[1;97m [*] Output :\x1b[1;93m ' + output
    save = open(output, 'w')
    save.write(json.dumps(id))
    save.close()
    return
# Awokawokawok Ngerekod:v