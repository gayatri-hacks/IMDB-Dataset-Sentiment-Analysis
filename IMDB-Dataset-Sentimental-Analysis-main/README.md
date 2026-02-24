# 🎬 IMDB Dataset Sentiment Analysis

This project implements sentiment analysis on the IMDB movie reviews dataset using a fine-tuned BERT model. It encompasses data preprocessing, model training, and a Streamlit-based web application for inference.

---

## 🛠️ Tech Stack

* **Programming Language:** Python 3.11
* **Libraries & Frameworks:**

  * [Transformers (Hugging Face)](https://huggingface.co/transformers/) – for BERT model and tokenizer
  * [TensorFlow](https://www.tensorflow.org/) – for model training and evaluation
  * [Streamlit](https://streamlit.io/) – for building the interactive web application
  * [Datasets (Hugging Face)](https://huggingface.co/docs/datasets/) – for loading and processing the IMDB dataset
  * [Matplotlib](https://matplotlib.org/) – for data visualization
  * [Scikit-learn](https://scikit-learn.org/) – for evaluation metrics
  * [Pandas](https://pandas.pydata.org/) – for data manipulation
  * [NumPy](https://numpy.org/) – for numerical computations
* **Development Tools:**

  * [Jupyter Notebook](https://jupyter.org/) – for exploratory data analysis and model training
  * [Virtual Environment (`venv`)](https://docs.python.org/3/library/venv.html) – for managing project dependencies

---

## 📁 Project Structure

```
IMDB-Dataset-Sentimental-Analysis/
├── .venv/                      # Python virtual environment (excluded from version control)
├── app.py                      # Streamlit application for sentiment prediction
├── data/                       # Directory cached files
├── notebooks/
│   ├── EDA.ipynb               # Exploratory Data Analysis notebook
│   └── train_model.ipynb       # Notebook for training the BERT model
├── outputs/                    # Directory for trained models and related outputs
├── requirements.txt            # List of project dependencies
└── README.md                   # Project documentation
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Saber0722/IMDB-Dataset-Sentimental-Analysis.git
cd IMDB-Dataset-Sentimental-Analysis
```

### 2. Create and Activate a Virtual Environment

It's recommended to use a virtual environment to manage dependencies.

```bash
python -m venv .venv
# Activate the virtual environment
# On Windows:
.venv\Scripts\activate
# On Unix or MacOS:
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 📊 Training the Model

* **Notebook:** `notebooks/train_model.ipynb`

  Running this notebook will:

  * Download and cache the IMDB dataset into the `data/` directory.
  * Preprocess the data.
  * Fine-tune a BERT model for sentiment classification.

**Note:** The dataset and tokenizer will be cached in the `data/` folder upon execution.

---

## ⚠️ Hardware Considerations

* The model was trained using a GPU, which significantly reduced training time.
* **If you're using a CPU**, be aware that training will be considerably slower and more resource-intensive.

  * To mitigate this:

    * **Reduce the maximum sequence length** from 128 to 8 or 4.
    * **Decrease the batch size** from 8 to 2 or even 1.

Adjust these parameters in the training notebook to accommodate your hardware capabilities.

---

## 🌐 Running the Streamlit App

The `app.py` file launches a Streamlit web application for sentiment prediction.

To run the app:

```bash
streamlit run app.py
```

**Please Note:**

* The initial loading time may be longer due to the size of the BERT model.
* Ensure that the trained model is available in the `outputs/` directory before running the app.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---
