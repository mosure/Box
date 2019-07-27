# Box

# Setup
Download and install neo4j desktop (https://neo4j.com/download/).

Create a new graph with the password `local`

Start the database

Run `python setup.py develop` to link your local package to source (`python setup.py install` if you are only running the application).

To start the Flask server, run `flask run`.

To view the active routes, run `flask routes`.

# Models

## What is a Part?

Think of a part as something that can be held (a piece of metal or plastic). Operations done onto a part may include CNC, paint, etc.

## What is an Operation?

An operation (in our manufacturing context), is any binary-state work done to a part. A part is either sanded or it isn't, we are not tracking partially completed operations on a single part. However, if the sanding operation could be further broken down into 'sub-operations' (such as sanding with different grit), our system would support this as a series of operations. Operations are never done in parallel on a single part (you can't sand the part and paint it at the same time, and if you 'can' then it should be encapsulated by a single operation).

## What is a Job?

In its most basic form, a job is a single operation done onto a part. A job is what we are actually tracking through a manufacturing facility. A job may have hundreds of operations, but they must all be done onto the same part. Operations done onto a part are represented in chronological order via a list.

### What about more complex parts?

Singular jobs capture the intent of a part. Given a source material and a list of operations, we can finish a job. However, this simple model does not support the notion of assembly in a manufacturing facility. A job can capture the intent of a part up until it is assembled into a larger assembly. Operations can be performed on that larger job assembly, however, they must only act on the entire assembly.

Here we run into the first unsolved model problem. What if we want to disassemble an assembly? Most of the time, it would make sense not to disassemble something that has been assembled, however, there are cases such as testing/quality assurance, and packaging/shipping where a large assembly must be disassembled, then operations done onto those subassemblies after the entire assembly has been built. We want to build a system that is as flexible as possible and supports this type of action.

#### Possible solution(s):

* Link Jobs together in a chronological graph instead of an assembly tree

### Batching

Batching of jobs is required to gain efficiency in many areas of manufacturing. For example, sheet metal parts rarely use an entire sheet and can be nested. It can also be thought of (in terms of our modeling) as the intersection of two job graphs. This intersection can happen at any point in time/hiearchy, though for the sheet metal example above, the intersection takes place at the 'beginning' (sheet of material (batched here) -> sheet metal parts).


# What is the purpose?

In addition to checkoff capabilities, the system tracks all operations to a physical station level granularity. For example, consider querying for a parts physical location at any point in time (including the future).

Using the checkoff data, over time, the system is able to generate useful statistics regarding operations and their efficiencies together.

Generate schedules and flow graphs given a pool of jobs (this is not easy, especially when trying to generate the optimal schedule).
