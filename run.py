# !/usr/bin/env python
from web import create_app

app = create_app()
# a secret key will protect against modifying cookies and cross-site request forgery attacks
if __name__ == "__main__":
    app.run(debug=True)


