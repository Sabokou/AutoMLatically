# AutoMLatically

### 1. Setup

To build and run all containers, run this in the main directory of this repo:

```bash
docker-compose up --build
```

To build individual services run this in the main directory:

```bash
docker-compose build <service-name>
```

Replace <service-name> with one of the following:
- frontend
- middleware
- backend