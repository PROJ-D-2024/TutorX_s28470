TUTOR_X S28470

# Wine Quality Dataset Workflow

This project sets up an **Apache Airflow** DAG for downloading, processing, and uploading the Wine Quality dataset to **Google Sheets**. The workflow includes three main tasks:

1. **Download Data**: Downloads the Wine Quality dataset from Kaggle.
2. **Read Data**: Reads the downloaded dataset (CSV format) into a Pandas DataFrame.
3. **Upload to Google Sheets**: Uploads the dataset to Google Sheets.

## Requirements

### Docker Setup

This project is containerized using **Docker**. It includes the following dependencies:

- **Python 3.9**
- **Apache Airflow 2.2.3**
- **Cython**
- **pandas**
- **gspread**
- **oauth2client**
- **kagglehub**

### Dockerfile

The Dockerfile sets up an environment with the necessary system dependencies and Python libraries.

### Airflow Configuration

- The **Airflow Scheduler** runs the tasks.
- The DAG is set up with the following tasks:
  - **download_data**: Downloads the Wine Quality dataset from Kaggle.
  - **read_data**: Reads the downloaded CSV file and converts it into JSON format.
  - **upload_to_google_sheets**: Uploads the data to Google Sheets.

### Google Sheets Setup

- The project uses **Google Sheets API** for uploading data. Ensure you have the `credentials.json` file with Google Sheets API access.

## Steps to Run

### 1. Build and Run the Docker Container

```bash
docker build -t wine-quality-workflow .
docker run -d -p 8080:8080 wine-quality-workflow
```

# Wine Quality Dataset Workflow

This project sets up an **Apache Airflow** DAG for downloading, processing, and uploading the Wine Quality dataset to **Google Sheets**. The workflow includes three main tasks:

1. **Download Data**: Downloads the Wine Quality dataset from Kaggle.
2. **Read Data**: Reads the downloaded dataset (CSV format) into a Pandas DataFrame.
3. **Upload to Google Sheets**: Uploads the dataset to Google Sheets.

## Requirements

### Docker Setup

This project is containerized using **Docker**. It includes the following dependencies:

- **Python 3.9**
- **Apache Airflow 2.2.3**
- **Cython**
- **pandas**
- **gspread**
- **oauth2client**
- **kagglehub**

### Dockerfile

The Dockerfile sets up an environment with the necessary system dependencies and Python libraries.

### Airflow Configuration

- The **Airflow Scheduler** runs the tasks.
- The DAG is set up with the following tasks:
  - **download_data**: Downloads the Wine Quality dataset from Kaggle.
  - **read_data**: Reads the downloaded CSV file and converts it into JSON format.
  - **upload_to_google_sheets**: Uploads the data to Google Sheets.

### Google Sheets Setup

- The project uses **Google Sheets API** for uploading data. Ensure you have the `credentials.json` file with Google Sheets API access.
