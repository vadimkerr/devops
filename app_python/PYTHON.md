# Python best practices

- pin dependency versions (`requirements.txt`, `pipenv`, `poetry`)
- use virtual envs (`virtualenv`, `pipenv`, `poetry`)
- separate dev and prod dependencies (don't make your containers fatter by installing linters and other non-runtime stuff on production environment)
- use formatters and linters (popular combo: `isort`, `black`, `flake8`)
- use git hooks (reduce "fix linting" commits by employing pre-commit hooks. popular option for python community is `pre-commit`)
