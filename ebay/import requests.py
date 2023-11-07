import requests
# Configuração das credenciais
app_id = 'IsaaclAm-appsite-SBX-34e5ff41f-b7270287'
access_token = 'v^1.1#i^1#p^1#I^3#f^0#r^0#t^H4sIAAAAAAAAAOVYe2wURRjvXR+G8FCCojYEz4N/pOzePu56dyt3ybVH4ZJCC3f2gSLO7s62S/d2l51Z2uMfzhIRAyGayCNBTSOiIUY0JEJMRCPxATGgBB+JxkhAsaJEDC+f6Oz2KNdCoNBLbOL+s5mZ7/vm+/3m++abGSZfNW7W2vlrL0703ObtyzN5r8fDjmfGVVXWTCr3VleWMUUCnr78zHxFb3n/HASymikshsg0dAR9PVlNR4LbGfPbli4YAKlI0EEWIgFLQjqxoFHgaEYwLQMbkqH5falkzC8GFQAgD2BtrcQyikx69cs2M0bMzzEcG+aUIOCjbIiHIhlHyIYpHWGgY3ecp1iWYkIZNiSwQYHl6AjDLPH7WqCFVEMnIjTjj7vuCq6uVeTr9V0FCEELEyP+eCrRkG5KpJJzF2bmBIpsxQs8pDHANhraqjdk6GsBmg2vPw1ypYW0LUkQIX8gPjDDUKNC4rIzt+C+S3U4CGSZDfIQRgDgZVASKhsMKwvw9f1welSZUlxRAepYxbkbMUrYEJdDCRdaC4mJVNLn/BbZQFMVFVox/9y6RHuiuZnYQgBIWiJLAdNEKoZUuq6N4oMwpChBVqHEMBdmuEi4MM+AsQLLwyaqN3RZdThDvoUGroPEaTicGqaIGiLUpDdZCQU7DhXLhQsUhqOhJc6aDiyijTt1Z1lhlvDgc5s3XoBBbYwtVbQxHLQwfMBlKOYnNKiyf/igG4qF6OlBMX8nxqYQCHR3d9PdPG1YHQGOYdhA24LGtNQJsyRAiKyT6668emMFSnWhSJBoIlXAOZP40kNClTigd/jjQZblgkyB96FuxYf3XtVRhDkwNCFKlSCRWkaOQBlG+Igkh9hIKRIkXojRgOMHFEGOygKrC2JTAxKkJBJndhZaqizwIYXjIwqk5NqoQgWjCgnbkFxLsQqEDISiKEUj/6M8GWmkp6FkQVyaUC9VmGM91x7tbGxO1GTbRS21wmbwYrCqvYdPtiG1XQ6kUGtNu1UXbVhhxEaaDNcEX6+phJkMmX/s5fp8A2EojwpeWjJM2GxoqpQbWwvMW3IzsHCuzs6RdhpqGvmNCmrCNFMl2rBLBfLm9opbg13COvXf1KhrokJO3I4tVI4+IgaAqdJOFaIlJ9eNbMAA5AjidC9zvfZdLXi1UEC0c3SHDREmnsjkEDhiJRJGWZoUNHnkKgPlkoAYuQq5Yci2hG9pIrcu04RNtaMTo5uas2c0pIi21jVyFRkCbVQhqpJ7xpgKUIJ0ALIqD1wQaBc3jVZKtAWRYVvkbkQ3OQfmjNEFdXL+wJahadBqYUe982azNgaiBsfaFlyCvUgF5HBU0es5N5ZwsbXRKBsNcyFuVNgk9/izbKxVkBIXzpu4BgWGvsnEy9yP7fXsY3o9b3k9HibMUGwN80BV+UMV5RP8jnc0ArosGj20ChSa7Ho6wLYF6S6YM4Fqeas86lefSb8VvQb1LWXuGXwPGlfOji96HGKmXRmpZG+/eyLHsywTYkNskOWWMDOujFawUyvuzJxa8+zDcMuhHc9Vn97V//MbJxedTDITB4U8nsoyErplvo/FD+8488nfL7ese/HTi5t6lLqd5uq2+ZOnrGMvnQD0Cu/21tYTj17o+yuPX7p/67btm6aev68r81jj07n1FeeqX1s1+czrB96x56W25adXjP98Q8ORSxub9+V7zyw/tuH4Cy3P2I9k9vwo1jeeT3z71EXfoR2Pl116ZRG3d/bZ3ZW9U+b+0dn/xJqVu3//dcJqIznPG9v/6j+nniz7SZl2cvGx6X+iw+8mTzz/zf5Zm+Wte/Yeqf5B0ne+2c/dde7Agu+4/PtfHFzaEtw17fSFvUelSV+qVWt43jAzB49+JMz0PvjsB30dm1ZLX59d+0vm2OF4/L32jQc3J4/fa2xoXX+BPjShzDvj+7c5avaWgWX8F05B6wOnEwAA'

