# This is testing reload()
import math
from imp import reload

reload(math)

# DeprecationWarning: the imp module is deprecated in favour of importlib; see the module's documentation for alternative uses
# from imp import reload
