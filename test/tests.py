from flask import Flask
from nose.tools import assert_equal
from base import webapp
from datetime import datetime
import random
import os

class Test:
    @classmethod
    def setUpClass(self):
        self.webapp = webapp.test_client()
        self.file_name = str(random.randint(0,100)) + "_test.html"
        self.msg = str(random.randint(0,1000)) + "Random Test"
        # Create a random page to be served by the server
        f = open("web/templates/" + self.file_name ,"w")
        f.write(self.msg)
        f.close()

    @classmethod
    def tearDownClass(self):
        """Delete previously created random page"""
        os.remove("web/templates/{}".format(self.file_name))

    def test_01_index(self):
        """Test index page works"""
        res = self.webapp.get('/')
        assert '<h1>Hello, world!</h1>' in res.data, res.data

    def test_02_header(self):
        """Test <head> section is included"""
        res = self.webapp.get('/')
        assert '<meta charset="utf-8">' in res.data, res.data
        assert '<meta name="description" content="' + webapp.config['DESCRIPTION'] + '">' in res.data, res.data
        assert '<meta name="author" content="' + webapp.config['COPYRIGHT'] + '">' in res.data, res.data

    def test_03_styles(self):
        """Test CSS files are included"""
        res = self.webapp.get('/')
        assert 'bootstrap.css' in res.data, res.data
        assert 'bootstrap-responsive.css' in res.data, res.data

    def test_04_googleanalytics(self):
        """Test Google Analaytics is included"""
        res = self.webapp.get('/')
        assert 'UA-XXXXX-Y' in res.data, res.data

    def test_05_navbar(self):
        """Test top navigation bar is included"""
        res = self.webapp.get('/')
        assert 'class="navbar navbar-fixed-top"' in res.data, res.data
        assert 'Home' in res.data, res.data
        assert 'About' in res.data, res.data
        assert 'Contact' in res.data, res.data

    def test_06_herounit(self):
        """Test Hero-Unit is rendered by default"""
        res = self.webapp.get('/')
        assert 'class="hero-unit"' in res.data, res.data

    def test_07_carousel(self):
        """Test Carousel is rendered via settings"""
        webapp.config['CAROUSEL'] = True
        webapp.config['HEROUNIT'] = False
        res = self.webapp.get('/')
        assert 'class="carousel slide"' in res.data, res.data
        assert 'carousel();' in res.data, res.data
        webapp.config['CAROUSEL'] = False
        webapp.config['HEROUNIT'] = True 

    def test_08_footer(self):
        """Test <footer> is included"""
        res = self.webapp.get('/')
        assert '<footer>' in res.data, res.data
        assert '<p>&copy; ' + webapp.config['COPYRIGHT'] + ' ' + str(datetime.now().year) + '</p>' in res.data, res.data

    def test_09_404(self):
        """Test 404 is returned for a wrong URL"""
        res = self.webapp.get("/thisdoesnotexist")
        assert res.status == '404 NOT FOUND', res.status
        assert "404" in res.data, res.data

    def test_10_new_page(self):
        """Test if a random new page is returned after creation"""
        res = self.webapp.get('/' + self.file_name)
        assert self.msg in res.data, res.data
