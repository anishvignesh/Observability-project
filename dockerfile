docker run -d --name tempo \
  -p 4317:4317 \
  -p 3200:3200 \
  -v $(pwd)/tempo.yaml:/etc/tempo.yaml \
  -v $(pwd)/tempo-data:/var/tempo \
  grafana/tempo:latest -config.file=/etc/tempo.yaml
