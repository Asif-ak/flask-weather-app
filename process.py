import datetime,urllib.request,urllib.parse,json
class Logic:
    def __init__(self):
        self.lists=[]

    def today(self):
        a = datetime.datetime.now()
        return a.strftime("%A")

    def todate(self):
        return datetime.datetime.now().date()

    def query(self,a):
        baseurl = "https://query.yahooapis.com/v1/public/yql?"
        yql_query = "select wind,atmosphere,astronomy,item,location from weather.forecast where woeid in (select woeid from geo.places(1) where text='{}')and u='c'".format(
            a)
        yql_url = baseurl + urllib.parse.urlencode({'q': yql_query}) + "&format=json"
        result = urllib.request.urlopen(yql_url).read()
        Data = json.loads(result)
        results=str(Data['query']['results'])
        if results == 'None':
            return False
        else:
            self.lists.append(Data['query']['results']['channel']['wind'])
            self.lists.append(Data['query']['results']['channel']['atmosphere'])
            self.lists.append(Data['query']['results']['channel']['astronomy'])
            self.lists.append(Data['query']['results']['channel']['item'])
            self.lists.append(Data['query']['results']['channel']['item']['condition'])
            self.lists.append(Data['query']['results']['channel']['item']['forecast'])
            self.lists.append(Data['query']['results']['channel']['location'])
            return True


    def degtocompass(self,degree):
        val = int((degree / 22.5) + .5)
        arr = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
        return (arr[(val % 16)])

    def item(self,index, key):
        return self.lists[index][key]

    def forcast(self,index):
        dic = {}
        for keys, values in self.lists[5][index].items():
            dic[keys] = values
        return dic



