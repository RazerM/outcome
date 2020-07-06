"""Top-level package for outcome."""

from ._impl import Error, Outcome, Value, acapture, capture
from ._util import AlreadyUsedError, fixup_module_metadata
from ._version import __version__

__all__ = (
    'Error', 'Outcome', 'Value', 'acapture', 'capture', 'AlreadyUsedError'
)

fixup_module_metadata(__name__, globals())
del fixup_module_metadata
