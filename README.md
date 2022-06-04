# EDHOC-C test application

How to run:

- create two virtual interfaces: `sudo ${RIOTBASE}/dist/tools/tapsetup/tapsetup -c 2`
- Compile and run two nodes:
```
PORT=tap0 make all term
PORT=tap1 make all term
```
- Choose one to be the receiver and run: `ifconfig`
- At the initiator, kick off the handshake: `init handshake fe80::98ee:a4ff:fe31:38fe`

# Snippets

C hex to CBOR:
```
chex = "0xa1, 0x04, 0x41, 0x23"
cbor2.loads(bytes([int(e, 16) for e in chex.split(", ")]))
```

CBOR to C hex:
```
# bob
ccbor = {4: b"\xad\x9eF\xf5@sH\xef\xb0A\xd5\x9e\x02\xf8,."} # only the value part, converted from b58 to bytes
ccbor = b"\xad\x9eF\xf5@sH\xef\xb0A\xd5\x9e\x02\xf8,."

# lamp
ccbor = {4: b"\xed\x84\x89\xcbt\x90F\x9e\x82'\xbb\xfc\xa8\xde\x0c\xcc"}
ccbor = b"\xed\x84\x89\xcbt\x90F\x9e\x82'\xbb\xfc\xa8\xde\x0c\xcc"

", ".join([f"{hex(e)}" for e in cbor2.dumps(ccbor)])
```

