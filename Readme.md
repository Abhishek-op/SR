# 💡 This is a kivy-android speech to text implementation.
➡️➡️See a example vedio➡️
[<img align="right" alt="GIF" src="https://img.youtube.com/vi/wvZQshoAw-Q/0.jpg" width="300px" />](https://www.youtube.com/watch?v=wvZQshoAw-Q)

#### Note: Needed permissions for Android: `RECORD_AUDIO`, `INTERNET`[if you want online voice recognition API to be used]

## 📌 How to use

#### To start listening::

    >>> from Speechrecognizer import stt
    >>> stt.start()
#### To retrieve partial results while listening::

    >>> assert stt.listening
    >>> print(stt.partial_results)
   
   
#### To stop listening::


    >>> stt.stop()
  
  
#### To retrieve results after the listening stopped::


    >>> print(stt.results)
    
## ⭐Give this Project a Star and also Check out my Github profile ☝️ [Abhishek-op](https://github.com/Abhishek-op)




