# Installation: pip3 install --upgrade reedsolo

# Initialization
from reedsolo import RSCodec
import random

# Symbol setting
symbols = 4
rsc = RSCodec(symbols)
print("Symbol:", symbols, "bytes")

# Message
message = "helloworld"
message = message.encode()
print("Message[", len(message), "]: ", message, sep='')

# Params
k = len(message)
m = symbols
n = m + k

print("RSC(", n, ", ", k, ") that means,", sep='')
print("> With POS, any ", k, " chunks of ", n, " chunks can be recovered.", sep='')
print("> Without POS, any ", int(k+m/2), " chunks of ", n, " chunks can be recovered.", sep='')

# Encoding # Note that chunking is supported transparently to encode any string length.
encoded = rsc.encode(message)
print("Encoded[", len(encoded), "]: ", encoded, sep='')

# Random spoiling
idxs = list(range(0, len(encoded)))
random.shuffle(idxs)
# Possible pollution
# If erase_pos is not given, less and equal than half of n-symbols polluted can be decoded.
# Otherwise, n-symbols polluted can be decoded.
pollution = random.randint(1, m)
print(pollution, "bytes are polluted.")
idxs = idxs[0:pollution]
for i in idxs: # polluting
    encoded[i] = 0
print("Encoded-Polluted[", len(encoded), "]: ", encoded, sep='')

# Decoding (repairing)
decoded = rsc.decode(encoded, erase_pos=idxs)[0]
print("Decoded[", len(decoded), "]: ", decoded, sep='')

# Verification
assert message == decoded