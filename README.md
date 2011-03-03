Flask Mako
==========

Provides Mako support in Flask.

Installation
------------
    setup.py install
    
    

Usage
-----

*app.cfg* (or however you configure your app)

    # one or more directories
    MAKO_DIR = 'sourcery/templates'
    # optional, if specified Mako will cache to this directory
    MAKO_CACHEDIR = '/tmp/mako'
    # optional, if specified Mako will respect the cache size
    MAKO_CACHESIZE = 500


*run.py* (or wherever you create your app)
    
    def create_app(name, **kw):
        from flask import Flask, g
        from flaskext.mako import init_mako
        
        app = Flask(name)
        app.config.update(kw)
        init_mako(app)

*views.py*

    from flaskext.mako import render_template
    
    app = Module(__name__)

    @app.route('/')
    def index():
        return render_template('test.html', username='Anonymous')

        