# AutoMLatically

This project is concerned with the implementation of a Auto Machine Learning (AutoML) framework. 
The software has a user-facing frontent (React Website) and a ML performing backend (Flask API server).

The ML framework is focussed on **supervised learning** algorithms. Hence, the provided dataset must have a column with labels/target variables.

---
### 1. Software requirements
Frontend UI displays:
- A selection mechanism for ML models that will be trained afterwards
- Option to upload a dataset in CSV format
- selection mechanism for the dataset's label column
- Performance metrics of trained ML models
- Buttons to download trained models
- The components visualized in the [docs folder](./docs/)

Backend that provides the following:
- API to process the following frontend requests: 
    - Receive uploaded dataset 
    - Receive the dataset's label column
    - Receive the ML model selection 
    - Request to initiate model training
    - Request to download specific trained Models
- The API sends the following requests back to the frontend:
    - The requested Model data
    - The performance measures of the ML models
- Logic to preprocess the dataset
- Logic to create and train selected ML models
- Logic to calculate performance measures
- Logic to tune the hyperparameters of the models
- Logic to store trained models, so that they can be send to the frontend if requested
---

### 2. Setup

<br>

#### 2.1 Prerequisits
You need Docker installed on your local machine. You can follow [these](https://docs.docker.com/engine/install/) instructions to install it. Make sure you have docker-compose installed as well. If you did install Docker Desktop, you already have it enabled. Otherwise you can follow [these](https://docs.docker.com/compose/install/) instructions. 

<br>

#### 2.2 Build and Start
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

---
### 3. Cooperation

The project is organized with a Trello Kanban Board, which is available [here](https://trello.com/b/lVgtr38t/automlatically).

The members of project team are:
- Alina Buss
- Canberk Alkan
- Dominic Viola
- Phillip Lange
