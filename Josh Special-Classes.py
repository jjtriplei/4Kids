class Stream():
  stream_name = "" # This is where you'd put twitch  
  url = "" #created a variable to hold the url to the stream    
  parsed_html = None
        
  def __init__(self, url, stream_name):
    # Calling the class method (a function is called a method when a class owns it)
    self.get_stream_response(url)    
    self.stream_team = stream_name

  def get_stream_response(url):
    raw_html = request(url)
    # Some parse function here, I'd probably use the requests library and beautifulsoup (You can look those up waaay later)
    self.parsed_html = parse(raw_html)  # NOte: Parse doesn't actually exist ... just giving you an example
    

    
# Now you have two classes that have been created which will do different things with the streams
# Like twitch will look for players, justin.tv might have viewers but they both need to have some
# Common functionality that exists in the base Stream class.
class Twitch(Stream):   
    def __init__(self,url):
      # Probably better to use super here to call the base class but I'm using this so it's easier to grasp.
      Stream(self, url, "Twitch")
        
    
    
class Justin(Stream):        
    def __init__(self,url):      
        Stream(self, url, "Justin.TV")  # What did I do here?
    

    
Street_Fighter_Stream = Twitch("http://twitch.tv/Capcomfighters")
Some_Dumb_Cat_Lady_Video = Justin("http://justin.tv/catladyusa")
