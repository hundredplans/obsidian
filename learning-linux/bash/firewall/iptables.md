- Syntax is **sudo iptables \[option] CHAIN_rule \[-j target]**
- Chains are strings of rules

# Options
- -A -> Appends a rule (string)
- -C -> Finds a rule that matches string
- -D -> Removes specified string
- -F -> Deletes all rules
- -i II -> Specify input interface (lo=localhost)
- -I \[NUM] -> Insert rule at given NUM position
- -j ACTION -> What action to take if a packet matches the rule
	- ACCEPT
	- DROP
	- REJECT
- -L -> List all rules
- -N chain_name -> Create a new chain of specified name
- -m MODULE_NAME -> Use specific module with extra matching or target options
	- state -> Allows to match packets based on connection state
- -p PROTOCOL -> Specify on which packet protocol to act on (tcp/udp)
- -s IP_ADDRESS -> Specify on which IP_ADDRESS to act, use -j ACCEPT to accept the address
- -v -> Display more info with -L
- -x -> Deletes chain

- --dport PORT -> Specify on which packet port to act on, can also use PORT1:PORT2 to accept ports within a specified range

# Similar Commands
- [[iptables-save]]