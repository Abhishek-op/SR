'''

Simple Examples
---------------

To start listening::

    >>> from plyer import stt
    >>> stt.start()

To retrieve partial results while listening::

    >>> assert stt.listening
    >>> print(stt.partial_results)

To stop listening::

    >>> stt.stop()

To retrieve results after the listening stopped::

    >>> print(stt.results)
'''


class STT:
    _language = 'en-US'
   

    _supported_languages = [
        'en-US',
        'pl-PL'
    ]

    results = []
  
    errors = []
    

    partial_results = []

    prefer_offline = True
 

    listening = False
 
    @property
    def supported_languages(self):
      
        return self._supported_languages

    @property
    def language(self):
      
        return self._language

    @language.setter
    def language(self, lang):
       
        if lang in self.supported_languages:
            self._language = lang

    # public methods
    def start(self):
        '''
        Start listening.
        '''

        self.results = []
        self.partial_results = []
        self._start()
        self.listening = True

    def stop(self):

        self._stop()
        self.listening = False

    def exist(self):
       
        return self._exist()

    # private methods
    def _start(self):
        raise NotImplementedError

    def _stop(self):
        raise NotImplementedError

    def _exist(self):
        raise NotImplementedError