api_url = 'https://api.sandbox.ebay.com/buy/deal/v1/deal_item?category_ids=9355'
# Cabeçalhos da solicitação
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'X-EBAY-C-MARKETPLACE-ID':'EBAY_US',
    'X-EBAY-C-ENDUSERCTX':'affiliateCampaignId=<ePNCampaignId>,affiliateReferenceId=<referenceId>',
}
# Realiza a chamada de API
response = requests.get(api_url, headers=headers)
# Processa a resposta
if response.status_code == 200:
    data = response.json()
    print(data)
    # Faça algo com os dados
else:
    print(f'Erro na chamada de API: {response.status_code}')

"""buy_apis = {
    'Search': 'https://api.sandbox.ebay.com/buy/browse/v1/item_summary/search?q=drone&limit=3',#browse_api
    'json': '''X-EBAY-C-MARKETPLACE-ID:EBAY_US
X-EBAY-C-ENDUSERCTX:affiliateCampaignId=<ePNCampaignId>,affiliateReferenceId=<referenceId>'''
}

sell_apis = {
    'getReportMetaData': 'https://api.sandbox.ebay.com/sell/marketing/v1/ad_report_metadata', #as duas marketing API
    'json': '''Accept:application/json''',
    'getReportMetaDataForReportType': '''https://api.sandbox.ebay.com/sell/marketing/v1/ad_report_metadata/ACCOUNT_PERFORMANCE_REPORT''',
    'json': 'msm de cima'
}

shopping_api = {
    'GetCategoryInfo': 'https://open.api.sandbox.ebay.com/shopping',
    'json': '''X-EBAY-API-IAF-TOKEN:f'Bearer {access_token}'
X-EBAY-API-SITE-ID:0
X-EBAY-API-CALL-NAME:GetCategoryInfo
X-EBAY-API-VERSION:863
X-EBAY-API-REQUEST-ENCODING:xml''',

    'FindProducts': 'https://open.api.sandbox.ebay.com/shopping',
    'json': '''X-EBAY-API-IAF-TOKEN:f'Bearer {access_token}'
X-EBAY-API-SITE-ID:0
X-EBAY-API-CALL-NAME:FindProducts
X-EBAY-API-VERSION:863
X-EBAY-API-REQUEST-ENCODING:xml''',

    'getebaytime': 'https://open.api.sandbox.ebay.com/shopping',
    'json': '''X-EBAY-API-IAF-TOKEN:f'Bearer {access_token}'
X-EBAY-API-SITE-ID:0
X-EBAY-API-CALL-NAME:GeteBayTime
X-EBAY-API-VERSION:863
X-EBAY-API-REQUEST-ENCODING:xml''',

    'getitemstatus': 'https://open.api.sandbox.ebay.com/shopping',
    'json': '''X-EBAY-API-IAF-TOKEN:f'Bearer {access_token}'
X-EBAY-API-SITE-ID:0
X-EBAY-API-CALL-NAME:GetItemStatus.
X-EBAY-API-VERSION:863
X-EBAY-API-REQUEST-ENCODING:xml''',

    'getmultipleitems': 'https://open.api.sandbox.ebay.com/shopping',
    'json': '''X-EBAY-API-IAF-TOKEN:f'Bearer {access_token}'
X-EBAY-API-SITE-ID:0
X-EBAY-API-CALL-NAME:GetMultipleItems
X-EBAY-API-VERSION:863
X-EBAY-API-REQUEST-ENCODING:xml''',

    'getshippingcosts': 'https://open.api.sandbox.ebay.com/shopping',
    'json': '''X-EBAY-API-IAF-TOKEN:f'Bearer {access_token}'
X-EBAY-API-SITE-ID:0
X-EBAY-API-CALL-NAME:GetShippingCosts
X-EBAY-API-VERSION:863
X-EBAY-API-REQUEST-ENCODING:xml''',

    'GetSingleItem': 'https://open.api.sandbox.ebay.com/shopping',
    'json': '''X-EBAY-API-IAF-TOKEN:f'Bearer {access_token}'
X-EBAY-API-SITE-ID:0
X-EBAY-API-CALL-NAME:GetSingleItem
X-EBAY-API-VERSION:863
X-EBAY-API-REQUEST-ENCODING:xml''',

    'GetUserProfile': 'https://open.api.sandbox.ebay.com/shopping',
    'json': '''X-EBAY-API-IAF-TOKEN:f'Bearer {access_token}'
X-EBAY-API-SITE-ID:0
X-EBAY-API-CALL-NAME:GetUserProfile
X-EBAY-API-VERSION:863
X-EBAY-API-REQUEST-ENCODING:xml''',

}

finding_api = {
    'findItemsAdvanced': 'https://svcs.sandbox.ebay.com/services/search/FindingService/v1', #as duas marketing API
    'json': '''X-EBAY-SOA-SECURITY-APPNAME:IsaaclAm-appsite-SBX-34e5ff41f-b7270287
X-EBAY-SOA-OPERATION-NAME:findItemsAdvanced''',

    'findItemsByCategory': '''https://svcs.sandbox.ebay.com/services/search/FindingService/v1''',
    'json': '''X-EBAY-SOA-SECURITY-APPNAME:IsaaclAm-appsite-SBX-34e5ff41f-b7270287
X-EBAY-SOA-OPERATION-NAME:findItemsByCategory''',

    'findItemsByKeywords': '''https://svcs.sandbox.ebay.com/services/search/FindingService/v1''',
    'json': '''X-EBAY-SOA-SECURITY-APPNAME:IsaaclAm-appsite-SBX-34e5ff41f-b7270287
X-EBAY-SOA-OPERATION-NAME:findItemsByKeywords''',

    'findItemsByProduct': '''https://svcs.sandbox.ebay.com/services/search/FindingService/v1''',
    'json': '''X-EBAY-SOA-SECURITY-APPNAME:IsaaclAm-appsite-SBX-34e5ff41f-b7270287
X-EBAY-SOA-OPERATION-NAME:findItemsByProduct''',

    'findItemsIneBayStores': '''https://svcs.sandbox.ebay.com/services/search/FindingService/v1''',
    'json': '''X-EBAY-SOA-SECURITY-APPNAME:IsaaclAm-appsite-SBX-34e5ff41f-b7270287
X-EBAY-SOA-OPERATION-NAME:findItemsIneBayStores''',

    'getHistograms': '''https://svcs.sandbox.ebay.com/services/search/FindingService/v1''',
    'json': '''X-EBAY-SOA-SECURITY-APPNAME:IsaaclAm-appsite-SBX-34e5ff41f-b7270287
X-EBAY-SOA-OPERATION-NAME:getHistograms''',

    'getSearchKeywordsRecommendation': '''https://svcs.sandbox.ebay.com/services/search/FindingService/v1''',
    'json': '''X-EBAY-SOA-SECURITY-APPNAME:IsaaclAm-appsite-SBX-34e5ff41f-b7270287
X-EBAY-SOA-OPERATION-NAME:getSearchKeywordsRecommendation''',

    'getVersion': '''https://svcs.sandbox.ebay.com/services/search/FindingService/v1''',
    'json': '''X-EBAY-SOA-SECURITY-APPNAME:IsaaclAm-appsite-SBX-34e5ff41f-b7270287
X-EBAY-SOA-OPERATION-NAME:getVersion''',


}

trading_api = {
    'AddFixedPriceItem': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:AddFixedPriceItem''',

    'AddItem': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:AddItem''',

    'AddItems': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:AddItems''',

    'AddMemberMessageAAQToPartner': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:AddMemberMessageAAQToPartner''',

    'AddMemberMessageRTQ': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:AddMemberMessageRTQ''',

    'AddMemberMessagesAAQToBidder': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:AddMemberMessagesAAQToBidder''',

    'AddOrder': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:AddOrder''',

    'AddSecondChanceItem': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:AddSecondChanceItem''',

    'AddToItemDescription': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:AddToItemDescription''',

    'AddToWatchList': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:AddToWatchList''',

    'CompleteSale': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:CompleteSale''',

    'ConfirmIdentity': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:ConfirmIdentity
X-EBAY-API-APP-NAME:IsaaclAm-appsite-SBX-34e5ff41f-b7270287
X-EBAY-API-DEV-NAME:11a9420a-9d41-4f23-8e0e-1346ae4405a5
X-EBAY-API-CERT-NAME:SBX-4e5ff41f4912-1049-4803-bf63-7eff''',

    'DeleteMyMessages': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:DeleteMyMessages''',

    'EndFixedPriceItem': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:EndFixedPriceItem''',

    'EndItem': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:EndItem''',

    'EndItems': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:EndItems''',

    'ExtendSiteHostedPictures': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:ExtendSiteHostedPictures''',

    'FetchToken': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:FetchToken
X-EBAY-API-APP-NAME:IsaaclAm-appsite-SBX-34e5ff41f-b7270287
X-EBAY-API-DEV-NAME:11a9420a-9d41-4f23-8e0e-1346ae4405a5
X-EBAY-API-CERT-NAME:SBX-4e5ff41f4912-1049-4803-bf63-7eff''',

    'GetAccount': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:GetAccount''',

    'GetAdFormatLeads': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:GetAdFormatLeads''',

    'GetAllBidders': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:GetAllBidders''',

    'GetBestOffers': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:GetBestOffers''',

    'GetBidderList': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:GetBidderList''',

    'GetCategories': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:GetCategories''',

    'GetCategoryFeatures': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:GetCategoryFeatures''',

    'GetCategoryMappings': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:GetCategoryMappings''',

    'GetChallengeToken': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:GetChallengeToken''',

    'GetClientAlertsAuthToken': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:GetClientAlertsAuthToken''',

    'GetDescriptionTemplates': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:GetDescriptionTemplates''',

    'GeteBayDetails': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:GeteBayDetails''',

    'GeteBayOfficialTime': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:GeteBayOfficialTime''',

    'GetFeedback': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:GetFeedback''',

    'GetItem': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:GetItem''',

    'GetItemsAwaitingFeedback': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:GetItemsAwaitingFeedback''',

    'GetItemShipping': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:GetItemShipping''',

    'GetMemberMessages': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:GetMemberMessages''',

    'GetMessagePreferences': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:GetMessagePreferences''',

    'GetMyeBayBuying': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:GetMyeBayBuying''',

    'GetMyeBaySelling': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:GetMyeBaySelling''',

    'GetMyMessages': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:GetMyMessages''',

    'GetNotificationPreferences': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:GetNotificationPreferences''',

    'GetNotificationsUsage': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:GetNotificationsUsage''',

    'GetOrders': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:GetOrders''',

    'GetOrderTransactions': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:GetOrderTransactions''',

    'GetSellerDashboard': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:GetSellerDashboard''',

    'GetSellerEvents': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:GetSellerEvents''',

    'GetSellerList': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:GetSellerList''',

    'GetSellerTransactions': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:GetSellerTransactions''',

    'GetSessionID': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:GetSessionID
X-EBAY-API-APP-NAME:IsaaclAm-appsite-SBX-34e5ff41f-b7270287
X-EBAY-API-DEV-NAME:11a9420a-9d41-4f23-8e0e-1346ae4405a5
X-EBAY-API-CERT-NAME:SBX-4e5ff41f4912-1049-4803-bf63-7eff''',

    'GetShippingDiscountProfiles': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:GetShippingDiscountProfiles''',

    'GetStore': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:GetStore''',

    'GetStoreCategoryUpdateStatus': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:GetStoreCategoryUpdateStatus''',

    'GetSuggestedCategories': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:GetSuggestedCategories''',

    'GetTaxTable': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:GetTaxTable''',

    'GetTokenStatus': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:GetTokenStatus
X-EBAY-API-APP-NAME:IsaaclAm-appsite-SBX-34e5ff41f-b7270287
X-EBAY-API-DEV-NAME:11a9420a-9d41-4f23-8e0e-1346ae4405a5
X-EBAY-API-CERT-NAME:SBX-4e5ff41f4912-1049-4803-bf63-7eff''',

    'GetUser': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:GetUser''',

    'GetUserContactDetails': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:GetUserContactDetails''',

    'GetUserPreferences': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:GetUserPreferences''',

    'GetVeROReasonCodeDetails': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:GetVeROReasonCodeDetails''',

    'LeaveFeedback': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:LeaveFeedback''',

    'PlaceOffer': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:PlaceOffer''',

    'RelistFixedPriceItemr': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:RelistFixedPriceItem''',

    'RelistItem': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:RelistItem''',

    'RemoveFromWatchList': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:RemoveFromWatchList''',

    'RespondToBestOffer': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:RespondToBestOffer''',

    'RespondToFeedback': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:RespondToFeedback''',

    'ReviseFixedPriceItem': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:ReviseFixedPriceItem''',

    'ReviseItem': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:ReviseItem''',

    'ReviseInventoryStatus': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:ReviseInventoryStatus''',

    'ReviseMyMessages': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:ReviseMyMessages''',

    'ReviseMyMessagesFolders': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:ReviseMyMessagesFolders''',

    'RevokeToken': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:RevokeToken
X-EBAY-API-APP-NAME:IsaaclAm-appsite-SBX-34e5ff41f-b7270287
X-EBAY-API-DEV-NAME:11a9420a-9d41-4f23-8e0e-1346ae4405a5
X-EBAY-API-CERT-NAME:SBX-4e5ff41f4912-1049-4803-bf63-7eff''',

    'SendInvoice': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:SendInvoice''',

    'SetMessagePreferences': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:SetMessagePreferences''',

    'SetNotificationPreferences': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:SetNotificationPreferences''',

    'SetShippingDiscountProfiles': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:SetShippingDiscountProfiles''',

    'SetStoreCategories': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:SetStoreCategories''',

    'SetTaxTable': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:SetTaxTable''',

    'SetUserNotes': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:SetUserNotes''',

    'SetUserPreferences': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:SetUserPreferences''',

    'UploadSiteHostedPictures': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:UploadSiteHostedPictures''',

    'ValidateChallengeInput': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:ValidateChallengeInput''',

    'ValidateTestUserRegistration': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:ValidateTestUserRegistration''',

    'VerifyAddFixedPriceItem': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:VerifyAddFixedPriceItem''',

    'VerifyAddItem': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:VerifyAddItem''',

    'VerifyAddSecondChanceItem': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:VerifyAddSecondChanceItem''',

    'VerifyRelistItem': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:VerifyRelistItem''',

    'VeROReportItems': '''https://api.sandbox.ebay.com/ws/api.dll''',
    'json': '''X-EBAY-API-SITEID:0
X-EBAY-API-COMPATIBILITY-LEVEL:967
X-EBAY-API-CALL-NAME:VeROReportItems''',



}"""