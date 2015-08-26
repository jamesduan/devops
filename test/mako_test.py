from mako.template import Template

t = Template(filename = 'ttt.conf')

print t.render(ip = '10.0.0.111')

