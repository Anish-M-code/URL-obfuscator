
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

url=''

#List of publicly discovered open_redirects.
open_redirect=[ 
                'https://www.google.com/url?q=',  # Redirect using Google .[  Google Redirect Notice. ] [ source: Google ]
                'https://via.hypothes.is/' ,      # Annotation service.     [ No warning ] [ source : Google ]
                'https://facebook.com/l.php?u=',  # Facebook Open Redirect       [ source : Google ]
                'http://vk.com/away.php?to=',     # Open Redirect in Russian Social Media vk.com [ No warning! ]
                'https://google.com/url?q='     , # Variant of above redirect. [ Warning prsent ] [ source: M.Anish ]
                'https://googleweblight.com/i?u=' ,# Redirect using Googleweblight [ No warning ]  [ source: Google ]
                'http://google.com/gwt/x?wsc=eb&u=', # Redirect using Googleweblight [ No warning ]  [ source: Virustotal ]
                'https://duckduckgo.com/y.js?u3=' , # Redirect using duckduckgo.  [ No Warning ]    [ source: Virustotal ]
                'https://duckduckgo.com/l/?kh=-1&uddg=', # Redirect using duckduckgo.  [ No Warning ] [ source: M.Anish ]
                'https://3g2upl4pq6kufc4m.onion/y.js?u3=', # Redirect duckduckgo.[ onion service][No warning][ source:M.Anish]
                'https://3g2upl4pq6kufc4m.onion/l/?kh=-1&uddg=',# Redirect duckduckgo.[ onion service][No warning][ source:M.Anish]
                'https://ahmia.fi/search/search/redirect?search_term=cat&redirect_url=' ,# Redirect in Ahmia DEEP WEB search engine.
                                                                                        #[ Easily detectable ][ source:M.Anish]
                'http://msydqstlz2kzerdg.onion/search/search/redirect?search_term=cat&redirect_url=',# Redirect in Ahmia DEEP WEB search engine.
                                                                                                      #[ Easily detectable ][ source:M.Anish]
                'http://haystakvxad7wbk5.onion/redir.php?url=',#Redirect using Haystack DEEP WEB search. [ ONION SERVICE][source:M.Anish]
                'http://l.wl.co/l?u='              # Open_redirect Whatsapp Business Account Profile website links. [ source:M.Anish]             
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
        f.write(i+url+'\n')
        
file_w()

#Function to obfuscate url using http basic auth.
def http_basic_auth():
    custom_url=[
                 'http://google_competitions_for_college_students@',
                 'http://facebook_led_ai_research_for_indian_college_students@',
                 'http://learn_microsoft_free_certifications@',
                ]            
    with open('url_obfuscated.txt','a+')as f:
        for i in custom_url:
            if url.startswith('https://'):
               f.write(i+url.strip('https://')+'\n') 
            elif url.startswith('http://'):
               f.write(i+url.strip('http://')+'\n')

http_basic_auth()            
x=input('Press to continue...')
