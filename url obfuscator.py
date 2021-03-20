
# URL Obfuscator 
# Copyright (C) 2019-2020 M.Anish <aneesh25861@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
url=''

#List of publicly discovered open_redirects.
open_redirect=[ '--- URLS with Redirection Notice ---\n',

                'https://www.google.com/url?q=',  # Redirect using Google .[  Google Redirect Notice. ] [ source: Google ]
                'https://google.com/url?q='     , # Variant of above redirect. [ Warning prsent ] [ source: M.Anish ]
                'https://facebook.com/l.php?u=',  # Facebook Open Redirect       [ source : Google ]

                '\n--- URLS with No Redirection Warnings ---\n',

                'https://via.hypothes.is/' ,      # Annotation service.     [ No warning ] [ source : Google ]
                'http://vk.com/away.php?to=',     # Open Redirect in Russian Social Media vk.com [ No warning! ]
                'https://googleweblight.com/i?u=' ,# Redirect using Googleweblight [ No warning ]  [ source: Google ]
                'https://duckduckgo.com/y.js?u3=' , # Redirect using duckduckgo.  [ No Warning ]    [ source: Virustotal ]
                'https://duckduckgo.com/l/?kh=-1&uddg=', # Redirect using duckduckgo.  [ No Warning ] [ source: M.Anish ]
                'https://ahmia.fi/search/search/redirect?search_term=cat&redirect_url=' ,# Redirect in Ahmia DEEP WEB search engine.
                                                                                        #[ Easily detectable ][ source:M.Anish]
                'http://l.wl.co/l?u=',              # Open_redirect Whatsapp Business Account Profile website links. [ source:M.Anish]
                'https://proxy-02.onionsearchengine.com/index.php?q=', #Open_redirect in Proxy.[ No warning ][ source: M.Anish]
                'https://proxy-02.onionsearchengine.com/url.php?u=',  #Open_redirect.[ No warning ][ source: M.Anish ] 
                'https://r.duckduckgo.com/l/?kh=-1&uddg=', #Open_redirect.[ No warning ][ source: M.Anish ]
                'https://r.duckduckgo.com/y.js?u3=', #Open_redirect.[ No warning ][ source: M.Anish ]
                'http://raspe.id.au/bypass/miniProxy.php?', #Open_redirect in proxy [ No warning ] [ Difficult to detect ]

                '\n--- ONION URLs ---\n',

                'http://r.3g2upl4pq6kufc4m.onion/y.js?u3=', #Open_redirect.[ No warning ][ source: M.Anish ] 
                'https://3g2upl4pq6kufc4m.onion/y.js?u3=', # Redirect duckduckgo.[ onion service][No warning][ source:M.Anish]
                'https://3g2upl4pq6kufc4m.onion/l/?kh=-1&uddg=',# Redirect duckduckgo.[ onion service][No warning][ source:M.Anish]
                'http://msydqstlz2kzerdg.onion/search/search/redirect?search_term=cat&redirect_url=',# Redirect in Ahmia DEEP WEB search engine.
                                                                                                      #[ Easily detectable ][ source:M.Anish]
                'http://haystakvxad7wbk5.onion/redir.php?url=',#Redirect using Haystack DEEP WEB search. [ ONION SERVICE][source:M.Anish]
                'http://r.3g2upl4pq6kufc4m.onion/l/?kh=-1&uddg=', #Open_redirect.[ No warning ][ source: M.Anish ]
                'http://onionf4j3fwqpeo5.onion/url.php?u=' #Open_redirect  [ no warning . ]                
                ]

#Function to get URL from user which will be obfuscated by the program.                
def get_url():
  print('\n Enter url: ',end='') 
  global url
  tmp=input()
  if tmp.startswith('http://') or tmp.startswith('https://'):
     url=tmp
  else:
     url='http://'+tmp

get_url()

#Function to write obfuscated URLs to url_obfuscated.txt file.
def file_w():
  with open('url_obfuscated.txt','w') as f:
     for i in open_redirect:
        if '---' in i:
           f.write(i)
        else:
           f.write('{}{}\n'.format(i,url))
        
file_w()

#Function to obfuscate url using http basic auth.
def http_basic_auth():
    custom_url=[
                 'https://accounts.google.com+signin=secure+v2+identifier=passive@',
                 'https://facebook.com+login=secure+settings=private@',
                 'https://instagram.com+accounts=login+settings=private@',
                 'https://linkedin.com+accounts=securelogin+settings=private@',
                 'https://github.com+login=secure+settings=private@'
                ]            
    with open('url_obfuscated.txt','a+')as f:
        f.write('\n--- Custom HTTP BASIC AUTH URLS [ Don\'t work in Firefox ] ---\n')
        for i in custom_url:
            if url.startswith('https://'):
               f.write(i+url[8:]+'\n') 
            elif url.startswith('http://'):
               f.write(i+url[7:]+'\n')

http_basic_auth()            
x=input( '\n {}/url_obfuscated.txt Generated!!!\n\nPress to continue...'.format(os.getcwd()))
