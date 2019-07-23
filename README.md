# properlist
![PyPI](https://img.shields.io/pypi/v/properlist.svg?color=blue)
![License](https://img.shields.io/pypi/l/properlist.svg)

Proper lists for Python
## What

Python lists that start at 1 instead of 0

## But why

Because it can be done

## Installation

```
pip install properlist
```

## Examples

```
from properlist import ProperList

proper_list = ProperList()

proper_list.append(5)
proper_list.append(2)

print(proper_list[1]) # returns 5
print(proper_list[2]) # returns 2
```

## Known Bugs

- [ ] Doesn't support slicing

## License

I know nobody asked for this but GPLv3 so go wild
