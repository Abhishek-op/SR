
__all__ = ('stt')

__version__ = '2.0.1.dev0'


from Speechrecognizer import facades
from Speechrecognizer.utils import Proxy

stt = Proxy('stt', facades.STT)

