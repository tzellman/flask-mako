# -*- coding: utf-8 -*-
from __future__ import absolute_import
from mako.lookup import TemplateLookup
from mako.template import Template
from flask import request, session, get_flashed_messages, url_for, g
from flask import _request_ctx_stack


def init_mako(app, **kw):
    """
    Initializes the Mako TemplateLookup based on the application configuration
    and updates the _request_ctx_stack before each request
    """
    
    def get_first(dicts, keys, default=None):
        # look in one or more dictionaries returning the first found value
        for d in dicts:
            found = filter(lambda x: x in d, keys)
            if found:
                return d[found[0]]
        return default
    
    dirs = get_first([kw, app.config],
                     map(lambda x: 'MAKO_%s' % x, ('DIRS', 'DIRECTORIES', 'DIR', 'DIRECTORY')),
                     default='.')
    if type(dirs) == str:
        dirs = dirs.split(' ')
    
    get = app.config.get
    kw['input_encoding'] = kw.pop('input_encoding', get('MAKO_INPUT_ENCODING', 'utf-8'))
    kw['output_encoding'] = kw.pop('output_encoding', get('MAKO_OUTPUT_ENCODING', 'utf-8'))
    kw['module_directory'] = kw.pop('module_directory', get('MAKO_CACHEDIR', None))
    kw['collection_size'] = kw.pop('collection_size', get('MAKO_CACHESIZE', -1))
    kw['imports'] = kw.pop('imports', get('MAKO_IMPORTS', None))
    
    lookup = TemplateLookup(directories=dirs, **kw)
    
    @app.before_request
    def before_request():
        _request_ctx_stack.top._mako_lookup = lookup
    
    return app

def render_template(path, **kw):
    """
    Replacement for the flask render_template which uses mako instead
    If mako does not exist, it falls back on the built-in (Jinja2)
    """
    try:
        render = _request_ctx_stack.top._mako_lookup.get_template(path).render
    except AttributeError, e:
        from flask import render_template
        return render_template(path, **kw)
    else:
        return render(g=g, request=request,
                      get_flashed_messages=get_flashed_messages,
                      session=session, url_for=url_for, **kw)
