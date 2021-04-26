This is a kivy-android speech to text repo.

See a example vedio::


http://youtube.com/shorts/wvZQshoAw-Q?feature=share

note::
    Needed permissions for Android: `RECORD_AUDIO` (and `INTERNET` if you want
    online voice recognition API to be used)


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
Buy me a cup of coffee: paypal:: 
https://www.paypal.me/thehackerone


![image](https://user-images.githubusercontent.com/83164668/116036818-dd158100-a684-11eb-961e-e7f0172e69d2.png)

