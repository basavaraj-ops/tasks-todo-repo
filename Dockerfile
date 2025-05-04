FROM python:3.12-slim-bookworm

# Set working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY ./requirements.txt /app/
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the rest of the project files
COPY . /app/

# Copy the entrypoint script and ensure it has execute permissions
COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

# Set the entrypoint
ENTRYPOINT ["/docker-entrypoint.sh"]

# Expose port
EXPOSE 80

# Command to run the application
CMD ["uvicorn", "master_server.asgi:application", "--host", "0.0.0.0", "--port", "80", "--workers", "3", "--log-config", "log_config.json", "--timeout-keep-alive", "300", "--lifespan", "off"]
