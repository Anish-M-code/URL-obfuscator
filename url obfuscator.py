
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
                'http://l.wl.co/l?u=',              # Open_redirect Whatsapp Business Account Profile website links. [ source:M.Anish]
                'https://proxy-02.onionsearchengine.com/index.php?q=', #Open_redirect in Proxy.[ No warning ][ source: M.Anish]
                'https://proxy-02.onionsearchengine.com/url.php?u=',  #Open_redirect.[ No warning ][ source: M.Anish ] 
                'https://r.duckduckgo.com/l/?kh=-1&uddg=', #Open_redirect.[ No warning ][ source: M.Anish ]
                'https://r.duckduckgo.com/y.js?u3=', #Open_redirect.[ No warning ][ source: M.Anish ]
                'http://r.3g2upl4pq6kufc4m.onion/y.js?u3=', #Open_redirect.[ No warning ][ source: M.Anish ] 
                'http://r.3g2upl4pq6kufc4m.onion/l/?kh=-1&uddg=' #Open_redirect.[ No warning ][ source: M.Anish ]               
                ]

#Function to write obfuscated URLs to url_obfuscated.txt file.
def file_w(content):
  with open('url_obfuscated.txt','w') as f:
    f.write(content)
    
#Function to obfuscate url using http basic auth.
def http_basic_auth(url):
    a = ""
    custom_url=[
                 'http://competitions_for_college_students@',
                 'http://ai_research_for_college_students@',
                 'http://free_certification_courses@',
                ]
    for i in custom_url:
        if url.startswith('https://'):
            a += i+url.strip('https://')+'\n'
        elif url.startswith('http://'):
            a += i+url.strip('http://')+'\n'
    return a

                     
def main():
    print("URL-obfuscator".center(50, "_"))
    data = """
URL : https://github.com/gowtham758550/URL-obfuscator.

Obfuscated URL's
"""
    url = input("Enter url : ")
    if not(url.startswith("https://") or url.startswith("http://")):
        url = "http://" + url		
    for i in open_redirect:
    	data += i 
    	data += url 
    	data += "\n"
    file_w(data + http_basic_auth(url))
    print("Check obfuscated urls in url_obfuscated.txt")
	  	

if __name__ == "__main__":
	main()
