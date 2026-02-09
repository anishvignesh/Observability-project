Centralized Observability Platform


        Server A (App Server)
      Python Application
              |
      OTEL SDK / Agent
              |
        (OTLP 4317/4318)
              |
              v
        Server C (OTEL Collector)
   Centralized Telemetry Gateway
              |
   -------------------------------
   |             |             |
Prometheus     Tempo        (Logs)
 Metrics       Traces
              |
              v
        Server B (Monitoring)
      Grafana Dashboards


Centralized Observability Platform – Server Details
Server A – Application Server
Role: Application & Telemetry Source
Purpose: Generates metrics and traces
Components:
•	Python Application
•	OpenTelemetry SDK / Agent
•	Linux (systemd services)
Ports Used:
•	OTLP gRPC → 4317
•	OTLP HTTP → 4318
Responsibilities:
•	Runs business application
•	Collects application metrics & traces
•	Sends telemetry to Central OTEL Collector
________________________________________
Server B – Monitoring Server
 
 
 

Role: Visualization & Analysis
Purpose: Observe system behavior
Components:
•	Grafana
•	Prometheus
•	(Optional) Node Exporter
Ports Used:
•	Grafana → 3000
•	Prometheus → 9090
Responsibilities:
•	Stores metrics (Prometheus)
•	Displays dashboards (Grafana)
•	Engineers access this server for monitoring
________________________________________
Server C – Observability Gateway
Role: Central Telemetry Router
Purpose: Core of the platform
Components:
•	OpenTelemetry Collector
•	Tempo (Trace storage)
•	Docker containers
Ports Used:
•	OTLP gRPC → 4317
•	OTLP HTTP → 4318
•	Prometheus Export → 8889
•	Tempo → 3200
Responsibilities:
•	Receives telemetry from all app servers
•	Processes & batches data
•	Exports:
o	Metrics → Prometheus
o	Traces → Tempo


•	This is your entire system in 4 files
Component	File
App	app.py
OTEL	otel-collector.yaml
Tempo	tempo.yaml
Prometheus	prometheus.yml

