# 🍽️ AI-Powered Calorie Counter Using Gemini  

## 📌 Project Overview  
This project is a **Generative AI-based calorie counter** that uses **Google's Gemini API** to analyze images of food items and **predict the calorie count** for each item. The application is built using **Streamlit** and integrates **Gemini Pro Vision** to provide real-time calorie estimation.

## 🎯 Key Features  
✅ **Upload an image of a food item** and get an instant calorie estimate.  
✅ **Generates a detailed breakdown** of calories for each item in the image.  
✅ **Uses Gemini Pro Vision API** for AI-powered food recognition.  
✅ **User-friendly web interface built with Streamlit.**  

---

## 📊 Technologies Used  
- **Python** (Backend)  
- **Streamlit** (Web UI)  
- **Google Gemini Pro Vision API** (AI Image Analysis)  
- **PIL (Pillow)** (Image Processing)  
- **Dotenv** (Environment Variable Management)  

---

## ⚙️ Installation & Setup  

### **1️⃣ Clone the repository**  
```bash
git clone https://github.com/VishalPython1594/Calorie-Counter-LIM.git
cd Gemini-Calorie-Counter
```

**2️⃣ Install dependencies**:
```bash
   pip install -r requirements.txt
```

**3️⃣ Set up API Key**
* Obtain a Google Gemini API Key from the Google AI Studio
* Create a .env file and add your API key:
```bash
GOOGLE_API_KEY=your_google_api_key
```

**4️⃣ Run the Streamlit app**
```bash
streamlit run app.py
```

### **🏗️ Project Workflow**
1️⃣ User uploads an image of food via the Streamlit app.
2️⃣ Image is processed and sent to Google Gemini Pro Vision API.
3️⃣ AI identifies food items and estimates their calorie count.
4️⃣ Results are displayed, listing each food item and its calorie count.

### **🖥️ Usage**
Run the app using streamlit run app.py.
Click "Choose an Image" and upload a .jpg, .jpeg, or .png file.
Click "Tell me the total calories" to get calorie breakdown.

### **📊 Sample Output**

![cal_1](https://github.com/user-attachments/assets/2f170565-127b-4882-a70d-f48a4a9f8638)
![cal_2](https://github.com/user-attachments/assets/2af77f03-a27d-4f1c-9555-a7f8142debd2)
![cal_3](https://github.com/user-attachments/assets/895b2825-c066-434f-91b3-456cf02a6fa8)



