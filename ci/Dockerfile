FROM docker.io/library/python:3.12-slim
WORKDIR /sdk
COPY . .
RUN pip install --no-cache-dir .
CMD ["python", "ci/smoke_test.py"]
