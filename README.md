# Background Removal API using rembg and Flask

This project provides a simple API for removing the background from an image using the `rembg` library and Flask. It accepts an image file via a POST request and returns the processed image with the background removed.

## Installation

1. Clone this repository to your local machine.
    
    ```shell
    git clone https://github.com/gaurav-321/rembg_flask-api.git

## Usage
       python app.py
Send a POST request to the /remove endpoint with the input image file attached.

       curl -X POST -F "image=@path/to/your/image.png" http://127.0.0.1:5000/remove > output.png


Replace path/to/your/image.png with the actual path to the image you want to process.

The processed image with the background removed will be saved as output.png.

## Contributing
Contributions are welcome! If you find a bug or want to improve the API, feel free to create a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.