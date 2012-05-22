Minimal is a small web application that allows you to create web pages
really fast and easily with a beautiful interface thanks to [Bootstrap](http://twitter.github.com/bootstrap/.)

This application saves you time creating a prototype, as you will not have to
write every header, footer, etc for every HTML page. Everything is configured using global
variables and different partials: _navbar.html, _footer.html, etc. take
a look at the templates folder

For example, by default Minimal serves an index page that can be overriden just
copying and pasting the index.html.template into a file named index.html.
Adding a new page is as simple as creating a new file in the template folder,
and requesting it via the URL http://domain/newpage.html

Minimal allows you to focus just in the HTML content, as the header and the
footer are already provided by the application.

Minimal it also has support for Google Analytics, so you only have to paste the
tracking code in the configuration file for tracking all the pages that you
have created. 

Finally, as Minimal is created using the micro-framework [Flask](http://flask.pocoo.org/) it is really easy to extend the application, as there are several plugins that can enhance the user experience.

# Installation

In order to install it you have to follow the next steps:

 * Clone the repository
 * Create a virtualenv for the application: virtualenv env
 * Activate it: . env/bin/activate
 * Install the required libraries in the virtualenv: pip install -r
   requirements.txt
 * Create a settings file for the server: cp settings_local.py.tmpl to
   settings_local.py
 * Launch the demo server: python minimal/app.py

If you want to deploy it using Apache2, you only have to check the **contrib**
folder, where you will find the WSGI application and the Apache2 configuration
site.
