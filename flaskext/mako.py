# -*- coding: utf-8 -*-
from __future__ import absolute_import
from mako.lookup import TemplateLookup
from mako.template import Template
from flask import g, request, session, get_flashed_messages, url_for

def init_mako(app):
    app = app
    get = app.config.get
    dirs = get('MAKO_DIRECTORIES', get('MAKO_DIRECTORY', '.'))
    lookup = TemplateLookup(directories=dirs,
                            input_encoding=get('MAKO_INPUT_ENCODING', 'utf-8'),
                            output_encoding=get('MAKO_OUTPUT_ENCODING', 'utf-8'),
                            module_directory=get('MAKO_CACHEDIR', None),
                            collection_size=get('MAKO_CACHESIZE', None),
                            imports=get('MAKO_IMPORTS', None))

    @app.before_request
    def before_request():
        g._makoLookup = lookup


def render_template(path, **kw):
    """
    Replacement for the flask render_template which uses mako instead
    If mako does not exist, it falls back on the built-in (Jinja2)
    """
    try:
        return g._makoLookup.get_template(path).render(g=g, request=request,
                                                       get_flashed_messages=get_flashed_messages,
                                                       session=session,
                                                       url_for=url_for, **kw)
    except AttributeError:
        from flask import render_template
        return render_template(path, **kw)
