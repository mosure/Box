This directory contains our database interface as well as extensions of the interface (which are actually used based on configuration)

All of the database configuration is hanldled in `.module` within the DatabaseModule. This is also where the serivices
are binded for dependency injection.

All of the services are defined in `/services`. These control all the interactions with the graph database driver.
