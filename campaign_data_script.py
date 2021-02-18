import requests,json
import pandas as pd

# retrive token from file - assumes file ends with \n !
f = open("API TOKEN.txt","r")
token = f.read()
token = token[:-1]
f.close()

headers = {
    'OB-TOKEN-V1': token
}
marketer_id = '00634b8160c24e3b063c76549f9404c0a1'

# prints a json object in a readable way
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

# prints a campaigns data by given id
def get_campaign_data():
    campaign_id = input("Enter your campaign id (for default press ENTER):")
    if campaign_id == '' :
        campaign_id = '00be63761f129a6aa7b0c09b12d56b1241'
    request = requests.get('https://api.outbrain.com/amplify/v0.1/campaigns/'+campaign_id+'?extraFields=', headers=headers)
    if request.status_code != 200 :
        print("Error! response code "+str(request.status_code))

    else:
        jprint(request.json())

# collects january data - creates a CSV with all data and prints campaigns  which spent above given amount
def get_january_data():
    request = requests.get('https://api.outbrain.com/amplify/v0.1/reports/marketers/'+marketer_id+'/campaigns?from=2021-01-01&to=2021-01-30&limit=100&offset=&sort=&filter=&includeArchivedCampaigns=&budgetId=&campaignId=&includeConversionDetails=&conversionsByClickDate=',headers=headers)
    if request.status_code != 200:
        print("Error! response code " + str(request.status_code))

    else:
        amount = input("Enter limited amount spent (for default -100 press ENTER): ")
        if amount == '':
            amount = '100'

        json_data = json.loads(request.text)
        json_data = json_data["results"]

        myData = []
        myAmountData = []

        for line in json_data :
            myDict = {"id" : line["metadata"]["id"],"campaign_name": line["metadata"]["name"],
                      "spend": line["metrics"]["spend"], "conversions" : line["metrics"]["conversions"],
                      "clicks" : line["metrics"]["clicks"]}
            myData.append(myDict)

            if int(line['metrics']['spend']) >= int(amount):
                myAmountData.append(line)

        jprint(myAmountData)

        data = pd.DataFrame(myData)
        data.to_csv(r'Jan_campaigns.csv', index=None, header=True)
        print("Jan_campaigns.csv was successfully created")

def main():
    get_campaign_data()
    get_january_data()

if __name__ == "__main__":
    main()