# Prometheus Playground

1. Tape some scrapes in a YAML file:

```yaml
scrapes:
  - status_code: '200'
    data: |
      foo{color="red",size="small"} 4
      foo{color="green",size="small"} 8
      bar{color="green",size="xlarge"} 2
      bar{color="blue",size="large"} 7

  - status_code: '500'
    data: 'Unexpected Error'

  - status_code: '200'
    data: |
      foo{color="blue",size="small"} 16
      foo{color="red",size="large"} 5
      bar{color="red",size="small"} 5
```

2. Run a fake service and a Prometheus instance:

```bash
docker-compose -f scenario-01/docker-compose.yaml up
```

3. Wait until all scrapes are consumed and explore the data:

```
open http://localhost:55055/
```

Read more about the playground <a href="https://iximiuz.com/en/posts/prometheus-learning-promql/">here</a>.

