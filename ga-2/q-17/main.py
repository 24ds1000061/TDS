from fastapi import FastAPI, Response
app = FastAPI()

@app.get("/")
def read_root():
    content = """
    <html>
    <head><title>24ds1000061@ds.study.iitm.ac.in</title></head>
    <body>24ds1000061@ds.study.iitm.ac.in</body>
    </html>
    """
    return Response(content=content, media_type="text/html", headers={
        "Bypass-Tunnel-Reminder": "true",
        "X-Email": "24ds1000061@ds.study.iitm.ac.in",
        "Access-Control-Expose-Headers": "X-Email"
    })

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8081)
