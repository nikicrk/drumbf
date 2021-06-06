#!usr/bin/python2.7
# coding=utf-8
import os, re, sys, json,time,itertools,datetime
from bs4 import BeautifulSoup as parser
from datetime import datetime

def main(self, cookie, url, config):
    flist = raw_input('\n \x1b[1;97m[?] Url Daftar Teman : \x1b[1;93m')
    try:
        domain = flist.split('//')[1].split('/')[0]
        flist = flist.replace(domain, 'mbasic.facebook.com')
    except IndexError:
        print '\x1b[1;91m [!] Url Tidak Ada'
        os.system('xdg-open https://youtu.be/WON_nU1jhtA ')
        os.system('python2 Dru.py')

    output = re.findall('https:\\/\\/.*?\\/(.*?)\\/friends\\?lst=', flist)
    _output = re.findall('id=(.*?)&refid=', flist)
    if len(output) == 0 and len(_output) == 0:
        print '\x1b[1;91m [!] Url Tidak Ada'
        os.system('xdg-open https://youtu.be/WON_nU1jhtA')
        os.system('python2 Dru.py')
    else:
        if len(output) != 0:
            output = 'dump/' + output[0] + '.json'
        else:
            output = 'dump/' + _output[0] + '.json'
        id = []
        print ''
        while True:
            try:
                response = config.httpRequest(flist, cookie).encode('utf-8')
                html = parser(response, 'html.parser')
                for x in html.find_all(style='vertical-align: middle'):
                    find = x.find('a')
                    if '+' in str(find) or find == None:
                        continue
                    else:
                        full_name = str(find.text.encode('utf-8'))
                        if '/profile.php?id=' in str(find):
                            uid = re.findall('/?id=(.*?)&', find['href'])
                        else:
                            uid = re.findall('/(.*?)\\?fref=', find['href'])
                        if len(uid) == 1:
                            id.append({'uid': uid[0], 'name': full_name})
                        sys.stdout.write('\r\x1b[1;95m•  \r\x1b[1;95m• \x1b[1;97m%s\x1b[1;95m • \x1b[1;97m%s\x1b[1;95m • \x1b[1;97mSedang Dump ' % (
                         datetime.now().strftime('%H:%M:%S'), len(id)))
                        sys.stdout.flush()
                        time.sleep(0.0050)

                if 'Lihat Teman Lain' in str(html):
                    flist = url + html.find('a', string='Lihat Teman Lain')['href']
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