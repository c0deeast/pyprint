#coding: utf-8


# website settings
username = 'c0deeast'
email = 'c0deeast@foxmail.com'
title = 'c0deeast\'s Blog'
motto = u'小逗比'
disqus_shortname = 'c0deeast'

# themes name
theme = 'default'

# development
debug = True


analytics_code = '''
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-53662402-1', 'auto');
  ga('send', 'pageview');
'''

post_of_page = 3


try:
    from localsettings import connect_str, cookie_secret
except ImportError:
    raise Exception('Please add connect_str and cookie_secret in localsettings.py')


try:
    module = __import__('themes.%s.config' % theme, globals(), locals(), ['*'])
    for k in dir(module):
        locals()[k] = getattr(module, k)
except ImportError:
    pass

