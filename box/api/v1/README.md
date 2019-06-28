
# API

## v1

This folder contains our routes.

`domain.com/api/v1/...`

`/jobs`
`/jobs/:jid`
`/jobs/:jid/operations`
`/jobs/:jid/operations/:oid`

Note: `/operations` returns all defined operations while `/jobs/:jid/operations` returns operations associated with a job
`/operations`
`/operations/:oid`

We will call job templates blueprints
`/blueprints`
`/blueprints/:bid`

The following need to be refined
`/webhooks`
`/webhooks/:wid`

# Dependency Injection

Use `from injector import inject` and `@inject(<param>=<DatabaseService>)` to inject a service from the database into a view.
