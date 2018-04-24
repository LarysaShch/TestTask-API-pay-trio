# Test task API pay-trio

Необходимо​ ​ разработать​ ​ и ​ ​ реализовать​ ​ flask​ ​ сервис.

Сервис​ ​ состоит​ ​ из​ ​ одной​ ​ страницы​ ​ со​ ​ следующими​ ​ элементами:
- Сумма​ ​ оплаты​ ​ (поле​ ​ ввода​ ​ суммы)
- Валюта​ ​ оплаты​ ​ (выпадающий​ ​ список​ ​ со​ ​ значениями​ ​ USD,​ ​ EUR)
- Описание​ ​ товара​ ​ (многострочное​ ​ поле​ ​ ввода​ ​ информации)
- Оплатить​ ​ (кнопка)

## Installation
- Clone.  git clone https://github.com/LarisaShcherbachenko/TestTask-API-pay-trio.git

- Create virtualenv and install needded libraries from requirements.txt

```bash
virtualenv --python=python3.6 ~/venv
pip3 install -r requirements.txt
```

For running server use:

```bash
export FLASK_APP=main.py
flask run
```










Taptica Bulk API allows publishers to pull offers Meta data directly from our servers, the offers inventory will be associated with your account by Taptica media managers.



Since there are frequent changes in the offers list,The publisher is responsible to generate an API request '''every 15 minutes'''. 
<br>In case an active  is no longer part of the the response, please  '''Remove''' the offer from production.


Taptica is limiting the numbers of daily requests per country,once you exceed 3000 requests you will not get a response.

==='''Request'''===

• The request is sent via an HTTP "Get request" to the following URL: https://api.taptica.com/v2/bulk?token={affiliate-token}

• The body of the POST contains URL encoded key/value pairs separated by "&". 

• Request headers should include:<br>
Header name: Accept-Encoding<br>
Header value: gzip<br>


Json Gzipped format - for testing purposes only, please do not use with live traffic:
 https://api.taptica.com/v2/bulk?token=7Bhisedf1PmH8bs7goa2jw%3d%3d&platforms=iPhone&version=2&format=json&countries=US



'''Request parameters'''
* Case sensitive 
{| border="1" cellspacing="0"  cellpadding="5" valign="top" style="color: black" "

|'''Parameter'''
|'''Name In Request'''  
|'''Description'''  
|'''Example'''  
|'''Mandatory'''  
|-

|token
|token
|Your Taptica affiliate token - will be sent as part of the integration
|token=7Bhisedf1PmH8bs7goa2jw%3d%3d
|Yes
|-

|platforms
|Platforms
|Indicate the Platform of the requested offers. Can be either iPhone, iPad, iPod, Android. 
|platforms=iPhone
|Yes
|-

|countries
|countries
|Enter the country codes of the requested offers. Can be multiple selection.
|countries=US,BG
|No
|-

|version
|version=2
|current version of Taptica API
|version=2
|Yes
|-


|payout Type
|payoutType
|Specifies the requested offer payout. Can be either CPA, CPC,CPE, CPM. Mostly, Taptica supports CPA, CPC , CPE offers.
|payoutType=cpa
|No
|-

|minPayout
|Min Payout
|Specifies the minimum payout offer you would like to get in the response. (if you do not want to filter by country leave it empty)
|minPayout=1.2
|No
|-

|categories
|Categories
|Specifies the offer categories you would like to get in the response.
|categories=Games,Travel and Local,
|No
|-


|noCreative 
|No creative
|No creative  allow the publisher to decide if the response will include the  creative or won't (the value can be false or true)
|noCreative=True
|No
|-

|size
|Creative size
|allow the publisher to decide which creative size will be include in the response (in case he wise to get specific banner size)
|size=320X480,320X50,728X90
|No
|-

|format
|format
|Specifies the response type. json(Default).
|json
|No
|-

|gzip
|gzip
|Taptica response will be sent zipped
|true
|YES
|-

|}

'''Category List in compliance with IAB'''

please see category list here : https://gist.github.com/thiagozs/6732050




'''Response parameters'''

