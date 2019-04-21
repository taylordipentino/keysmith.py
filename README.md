
# Keysmith.py
Keysmith.py is a small Python script to generate a random password of a given length. 

### Usage

Show help dialog: 
```sh
$ python3 keysmith.py -h
 
  Basic Usage: 
      keysmith <action> [options]

  Available Actions: 
      -h  -  Show help dialog
      -g  -  Generate passphrase

  Available Options: 
      keysmith -g [length]
      length  -  Character length of the generated password. Default is 16
```

Generate a random password, default length (16 characters): 
```sh
$ python3 keysmith.py -g
```

Generate a random password, specified length: 
```sh
$ python3 keysmith.py -g 32
```

Created by [Taylor DiPentino](https://github.com/taylordipentino).

