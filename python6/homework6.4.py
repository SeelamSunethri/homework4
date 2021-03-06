db = shelve.open('/tmp/somefile','c')
db['bob'] = {'shoesize':42, 'gender':'m'}
db['bob']
{'shoesize': 42, 'gender': 'm'}
db['bob']['gender'] = 'u'
db['bob']
{'shoesize': 42, 'gender': 'm'}
db['bob'] = {'shoesize': 42, 'gender': 'u'}
db['bob']
{'shoesize': 42, 'gender': 'u'}