# CI best practices

- VCS repo should be a single source of truth, don't rely on one-off manual actions
- make release process frictionless to enable engineers to commit and deploy often
- employ `lint` and `test` stages to have consistent and stable builds
- there should be only one way to deploy to production, this process should be clear to everyone in team
- CI pipelines should be fast to enable better feedback loop (engineers can see results and fix problems faster)
