FROM python:3.11-slim

# Create user with UID 1000 as per HF requirements
RUN useradd -m -u 1000 user
USER user
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH \
    APP_PORT=7007

WORKDIR $HOME/app

COPY --chown=user . $HOME/app

RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 7007

# Run uvicorn on fixed port 7007
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7007"]
