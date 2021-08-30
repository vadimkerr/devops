# Best practices

## python best practices

- pin dependency versions (`requirements.txt`, `pipenv`, `poetry`)
- use virtual envs (`virtualenv`, `pipenv`, `poetry`)
- separate dev and prod dependencies (don't make your containers fatter by installing linters and other non-runtime stuff on production environment)
- use formatters and linters (popular combo: `isort`, `black`, `flake8`)
- use git hooks (reduce "fix linting" commits by employing pre-commit hooks. popular option for python community is `pre-commit`)

## unit test best practices

- tests should be simple and easy to comprehend
- tests should be deterministic, meaning that there should be no state differences between runs
- tests should be automated and present in CI pipeline
- tests should not be coupled to implementation details
- measure test coverage and maintain a certain level (e.g. 100%)
