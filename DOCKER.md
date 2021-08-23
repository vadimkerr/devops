# Docker best practices

- pin package versions
- install only needed packages to minimize image sizes
- use linters for Dockerfile (popular option: `hadolint`)
- order layers properly so the build cache is maximized (e.g. first initialize the runtime since it doesn't change much, then `COPY` the code itself)
- reduce number of layers by reducing the number of `RUN`, `COPY`, `ADD` instructions in Dockerfile
