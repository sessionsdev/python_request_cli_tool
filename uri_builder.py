from typing import Dict

# Step 1: Complete a Builder class for the Uri class
# Step 2: Add support for query paramters
# Step 3: Add support for URI fragment identifiers (https://en.wikipedia.org/wiki/Fragment_identifier)
# Step 4: Ensure nobody can use the URI constructor, 
#         they should only be able to use the Builder to create a URI

class Uri():
    """
    Uri class
    """

    
    @staticmethod
    def new():
        return UriBuilder()
    
    def __init__(self, scheme: str, host: str, path: str, params: str, fragment: str, valid=None):
        self.scheme = scheme
        self.host = host
        self.path = path
        self.params = params
        self.fragment = fragment
        if valid == None:
            raise ValueError("Must call from constructor from builder method.")
        
        
        
        
    def to_string(self):
        
        
        p = '?'
        if self.params:
            for k, v in self.params.items():
                p = p + (f'{k}={v}&')
            p.join('')

        f = '#'
        if self.fragment:
            for k, v in self.fragment.items():
                if v is not None:
                    f = f + (f'{k}={v}&')
                else:
                    f = f + (f'{k}&')
            f.join('')

        path = ""
        if self.path:
            path = f'{self.path}/'

                
        
        return f'{self.scheme}://{self.host}/{path}{p[:-1]}{f[:-1]}'

    
    
class UriBuilder:
    
    
    def __init__(self, scheme: str=None, host: str=None, path: str="", params = None,fragment = None):
        self.scheme = scheme
        self.host = host
        self.path = path
        self.params = params
        self.fragment = fragment
    
    def with_scheme(self, scheme):
        return UriBuilder(scheme=scheme, host=self.host, path=self.path, params=self.params, fragment=self.fragment)
    
    def with_host(self, host):
        return UriBuilder(scheme=self.scheme, host=host, path=self.path, params=self.params, fragment=self.fragment)
    
    def with_path(self, path):
        return UriBuilder(scheme=self.scheme, host=self.host, path=path, params=self.params, fragment=self.fragment)
    
    def with_param(self, key, value):
        paremeters = dict()
        paremeters[key] = value
        return UriBuilder(scheme=self.scheme, host=self.host, path=self.path, params=paremeters, fragment=self.fragment)

    def with_fragment(self, key, value=None):
        fragment = dict()
        fragment[key] = value
        return UriBuilder(scheme=self.scheme, host=self.host, path=self.path, params=self.params, fragment=fragment)

        
    
    def to_uri(self):
        return Uri(scheme=self.scheme, host=self.host, path=self.path, params=self.params, fragment=self.fragment, valid=1)
    
