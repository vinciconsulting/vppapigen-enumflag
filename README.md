
# vppapigen-enumflag

vppapigen-enumflag is provided as emitter plugin to extend vppapigen. 

It emits whether an enum looks like an enum or an enumflag, based on any elements with more than one bits set. 


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.
install via pip:
```bash
python3 -m pip install vppapigen-enumflag 
```

## Verification

After installation, you should see the new emitter in the options.
```vppapigen -h
usage: vppapigen [-h] [--includedir INCLUDEDIR] [--outputdir OUTPUTDIR] [--input INPUT] [--output [OUTPUT]] [--debug]
                 [--show-name SHOW_NAME] [--git-revision GIT_REVISION]
                 [{ENUMFLAG,C,CRC,JSON}]
```

## Using
```vppapigen --help

import vppapigen
args.output='ENUMFLAG'
vppapigen.main(args)

```

## Contributing
Pull requests are welcome.



## License
[Apache-2](https://choosealicense.com/licenses/apache-2.0/)
