This is a kivy-android speech to text repo.

See a example vedio::


http://youtube.com/shorts/wvZQshoAw-Q?feature=share


To start listening::

    >>> from Speechrecognizer import stt
    >>> stt.start()
    
	
To retrieve partial results while listening::

    >>> assert stt.listening
    >>> print(stt.partial_results)
   
   
To stop listening::


    >>> stt.stop()
  
  
To retrieve results after the listening stopped::


    >>> print(stt.results)
