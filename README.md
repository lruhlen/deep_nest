# NDict: A Python Module for Nested Dictionaries

## Installation:
```
pip install ndict
```

## Usage
### Create an ndict from a regular dictionary
```
reg_dict = {'key1': 1, 'key2': {'subkey2': 2, 'another key': 3}}
my_ndict = ndict(reg_dict)
print my_ndict['key2', 'another key']
> 3
```

### Create an ndict directly
```
my_ndict = ndict()
my_ndict['key1'] = 1
my_ndict['key2', 'subkey2'] = 2
my_ndict['key2', 'another key'] = 3

print my_ndict
> {'key1': 1, 'key2': {'subkey2': 2, 'another key': 3}}
```

### Update existing entries
```
my_ndict['key2', 'subkey2'] = 'MOOSE'

print my_ndict
> {'key1': 1, 'key2': {'subkey2': 'MOOSE', 'another key': 3}}

my_ndict['key1', 'subkey1'] = 1
print my_ndict
> {'key1': {'subkey1': 1}, 'key2': {'subkey2': 'MOOSE', 'another key': 3}}
```

### Delete entries
```
del my_ndict['key2', 'subkey2', 'another key']
print my_ndict
>  {'key1': {'subkey1': 1}, 'key2': {'subkey2': 'MOOSE'}}
```


