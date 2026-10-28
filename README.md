# Network Intrusion Detection Study

**Python · Streamlit · scikit-learn · Cisco Packet Tracer**

An educational network traffic classification project developed for a Computer Networks course. It uses a **Random Forest** classifier trained on synthetic traffic records and provides a **Streamlit** interface to inspect CSV exports from Cisco Packet Tracer.

> **Project scope:** This is a classroom prototype, **not** a production-ready intrusion detection system. Classification results on synthetic data must not be interpreted as real-world detection accuracy.

## Features

- Generates a synthetic dataset with normal and attack-labeled traffic examples.
- Trains and evaluates a Random Forest model using `scikit-learn`.
- Accepts compatible Packet Tracer CSV exports through a Streamlit interface.
- Displays packet counts, predicted suspicious packet counts, and row-level classifications.

## Tech Stack

| Component | Technology |
| --- | --- |
| Language | Python |
| Data processing | pandas |
| Machine learning | scikit-learn (Random Forest) |
| Interface | Streamlit |
| Network simulation | Cisco Packet Tracer |

## Repository Structure

```text
Bilgisayar_Ağlari_Proje_AI/
├── app.py                      # Streamlit interface
├── data/
│   ├── generator.py            # Synthetic dataset generator
│   └── synthetic_network_traffic.csv
├── trainer/
│   └── train.py                # Model training and evaluation
├── pt_analysis/
│   └── analyzer.py             # Packet Tracer CSV preprocessing and inference
├── models/
│   └── ids_model.pkl           # Serialized trained model
├── proje.pkt                   # Cisco Packet Tracer project
└── rapor.docx                  # Project report
```

## Run Locally

Requires Python 3 and a compatible Python environment.

1. Clone the repository and enter the project directory:

   ```bash
   git clone https://github.com/emirpeker/AI_Destekli_Saldiri_Sistemi.git
   cd AI_Destekli_Saldiri_Sistemi/Bilgisayar_Ağlari_Proje_AI
   ```

2. Install dependencies (preferably inside a virtual environment):

   ```bash
   python -m pip install pandas scikit-learn streamlit
   ```

3. Optionally regenerate the synthetic dataset and retrain the model:

   ```bash
   python data/generator.py
   python trainer/train.py
   ```

   The repository also includes a pre-trained `.pkl` model. Only load model files from sources you trust.

4. Launch the UI:

   ```bash
   python -m streamlit run app.py
   ```

5. Upload a compatible Packet Tracer CSV file. The analysis code expects at least the columns **`Time`**, **`Type`**, and **`Size`**.

## Model Overview

The synthetic training dataset contains four input features:

- **`protocol`** — numeric encoding of TCP, UDP, or ICMP
- **`dst_port`** — destination port
- **`pkt_size`** — packet size
- **`interval`** — time between consecutive packets

The target label is **`0` (normal)** or **`1` (attack)**. Training uses an 80/20 train/test split and a Random Forest with 100 trees and maximum depth 10.

## Known Limitations

- Training examples are **synthetically generated**; the model has not been validated against an independently collected real-traffic dataset.
- The current inference code **hardcodes destination port to `80`**, regardless of the actual packet. This may reduce the validity of predictions, particularly for port scanning.
- CSV ingestion depends on Packet Tracer's export format and does not include robust schema validation.
- The current app writes uploaded CSV data to a temporary filename in the project directory; it is designed for local demonstration, not a multi-user deployment.
- Results represent **per-row classification**, not a comprehensive traffic-based intrusion detection workflow.

## Next Improvements

- Extract actual destination ports during preprocessing and validate input schemas.
- Evaluate on independently sourced, labeled network traffic.
- Add automated tests for preprocessing, feature mapping, and invalid CSV inputs.
- Replace row-by-row prediction with batched model inference for larger files.

---

*Academic project — Computer Networks*
