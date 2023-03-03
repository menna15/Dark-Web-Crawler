# Crawler
## Install tor 
sudo apt install tor

## Add briges
- from https://bridges.torproject.org/
- choose obsf4
- Append the bridges to etc/tor/torrc

-- UseBridges 1
-- ClientTransportPlugin obfs4 exec /usr/bin/obfs4proxy
-- Bridge obfs4 "bridge"

# hash password
- run in terminal 'tor --hash-password "pass"

## Uncomment 
- controlport
- socks
- Hashedpassword

## run tor in terminal
- tor


