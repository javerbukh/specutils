from __future__ import absolute_import, division, print_function

from .registries import loader_registry
from .registries import io_registry

import logging
from ..core.data import Data

import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
from astropy.nddata import StdDevUncertainty
from astropy.units import Unit


def fits_reader(filename, filter, **kwargs):
    """
    This generic function will query the loader factory, which has already
    loaded the yaml configuration files, in an attempt to parse the
    associated fits file.
    """
    hdulist = fits.open(filename, **kwargs)
    ref = loader_registry.get(filter)

    wcs = WCS(hdulist[ref.wcs['hdu']].header)
    data = hdulist[ref.data['hdu']].data
    uncertainty = None
    unit = Unit("")
    mask = np.zeros(shape=data.shape)

    # Grab the data array, use columns if necessary
    if ref.data.get('col') is not None:
        try:
            data = data[data.columns[ref.data['col']].name]
        except AttributeError:
            logging.warning("No such columns available.")

    if ref.uncertainty is not None and ref.uncertainty.get('hdu') is \
            not None:
        uncertainty = hdulist[ref.uncertainty['hdu']].data
        uncertainty_type = ref.uncertainty.get('type') or 'var'

        # This will be dictated by the type of the uncertainty
        uncertainty = StdDevUncertainty(uncertainty)

    if ref.mask is not None and ref.mask.get('hdu') is not None:
        try:
            mask = hdulist[ref.mask['hdu']].data
        except IndexError:
            logging.warning("Mask extension not valid.")

    return Data(data=data, uncertainty=uncertainty, mask=mask, wcs=wcs,
                unit=unit)


def fits_identify(origin, *args, **kwargs):
    return isinstance(args[0], basestring) and \
           args[0].lower().split('.')[-1] in ['fits', 'fit']


# Add IO reader/identifier to io registry
io_registry.register_reader('fits', Data, fits_reader)
io_registry.register_identifier('fits', Data, fits_identify)
