## Setup

If you only want to run the Machine Learning server, you can run the following command:

```bash
docker build machine_learning/ -t ml_server

docker run ml_server
```

Or in the main directory run:
```bash
docker-compose up --build
```