{| border="1" cellspacing="0" cellpadding="5" valign="top"

|'''Parameter'''  
|'''Description'''  
|'''Example'''  
  
|-

|OfferId
|Taptica internal offer ID.
|4960
|-

|Name
|Taptica internal offer name.
|Underworld Empire- US- iPhone
|-

|Description
|Offer description.
|Play with MILLIONs of players NOW in the LARGEST, most INTENSE, SOCIAL CRIME MMO!
|-

|platforms
|Supported platform.
|iPhone
|-

|MinOsVersion
|Minimum OS version.
|4.3
|-

|MarketAppId
|Google / Appstore application id.
|555150599
|-

|AppRate
|application rate based on rate in the app/google store
|"AppRate": "4"
|-

|PreviewLink
|Link to the application in Appstore.
|https://itunes.apple.com/us/app/underworld-empire/id555150599
|-

|TrackingLink
|Taptica basic tracking link *(please see explanation below)
|http://tracking.taptica.com/aff_c?tt_ls=b&offer_id=4390&tt_appid=555150599&aff_id=2004&tt_sub_aff=YYYY&tt_bannerid=49552&tt_mac=&tt_mac_sha1=&tt_mac_md5=&tt_idfa=&tt_idfa_sha1=&tt_idfa_md5=&tt_aff_impid=1321sads35sa&tt_aff_clickid=qa143287w
|-

|IsDeviceIdMandatory
|when set to true, it means that the application '''must''' get at least one of the device parameters specified in the "DeviceIds".
|false / true
|-

|DeviceIds
|Indicates the supporeted device ids
|tt_mac,tt_mac_sha1,tt_mac_md5,tt_idfa,tt_idfa_sha1,tt_idfa_md5
|-

|SupportedCountriesV2
|Indicates the offer's supported countries (returned as list).
|US
|-


|city
|Indicates the offer's supported cities (returned as list under each coutry).
|Albany
|-

|region
|Indicates the offer's supported regions (returned as list under each country).
|New York
|-

|payoutType
|Indicates the offer Payout Type, can be either CPA, CPC, CPM,CPE.
|CPA
|-

|Payout
|Indicates the offer Payout. 
|1.2
|-

|DailyBudget
|Returns the remaining budget for specific  publisher in USD  or returns 'unavailable' when there is no limit. 
|Unlimited / 1500
|-

|Categories
|Shows the offer categories as sets in Taptica system (returned as list).
|Entertainment / Games
|-

|HasVideo
|offer contains a video creative.
|true/false
|-

|VideoBanner
|Companion Banner for video creative
|"CompanionBanner",
"Id": 2334079,
"Name": "480x320.jpg"}]

|-

|Creatives
|provides the creative data as Banner ID, Banner Name, Creative Link, Creative Type, Creative Size. (returned as list) 
|
 Id 49552
 Name 20130327115527-DJ_Tira_static_Banner_320X320.gif
 CreativeLink http://media.go2speed.org/brand/files/taptica/3530/20130327115527-DJ_Tira_static_Banner_320X320.gif
 CreativeType banner
 CreativeSize 320x320
|-

|BlockedSubAffiliateV2
|Unauthorized sub affiliate, Specifies the sub affiliate of the affiliate which are unauthorized to run the offer.
|"373329","sub_affliate353"
|-

|AllowedSubAffiliate
|Authorized sub affiliate, Specifies the sub affiliate of the affiliate which are authorized to run the offer.
|Unavailable / 1265 ...
|-

|isAppNameMandatory
|Indicates offers with a mandatory request to pass the specific application name of the media source to Taptica through the click URL, using parameter 'tt_app_name'
|false/true
|-

|BannerText
|Offer promotion text.
|Get Free Application Now!
|-

|IsIncent
|Incentivised traffic allowed 
|false/true
|-

|CallToAction
|Offer promotion text- to be used with native ads
|Get Free Application Now!
|-

|payableAction
|event the user required to complete in order for the publisher to get paid
|Tutorial
|-

|AppIconURL
|link to the application Icon on app store or Google play 
|https://lh6.ggpht.com/LmBa6jgU5zTnvb4G52ZYeCr2CAq8BEB9atNBTGkyZXIsEZTjxDA_F7YV6l1t9gpBEw=w300-rw
|-

|AppProviderName
|The Application Provider Name
|Playtika LTD
|-

|AppName
|The application official name as it on app store or Google play
|Candy Crush Sega
|-

|Carriers
|mobile service carriers to be targeted 
|[t-mobile]
|-

|Networks
|network connection type to be targeted 
|["WIFI","3G"]
|-

