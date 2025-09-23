from prometheus_client import start_http_server, Counter, Gauge
import psutil
import time, random

# App-level metrics
error_count = Counter('log_errors_total', 'Total number of error logs')
request_latency = Gauge('request_latency_seconds', 'Simulated request latency')

# System-level metrics
bytes_sent = Counter('system_bytes_sent_total', 'Total bytes sent over all interfaces')
bytes_recv = Counter('system_bytes_received_total', 'Total bytes received over all interfaces')
process_count = Gauge('system_process_count', 'Number of running processes')

def collect_system_metrics():
    net_io = psutil.net_io_counters()
    bytes_sent.inc(net_io.bytes_sent - bytes_sent._value.get())
    bytes_recv.inc(net_io.bytes_recv - bytes_recv._value.get())
    process_count.set(len(psutil.pids()))

def simulate_logs():
    while True:
        # App-level simulation
        latency = random.uniform(0.1, 1.5)
        request_latency.set(latency)
        if latency > 1.0:
            error_count.inc()

        # System-level metrics
        collect_system_metrics()

        time.sleep(2)

if __name__ == "__main__":
    start_http_server(8087)
    print("[INFO] Exporter running on http://localhost:8000/metrics")
    simulate_logs()

