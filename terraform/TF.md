# Terraform best practices

- use shared state location so there's no ambiguity which state is the "right" one
- use terraform modules to abstract complexity and increase configuration reuse
- employ terraform on CI/CD to provision services your project depends on, that way everyone in team can track resource configuration checked in to VCS
- use `terraform fmt` and `terraform validate` to keep your configuration files clean and consistent
