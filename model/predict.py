from datetime import date
import pickle
import pandas as pd

class predict_price():
    def __init__(self, distance, dateTimeStr):
        self.distance = distance
        self.dateTimeStr = dateTimeStr.split(" ")
        self.date = self.dateTimeStr[0]
        self.time = self.dateTimeStr[1]
        self.columns = ['distance', 'LyftCabs', 'UberCabs', 'Black', 'Black SUV', 'Lux', 'Lux Black', 'Lux Black XL', 'Lyft', 'Lyft XL', 'Shared', 'UberPool', 'UberX', 'UberXL', 'WAV', 'EarlyMorning', 'LateNight', 'MorningNoon', 'Night', 'weekend', 'weekday']
    
    def populateTimePeriod(self, toPredData):
        hour = [int(n) for n in self.time.split(":")][0]
        if 3 <= hour and hour <= 6 : toPredData['EarlyMorning'] = 1
        elif 6 < hour and hour <= 17 : toPredData['MorningNoon'] = 1
        elif 17 < hour and hour <= 22 : toPredData['Night'] = 1
        else : toPredData['LateNight'] = 1      
        
        dateList = [int(n) for n in self.date.split("-")]
        d = date(dateList[2], dateList[1], dateList[0]).strftime('%A')
        if d in ["Saturday", "Sunday"] : toPredData["weekend"] = 1
        else : toPredData["weekday"] = 1
        toPredData["weekend"] = 1
        
        return toPredData

    def dataframeFromDict(self, toPred):
        newData = pd.DataFrame(toPred.items()).transpose()
        cols = newData.iloc[0] 
        newData = newData[1:] 
        newData.columns = cols 
        return newData


    def predictCabs(self, toPred):
        with open('model.pkl', 'rb') as f:
            lassoTrainedModel = pickle.load(f)

        res = ""
        cabs = {
          "UberCabs" : ['UberPool', 'Black SUV'],
          "LyftCabs" : ['Shared', 'Lux Black XL']
        }

        for eachCabComp in cabs.keys():
            toPred[eachCabComp] = 1
            priceRange = []
            for eachCabType in cabs[eachCabComp]:
                toPred[eachCabType] = 1
                toPredDf = self.dataframeFromDict(toPred)
                price = lassoTrainedModel.predict(toPredDf.to_numpy())
                priceRange.append(price)
                toPred[eachCabType] = 0
            res += f"For {eachCabComp}, price ranges from ${round(priceRange[0][0], 2)} to ${round(priceRange[1][0], 2)}\n"
            toPred[eachCabComp] = 0
        return res

    def createDataForPrice(self):
        toPred = {}
        for each in self.columns:
            toPred[each] = 0
        toPred["distance"] = self.distance
        toPred = self.populateTimePeriod(toPred)
        return toPred


    def generate_data_return_price(self):
        data = self.createDataForPrice()
        priceStr = self.predictCabs(data)
        return priceStr
