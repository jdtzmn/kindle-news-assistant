from .cloudpickle import *
from .cloudpickle_fast import CloudPickler as CloudPickler, dump as dump, dumps as dumps

Pickler = CloudPickler
