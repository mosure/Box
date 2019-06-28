This directory contains our database interface as well as extensions of the interface (which are actually used based on configuration)

We will use `jobs.py` as our example interface for an explaination:

The `Jobs` class that resides in `jobs.py` at this level is our 'interface' that gets dependency injected into our API. This `Jobs` class acts as a switch depending on what type of database has been selected.

The `jobs.py` that resides in the `./sql` folder is an implementation of the outer `jobs.py`.

The registration of the `./sql/jobs.py` happens in `__init__.py`'s `DatabaseModule`.
