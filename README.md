# rembg_flask_api

## Description

`rembg_flask_api` is a simple Python program that creates a Flask web application. It allows users to upload an image and remove its background using the `rembg` library. The project is designed to be easy to use and integrate into other applications.

## Features
- **Image Background Removal**: Utilizes the `rembg` library to efficiently remove backgrounds from images.
- **Flask Web API**: Exposes a RESTful API for processing image uploads.
- **User-Friendly Interface**: Provides clear instructions and examples for setting up and using the project.

## 🛠️ Installation

To install the required dependencies, run the following command:

```sh
pip install Flask rembg
```

## 💻 Usage

### Basic Usage

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Run the Flask application using the following command:

```sh
python app.py
```

4. Open a web browser and go to `http://127.0.0.1:5000/`. You should see the upload form where you can select an image to remove its background.

### Example Code

Here's a simple example of how to use the API:

```python
import requests
from PIL import Image
from io import BytesIO

# Define the API URL
API_URL = "http://127.0.0.1:5000/remove-background"

# Open an image file
with open("path/to/your/image.jpg", "rb") as image_file:
    # Send a POST request with the image data
    response = requests.post(API_URL, files={"file": image_file})

# Check if the request was successful
if response.status_code == 200:
    # Open the processed image
    processed_image = Image.open(BytesIO(response.content))
    processed_image.show()
else:
    print("Failed to process image")
```

## 🎨 Configuration

The project does not require any configuration settings or environment variables.

## 🧪 Tests

To run tests, you can use the following command:

```sh
python request.py --api-test-count=10
```

This will send 10 POST requests to the API and measure the response time.

## 📁 Project Structure

```
rembg_flask_api/
├── app.py          # Main Flask application file
├── rembg           # rembg library for background removal
└── request.py      # Script for testing the API
```

## 👥 Contributing

Contributions are welcome! Please read our [CONTRIBUTING.md](https://github.com/gag3301v/rembg_flask_api/blob/master/CONTRIBUTING.md) for more details on how to contribute.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/gag3301v/rembg_flask_api/blob/master/LICENSE) file for details.