# OTEL Collector
docker run -d --name otelcol   -p 4317:4317   -p 4318:4318   -p 8889:8889   -v $(pwd)/otel-collector.yaml:/etc/otel/config.yaml   otel/opentelemetry-collector-contrib   --config /etc/otel/config.yaml

# Tempo
docker run -d --name tempo   -p 3200:3200   -p 4317:4317   -v $(pwd)/tempo.yaml:/etc/tempo.yaml   grafana/tempo   -config.file=/etc/tempo.yaml