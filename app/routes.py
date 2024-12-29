from app import app  # Assuming your Flask app is defined in `app.py` or similar
from flask_frozen import Freezer

# Initialize the Freezer object
freezer = Freezer(app)

# This will generate static files
if __name__ == "__main__":
    freezer.freeze()  # Generates the static site files in the `build/` directory
