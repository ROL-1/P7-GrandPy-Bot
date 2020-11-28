#! /usr/bin/env python
from grandPyApp import app
from grandPyApp.settings import DEBUG

if __name__ == "__main__":
    """
    debug : updates when the application is modified.
    There is no longer need to restart the server.
    (To be removed when app will be online.)
    Open error log page when needed.
    """
    app.run(debug=DEBUG)
