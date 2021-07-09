# ProzorroProject
____
![About](https://github.com/Alekseev0/images/blob/main/About.PNG)
____
## Search
### You may take Tender hash on prozorro.gov.ua.

![Prozorro](https://github.com/Alekseev0/images/blob/main/Prozorro.gov.ua.PNG)

____

### You may use this hash to find the tender:

![Search](https://github.com/Alekseev0/images/blob/main/TenderSearch.PNG)

____
## Profile
###  Your profile shows you all your tender history. If status of any tender in your history changes - you will receive an email about it.

![Search](https://github.com/Alekseev0/images/blob/main/Profile.PNG)

###  If you are not interested in some tender any more, you may remove this tender from your history. Then you won`t get any emails about its status
____
## Technologies and logic

This project is based on Prozorro API. When user searches for tender, service sending a request to the Prozorro API, finds tender and adds it to the database. 
To show user history, was created a model UserHistory. It saves user and tender he searched for, and then in profile shows user his tender history.
Email sending working asynchronous with help of celery. It monitors status of all tenders every midnight with crontab.
