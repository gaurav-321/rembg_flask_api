from rembg import remove, __version__
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/remove', methods=['POST'])
def remove_background():
    # Get the input image file from the request
    image_file = request.files['image']

    # Process the image using rembg
    image_data = image_file.read()
    output_data = remove(image_data)

    # Return the processed image
    return output_data

if __name__ == '__main__':
    app.run()