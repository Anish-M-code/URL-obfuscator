
# URL Obfuscator 
# Copyright (C) 2019-2022 M.Anish <aneesh25861@gmail.com>
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
                'https://l.wl.co/l?u=',              # Open_redirect Whatsapp Business Account Profile website links. [ source:M.Anish]
                'https://tor2web.onionsearchengine.com/index.php?q=', #Open_redirect in Proxy.[ No warning ][ source: M.Anish]
                'https://proxy.torgateway.com/index.php?q=',  #Open_redirect.[ No warning ][ source: M.Anish ] 
                'https://onionengine.com/url.php?u=', #Open_redirect.[ No warning ][ source: M.Anish ] 
                'http://raspe.id.au/bypass/miniProxy.php?', #Open_redirect in proxy [ No warning ] [ Difficult to detect ]
                'https://www.awin1.com/cread.php?awinmid=6798&awinaffid=673201&ued=', # [ No warning ]
                'https://www.anrdoezrs.net/click-6361382-15020510?url=', # [ No warning ]
                'https://www.digit.in/flipkart/intermediate?url=', # [ Easy to detect ]
                'https://adclick.g.doubleclick.net/pcs/click?xai=AKAOjstFA55hCSrFSTBDNko3225YAz6GkouTQlHjExWXRbT5OPMnSlE8Wh4LAVp-D7jWRr-LcKW0w-HH1g8lCVAK_eU-5azfUXfjqfTiHFOFWV9I8m2ZaGczGlov1iY8kMSnelCX-AHG6VYBmpcZJapT1XbdlOM3B9u9whYqpkxEpFLbkzwDao00-DL8JyS7UIxIApb_JHANRmtKLSuRcM8IWqFaP0cOc8n8jTedmwHc8oAw2MV2tRUaAnN3eaxaESpc8fovDeWslJ0A3duo5g46YzCYxQ8A56RI5MGcQw4TZj6TeWuj6jRjAe7g0X18--IBmztC1sUi6XuHkB1Ew-z_h9bv1XK-s_9L6zeDfQPtMsI3hOqp8T8545VdgCoElxs&sig=Cg0ArKJSzEpZ_YMvCKWCEAE&fbs_aeid=[gw_fbsaeid]&urlfix=1&adurl=', # [ No warning ]
                'https://shop-links.co/link?publisher_slug=future&exclusive=1&u1=tomsguide-in-2620345246174741000&url=', # [ No warning ]
                'https://www.womginx.gq/main/', # Open_redirect in proxy [ No warning ] 
                'https://wassupwomiwi.herokuapp.com/main/', # Open_redirect in proxy [ No warning ] 
                'https://womginx.arph.org/main/', # Open_redirect in proxy [ No warning ] 
                'https://wg.abcya.ga/main/', # Open_redirect in proxy [ No warning ] 
                'https://e.lexiapowerup.ga/main/', # Open_redirect in proxy [ No warning ] 
                'http://seelenotseelie.herokuapp.com/main/', # Open_redirect in proxy [ No warning ] 
                'https://elzxs.herokuapp.com/main/', # Open_redirect in proxy [ No warning ] 
                'https://kavenciwomginx.herokuapp.com/main/', # Open_redirect in proxy [ No warning ] 
                'https://back4app.herokuapp.com/main/', # Open_redirect in proxy [ No warning ] 
                'https://bananalearning.herokuapp.com/main/', # Open_redirect in proxy [ No warning ] 
                'https://meumundomaisdigital.com.br/wp-content/plugins/super-links/application/helpers/super-links-proxy.php?', # Open_redirect in proxy [ No warning ] 
                'http://media.mailadam.com/proxy/index.php?', # Open_redirect in proxy [ No warning ] 
                'http://f2pool.cam/index.php?', # Open_redirect in proxy [ No warning ] 
                'https://www.coinmarketguide.com/index.php?', # Open_redirect in proxy [ No warning ] 
                'https://loja.rarp.com.br/wp-content/plugins/super-links/application/helpers/super-links-proxy.php?', # Open_redirect in proxy [ No warning ] 
                'http://prox.x86.co.uk/index.php?', # Open_redirect in proxy [ No warning ] 
                'https://ersupport.com/plugins/QuickWebProxy/miniProxy.php?', # Open_redirect in proxy [ No warning ] 
                'http://ps-chi.herokuapp.com/index.php?', # Open_redirect in proxy [ No warning ] 
                'http://xlx723.dyndns.org/iproxy/miniProxy.php?', # Open_redirect in proxy [ No warning ] 
                'http://proxy.voracek.net/subdom/proxy/index.php/', # Open_redirect in proxy [ No warning ] 

                
                '\n--- ONION URLs ---\n',

                'http://haystak5njsmn2hqkewecpaxetahtwhsbsa64jom2k22z5afxhnpxfid.onion/redir.php?url=',#Redirect using Haystack DEEP WEB search. [ ONION SERVICE][source:M.Anish]
                'http://zgphrnyp45suenks3jcscwvc5zllyk3vz4izzw67puwlzabw4wvwufid.onion/url.php?u=', #Open_redirect  [ no warning . ]  

                '\n--- Tor Onion URL Redirection [ only works for sites ending with .onion ] ---\n',

                'https://ahmia.fi/search/search/redirect?search_term=cat&redirect_url=', #Redirect in Ahmia Search [ easily detectable]     
                'http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion/search/search/redirect?search_term=cat&redirect_url=' #Redirect Ahmia [ easily detectable]        
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
