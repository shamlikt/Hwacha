import broadcast
import pytest







def test_broadcst():




    
    key={'consumer_key':'igjX6vqB8HtMzPByguX9KUtqv',
     'consumer_secret': 'R8pyvLiKSDDTjyf84DnKVgM4IQLYTXq9fDdCbsq3vCEzXkC7qz',
     'access_token': '4472517314-QveTAuRwPQ0JKnBTkVobZZTG3KusZm8fFBUSXKw',
     'access_token_secret':'XItUgPH1VCP027HufEewBqdO45dCEz4Ga4IwqOmgo2brN',
      }
    soc_media= 'twitter'
    push = broadcast.pushmessage('Hello Hwach',soc_media,key)
    assert push == None
    

def test_broadcst2():

    wrong_key = {'consumer_key':'qB8HtMzPByguX9KUtqv',
     'consumer_secret': 'R8pyvLiKSDDTjyf84DnKVgM4IQLYTXq9fDdCbsq3vCEzXkC7qz',
     'access_token': '44725173veTAuRwPQ0JKnBTkVobZZTG3KusZm8fFBUSXKw',
     'access_token_secret':'tUgPH1VCP027HufEewBqdO45dCEz4Ga4IwqOmgo2brN'
     }
    soc_media= 'twitter'
    error_code = 89
    
    push = broadcast.pushmessage('Hello Hwach',soc_media,wrong_key)
    print push
    assert push == error_code
    

 
