# ansible-heartbeat
Role to create a daemon which sends heartbeat to Riemann server at defined intervals.

NOTE: You need a working riemann server to test this role. Without a riemann server to connect to the heartbeat script will fail after 4 retries.

You can provide the hostname of the riemann server with the variable "riemann_host". By default it is set to localhost.
