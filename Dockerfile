FROM python:3.12-slim

WORKDIR /app

COPY *.py *.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

CMD ["sh", "-c", "radon cc ./ -s && radon mi ./ && xenon --max-absolute B ./"]