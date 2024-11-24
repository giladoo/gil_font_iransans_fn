# -*- coding: utf-8 -*-
{
    'name': "Font IranSans FN",

    'summary': """
        Enjoy IRANSans persian font """,

    'description': """
        It will effect persian langruage context.
        Most of texts and numbers would be decorated as IranSans font.
    """,

    'author': "Arash Homayounfar",
    'website': "https://giladoo.com/shop/odoo-iransans-font-with-persian-number-2",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Tools/UI',
    'application': False,
    'version': '18.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web'],

    'assets': {
        'web.assets_backend': [
            'gil_font_iransans_fn/static/src/css/fonts.scss',
            'gil_font_iransans_fn/static/src/css/fonts_web.scss',
            ],
        'web.assets_frontend': [
            'gil_font_iransans_fn/static/src/css/fonts.scss',
            'gil_font_iransans_fn/static/src/css/fonts_front.scss',
        ],
        'web.report_assets_common': [
            'gil_font_iransans_fn/static/src/css/fonts.scss',
            'gil_font_iransans_fn/static/src/css/fonts_report.scss',
            ],
        },
    'license': 'LGPL-3',
}
