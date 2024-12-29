from app import routes  # Assuming your Flask app is defined in `app.py` or similar
from Frozen_Flask import Freezer

# Initialize the Freezer object
freezer = Freezer(routes)

# This will generate static files
if __name__ == "__main__":
    freezer.freeze()  # Generates the static site files in the `build/` directory