|}


{| border="1" cellspacing="0" cellpadding="5" valign="top"

|'''Parameter'''  
|'''Description'''  
|'''Example'''  
|-

'''Taptica optional affiliate Keys''' 


|Affiliate click ID
|Used for click id that the publisher may want to send Taptica and get back via S2S postback  (alfa numeric)
|tt_aff_clickid=qa143287w 
|-


|Sub affiliate
|Used for sending Taptica your sub affiliate id upon click. The publisher can get it back via S2S postback (alfa numeric)
|tt_sub_aff=13461d46
|-

|Affiliate impression ID
|Used for impression id that the publisher may want to send Taptica and get back via S2S postback (alfa numeric)
|tt_aff_impid=1321sads35sa
|-

|Pipeline Data
|Used for any information that the publisher may want to send Taptica upon click and get back via S2S postback (alfa numeric)
|pd=abcd1234
|-
|}

'''Taptica Device Keys''' 

{| border="1" cellspacing="0" cellpadding="5" valign="top"

|'''Parameter''' 
|'''Description'''  
|'''Example'''   
|-

|IMEI
|Device  '''Plain'''  IMEI
|tt_imei=86453214567892
|-

|IMEI SHA1
|Device  IMEI in SHA1 format
|tt_imei_sha1=35eb6d1fc48b502e239b6449e9df534e415cad95
|-

|IMEI MD5
|Device IMEI in MD5 format
|tt_imei_md5=946cc1baf8bcaec827bb1828cc6d9a94
|-

|Android Advertising ID 
|Device Android advertising plain ID
|tt_advertising_id=3ee0149b4ccef71bs85d24derg
|-

|Android Advertising ID SHA1
|Device  Android advertising ID in SHA1 format 
|tt_advertising_id=32f2e52e8157fcb729d799d1ca69160df2edf8974
|-

|Android Advertising ID MD5
|Device Android advertising ID in MD5 format 
|tt_advertising_id=2315w52e8157fcb729d799d1ca691608speofd2
|-

|Mac Address
|Device  Plain  Mac Address or when you don’t know what is the format of the Mac Address you have. (upper case with colon)
|tt_mac=44:2A:60:G5:GE:G5
|-

|Mac Address SHA1
|Device  Mac Address in SHA1 format (upper case with colon)
|tt_mac_sha1=fa6bb084ae52461328eb9f06039be222ef287246
|-

|Mac Address MD5
|Device  Mac Address in MD5 format (upper case with colon)
|tt_mac_md5=80efe2256d548c85ca2f2d18de241a80
|-

|IDFA
|Device  Plain  IDFA or when you don’t know what is the format of IDFA you have.
|tt_idfa=771468523E3346ABAA04E207BBAF094B
|-

|IDFA SHA1
|Device  IDFA in SHA1 format
|tt_idfa_sha1=ee5c19f8cf370b5978f4b9f33343a5e79c58df9a
|-

|IDFA MD5
|Device  IDFA in MD5 format
|tt_idfa_md5=bb1e0285fbb97ba83fdb4e72514d62f5
|-
|}


'''Error messages'''

{| border="1" cellspacing="0" cellpadding="5" valign="top"

|'''Error Code'''
|'''Error Text'''  
|'''Error description'''   
|-

|0
|OK
|Success
|-

|100
|Not Modified.
|There was no data to return, please try again. if consist please contact Taptica Support
|-

|200
|Bad Request.
|Bad Request for parameter + the bad parameter
|-

|300
|Unauthorized.
|Authorization error. Authentication credential are missing or incorrect.
|-

|301
|Invalid token.
|The token that was delivered  is invalid
|-

|400
|General Error.
|Any other error that does not fall under the above errors
|-

|}


'''Sample Json Response'''

{"Error":"OK","ErrorCode":0,"Data":[{"AppIconUrl":"http:\/\/a4.mzstatic.com\/us\/r30\/Purple4\/v4\/20\/4c\/41\/204c41c4-de06-9d79-7a28-3a3790821887\/mzl.oqwgeagh.175x175-75.jpg","AppName":"Game of War - Fire Age","AppProviderName":"Machine Zone, Inc","AppRate":"4.5","BannerText":null,"BlockedSubAffiliateV2":["323232","u_ttr01234"],"isAppNameMandatory": 
