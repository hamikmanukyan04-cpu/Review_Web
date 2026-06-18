# 🤖 AI Sentiment Analysis Web App

This is a simple Machine Learning web application that classifies text as **Positive** or **Negative** using TF-IDF + Logistic Regression.

---

## 🚀 Features

- AI sentiment analysis (Positive / Negative)
- Simple web interface (Flask)
- ML model trained with scikit-learn
- Easy to run locally
- Ready for GitHub deployment

---

## 🧠 Tech Stack

- Python 🐍
- Flask 🌐
- Scikit-learn 🤖
- Pandas 📊
- Joblib 💾
- HTML + CSS 🎨

---

## 📁 Project Structure



├── app.py
├── train.py
├── model.pkl
├── requirements.txt
├── templates/
│ └── index.html
├── static/
│ └── style.css



---

## ⚙️ Installation

### 1. Clone repository
```bash
git clone https://github.com/your-username/sentiment-site.git
cd sentiment-site

```
### 2. Install dependencies
```bash
pip install -r requirements.txt

```
### 3. Train the model
```bash
python train.py

👉 This will create model.pkl

```
### 4. Run the web app
```bash
python app.py

```
### 🌍 Open in browser
```bash
http://127.0.0.1:5000/

```
### 🧪 Example

Input:
```bash
I love this product, it is amazing!

```
Output:
```bash
Positive 😊

```
Input:
```bash
This is the worst experience ever.

```
Output:
```bash
Negative 😡
