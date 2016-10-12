# -*- coding: utf-8 -*-
from plone import api
import os


def post_install(context):
    portal = api.portal.get()
    _create_content(portal)


def _create_content(portal):
    if not portal.get('slider-images', False):
        slider = api.content.create(
            type='Folder',
            container=portal,
            title=u'Slider',
            id='slider-images'
        )
        for slider_number in range(1, 4):
            slider_name = u'slider-{0}'.format(str(slider_number))
            slider_image = api.content.create(
                type='Image',
                container=slider,
                id=slider_name
            )
            slider_image.image = load_image(slider_number)
        api.content.transition(obj=slider, transition='publish')


def load_image(slider):
    from plone.namedfile.file import NamedBlobImage
    filename = os.path.join(os.path.dirname(__file__), 'theme', 'img',
                            'slide-{0}.jpg'.format(slider))
    return NamedBlobImage(
        data=open(filename, 'r').read(),
        filename=u'slide-{0}.jpg'.format(slider)
    )


def uninstall(context):
    """Uninstall script"""
    if context.readDataFile('plonethemetango_uninstall.txt') is None:
        return
        # Do something during the uninstallation of this package
