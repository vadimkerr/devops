# Logging

## screenshots

![](images/grafana.png)
![](images/promtail.png)
![](images/prometheus.png)
![](images/dashboard-loki.png)
![](images/dashboard-prometheus.png)

## best practices

- establish a consistent format for logs
- use some persistent storage to back up your logs (e.g. AWS S3)
- employ log rotation
- don't log sensitive info like tokens, passwords, etc.
