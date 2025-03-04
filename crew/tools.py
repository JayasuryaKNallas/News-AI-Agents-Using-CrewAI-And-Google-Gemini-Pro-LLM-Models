import os
from dotenv import load_dotenv
from crewai_tools import SerperDevTool

# ✅ Load environment variables from .env
load_dotenv()

# ✅ Get the SERPER_API_KEY safely
serper_api_key = os.getenv('SERPER_API_KEY')

# ✅ Check if API key is available
if not serper_api_key:
    raise ValueError("⚠️ SERPER_API_KEY is missing. Please check your .env file.")

# ✅ Set the environment variable explicitly
os.environ['SERPER_API_KEY'] = serper_api_key

# ✅ Initialize the tool for internet searching capabilities
tool = SerperDevTool()

print("✅ SerperDevTool initialized successfully!")
