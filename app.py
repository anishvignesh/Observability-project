from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
import time

resource = Resource(attributes={"service.name": "python-app"})
trace.set_tracer_provider(TracerProvider(resource=resource))
tracer = trace.get_tracer(__name__)

span_exporter = OTLPSpanExporter(
    endpoint="http://SERVER_C_IP:4317",
    insecure=True
)

trace.get_tracer_provider().add_span_processor(
    BatchSpanProcessor(span_exporter)
)

while True:
    with tracer.start_as_current_span("demo-span"):
        print("Sending trace...")
        time.sleep(5)