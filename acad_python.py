import logging
import comtypes
import glob
import os
import array
# import operator
import math


try:
    import comtypes.client
    # generate modules for work with ACAD constants
    for pattern in ("acax*enu.tlb", "axdb*enu.tlb"):
        pattern = os.path.join(
            r"C:\Program Files\Common Files\Autodesk Shared",
            pattern
        )
        tlib = glob.glob(pattern)[0]
        comtypes.client.GetModule(tlib)
    import comtypes.gen.AutoCAD as ACAD
except Exception:
    # we are under readthedocs.org and need to mock this
    ACAD = None

# import pyautocad.types
# from pyautocad.compat import basestring, xrange

logger = logging.getLogger(__name__)


class Autocad(object):

    def __init__(self, create_if_not_exists=False, visible=True):
        """
        :param create_if_not_exists: if AutoCAD doesn't run, then
                                     new instanse will be crated
        :param visible: new AutoCAD instance will be visible if True (default)
        """
        self._create_if_not_exists = create_if_not_exists
        self._visible = visible
        self._app = None

    @property
    def app(self):
        """Returns active :class:`AutoCAD.Application`

        if :class:`Autocad` was created with :data:`create_if_not_exists=True`,
        it will create :class:`AutoCAD.Application` if there is no active one
        """
        if self._app is None:
            try:
                self._app = comtypes.client.GetActiveObject('AutoCAD.Application', dynamic=True)
            except WindowsError:
                if not self._create_if_not_exists:
                    raise
                self._app = comtypes.client.CreateObject('AutoCAD.Application', dynamic=True)
                self._app.Visible = self._visible
        return self._app

    @property
    def doc(self):
        """ Returns `ActiveDocument` of current :attr:`Application`"""
        return self.app.ActiveDocument

    #: Same as :attr:`doc`
    ActiveDocument = doc

    #: Same as :attr:`app`
    Application = app

    @property
    def model(self):
        """ `ModelSpace` from active document """
        return self.doc.ModelSpace



class APoint(array.array):
    """ 3D point with basic geometric operations and support for passing as a
        parameter for `AutoCAD` Automation functions

    Usage::

        >>> p1 = APoint(10, 10)
        >>> p2 = APoint(20, 20)
        >>> p1 + p2
        APoint(30.00, 30.00, 0.00)

    Also it supports iterable as parameter::

        >>> APoint([10, 20, 30])
        APoint(10.00, 20.00, 30.00)
        >>> APoint(range(3))
        APoint(0.00, 1.00, 2.00)

    Supported math operations: `+`, `-`, `*`, `/`, `+=`, `-=`, `*=`, `/=`::

        >>> p = APoint(10, 10)
        >>> p + p
        APoint(20.00, 20.00, 0.00)
        >>> p + 10
        APoint(20.00, 20.00, 10.00)
        >>> p * 2
        APoint(20.00, 20.00, 0.00)
        >>> p -= 1
        >>> p
        APoint(9.00, 9.00, -1.00)

    It can be converted to `tuple` or `list`::

        >>> tuple(APoint(1, 1, 1))
        (1.0, 1.0, 1.0)

    """
    def __new__(cls, x_or_seq, y=0.0, z=0.0):
        if isinstance(x_or_seq, (array.array, list, tuple)) and len(x_or_seq) == 3:
            return super(APoint, cls).__new__(cls, 'd', x_or_seq)
        return super(APoint, cls).__new__(cls, 'd', (x_or_seq, y, z))


    @property
    def x(self):
        """ x coordinate of 3D point"""
        return self[0]

    @x.setter
    def x(self, value):
        self[0] = value

    @property
    def y(self):
        """ y coordinate of 3D point"""
        return self[1]

    @y.setter
    def y(self, value):
        self[1] = value

    @property
    def z(self):
        """ z coordinate of 3D point"""
        return self[2]

    @z.setter
    def z(self, value):
        self[2] = value



