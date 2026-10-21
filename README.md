# E-Commerce Product Content Generator

## 1. Project Overview
This project implements an academic prototype for generating e-commerce product content from structured product information.

The application can generate:
- Product title
- Product description
- Key selling points / bullet points
- SEO keywords
- Marketing tagline

Two modes are provided:
1. **Demo / Template Mode** – works without an API key.
2. **Gemini AI Mode** – uses Google's Gemini API for Generative AI content.

## 2. Technology Used
- Python
- Jupyter Notebook
- Streamlit
- Google Gemini API (optional AI mode)
- google-genai SDK

## 3. Files in This Submission
- `E_Commerce_Product_Content_Generator.ipynb` – Jupyter Notebook implementation and explanation.
- `app.py` – Streamlit web application.
- `requirements.txt` – required Python packages.
- `README.md` – setup, execution and documentation steps.

## 4. System Requirements
- Python 3.9 or newer
- Internet connection for installing packages and for Gemini AI mode
- A modern web browser
- Gemini API key only if Gemini AI Mode is used

## 5. Installation Steps

### Step 1: Open the project folder
Open a terminal / Command Prompt in the folder containing these files.

### Step 2: Create a virtual environment (recommended)
Windows:
```bash
python -m venv .venv
.venv\Scripts\activate
```

macOS/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Step 3: Install requirements
```bash
pip install -r requirements.txt
```

## 6. Run the Jupyter Notebook

Install Jupyter if it is not already installed:
```bash
pip install notebook
```

Start Jupyter:
```bash
jupyter notebook
```

Open:
`E_Commerce_Product_Content_Generator.ipynb`

Run the cells from top to bottom.

## 7. Run the Streamlit Web Application

From the project folder:
```bash
streamlit run app.py
```

Streamlit will display a local address, normally:
`http://localhost:8501`

Open that address in a browser.

## 8. Using Demo / Template Mode
1. Keep `Demo / Template Mode` selected.
2. Enter product name, category, brand and price.
3. Enter the product features, one per line.
4. Enter the target audience.
5. Select tone and description length.
6. Click **Generate Product Content**.
7. The application displays the generated listing content.

This mode does not require an API key.

## 9. Using Gemini AI Mode

### Step 1: Obtain a Gemini API key
Create a Gemini API key using Google's AI developer platform.

### Step 2: Set the API key

Windows Command Prompt:
```bash
set GEMINI_API_KEY=YOUR_API_KEY
```

Windows PowerShell:
```powershell
$env:GEMINI_API_KEY="YOUR_API_KEY"
```

macOS/Linux:
```bash
export GEMINI_API_KEY="YOUR_API_KEY"
```

### Step 3: Start the application
```bash
streamlit run app.py
```

Select `Gemini AI Mode` in the sidebar and generate the content.

**Do not put the API key directly inside `app.py`, the notebook, or a public GitHub repository.**

## 10. Major Workflow
Product Information
        ↓
Input Validation
        ↓
Content Generation
        ↓
Title + Description + Bullets + SEO Keywords + Tagline
        ↓
Human Validation
        ↓
E-Commerce Listing

## 11. GenAI Prompting Approach
The Gemini mode uses a structured prompt containing:
- Product name
- Category
- Brand
- Price
- Target audience
- Product features
- Desired tone
- Desired description length

The prompt explicitly instructs the model to use only supplied product facts and not invent specifications, certifications, discounts, ratings, warranty terms or other unsupported claims.

## 12. Limitations
- Generated text can still require human review.
- Gemini AI mode requires an API key and internet access.
- API availability and model names can change.
- Product information must be accurate at the input stage.
- Price and promotional information should be verified before publishing.

## 13. Expected Output
For a sample wireless headphone product, the system produces:
- A concise product title
- A marketing-oriented product description
- Feature bullet points
- Relevant SEO keywords
- A short tagline

## 14. Conclusion
The project demonstrates a practical Generative AI workflow for automating e-commerce product content creation. It reduces repetitive writing work while maintaining a structured input-output process. The system can be extended with product databases, image generation, multilingual content, content quality scoring, and an administrator approval workflow.
