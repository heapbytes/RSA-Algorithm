# bytes_to_long

## Demonstration of working of bytes_to_long

```py
from Crypto.Util.number import *

#Using library
print(bytes_to_long(b'hello'))

#Manual way
msg = b'hello'
convert = '0x'
for i in msg:
  convert += hex(i)[2:]

fin = int(convert,16)
print(fin)
```

# long_to_bytes

## Demonstration of working of long_to_bytes

```py
from Crypto.Util.number import *

#Using Library
print(long_to_bytes(448378203247))

#Manual way

fin = hex(448378203247)[2:]
print(bytes.fromhex(fin))

```
