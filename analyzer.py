from clarifai.rest import ClarifaiApp

app = ClarifaiApp("tWTHr0Cms_7ENIrEzeHrYlGHvE_KVIvIZhubVRdV", "YgmB3wnM77i6WDC_V2cg7EhzI6FM6P3ZDtVw49Le")

# get the general model
model = app.models.get("general-v1.3")

url = 'https://www.facebook.com/fishfisherson/videos/10211532042960734/'


data = model.predict_by_url(url=url)
# predict with the model
print(data)

data = data["outputs"][0]['data']['concepts']

newdata = [item['name'] for item in data if item['value'] >= .95]
data = newdata

print(data)