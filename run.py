#! /usr/bin/env python
from grandPyApp import app

if __name__ == "__main__":
    """
    debug : updates when the application is modified. 
    There is no longer need to restart the server.
    (To be removed when app will be online.)
    Open error log page when needed.
    """
    app.run(debug=True) # Launch server