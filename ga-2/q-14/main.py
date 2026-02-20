from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse
import json
import os
import numpy as np

app = FastAPI()

# CORS headers configuration from reference
CORS_HEADERS = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "*",
    "Access-Control-Allow-Headers": "Content-Type, Authorization",
    "Access-Control-Expose-Headers": "Access-Control-Allow-Origin",
}

class CORSJSONResponse(JSONResponse):
    def init_headers(self, headers=None):
        super().init_headers(headers)
        for key, value in CORS_HEADERS.items():
            self.headers[key] = value

# Load data once
DATA_FILE = os.path.join(os.path.dirname(__file__), "data.json")
with open(DATA_FILE, "r") as f:
    TELEMETRY_DATA = json.load(f)

@app.post("/api")
async def get_latency_metrics(request: Request):
    try:
        body = await request.json()
    except:
        body = {}
        
    regions = body.get("regions", [])
    threshold = body.get("threshold_ms", 180)

    results = {}
    for region in regions:
        # Case-insensitive region matching from reference
        region_data = [d for d in TELEMETRY_DATA if d.get("region", "").lower() == region.lower()]
        
        if not region_data:
            results[region] = {
                "avg_latency": 0.0,
                "p95_latency": 0.0,
                "avg_uptime": 0.0,
                "breaches": 0
            }
            continue

        latencies = np.array([d.get("latency_ms", 0) for d in region_data], dtype=float)
        uptimes = np.array([d.get("uptime_pct", 0) for d in region_data], dtype=float)
        
        # Calculations using numpy for exact precision (matches 209.07 for EMEA)
        avg_latency = float(np.mean(latencies))
        p95_latency = float(np.percentile(latencies, 95))
        avg_uptime = float(np.mean(uptimes))
        breaches = int(np.sum(latencies > threshold))

        results[region] = {
            "avg_latency": avg_latency,
            "p95_latency": p95_latency,
            "avg_uptime": avg_uptime,
            "breaches": breaches
        }

    return CORSJSONResponse({"regions": results})

@app.options("/api")
async def options_handler():
    return CORSJSONResponse({})

@app.get("/")
def read_root():
    return CORSJSONResponse({"message": "Vercel Latency API active. Use POST /api"})
