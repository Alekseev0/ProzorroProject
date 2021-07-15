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

____
### How to run the project

## 1. Email settings:
In ProzorroPlatform/settings_constants.py you need to set up settings for email sending. Gmail account, that will send emails and password. Then you have to do the next steps in your gmail account:

Click on "Manage your account"
![Search](https://res.cloudinary.com/practicaldev/image/fetch/s--fE1hYfre--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://snipboard.io/L58jDC.jpg)

Then click on "Security tab"
![Search](https://res.cloudinary.com/practicaldev/image/fetch/s--ZlEawP28--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://lh3.googleusercontent.com/pw/ACtC-3e_6aPStbMIv0ANp4Iu6OMfDlwZKfWxKUjyqb_REB5m3dCrtG3jAsMaGZ013K8M5jMy3crB9FtoR7Il54aBh7kcM8RqJed6gDIHfFSWxbYeJfC7NXbihFby3fp2Vkw7cJQyeF0m-dJKQgMScsPXoH5h%3Dw1888-h861-no%3Fauthuser%3D0)

Enable two steps verification
![Search](https://res.cloudinary.com/practicaldev/image/fetch/s--9JGiAb33--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://lh3.googleusercontent.com/pw/ACtC-3eWoQjfXlmn1lYATXGi8KKOAoslgdvuK6pXA1VmerWuQWl46ELbqQ4OrpjGdQxVwqWfjnnKMYSYTYtwwxRAU3H266JyOxZ6aH3Srhp33lHregF5GoV-ZWxnoR4WguJtAiavzTvIM_Xxr2EgLpXEae1g%3Dw1913-h867-no%3Fauthuser%3D0)


Now click on App passwords
![Search](https://res.cloudinary.com/practicaldev/image/fetch/s--zHFKbsT3--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://lh3.googleusercontent.com/pw/ACtC-3dMYd_TZpn5IbXTP2YgX6cGcGR-PgY5MXSNugjMn-MNfwzLV-78-ZdGzJhfN4YXN4zX2M7VSRMD9eZCPNnItFik3akf6D7CObjRFGY8M_VPIVkkkEmoCu7-h1Xs8LRuDNG97AYZzM8H_Ylst9CE_4pK%3Dw1913-h867-no%3Fauthuser%3D0)

Click on select app choose "other(Custom Name)" and give a name to your app
![Search](https://res.cloudinary.com/practicaldev/image/fetch/s--z4ZHmmg0--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://lh3.googleusercontent.com/pw/ACtC-3c-yMkJ2aq5EER9h7BEuN5-TpwPN1OlNKppFhP0uyOjRfcNMtLX0-MflzIKxkbG0-DCnGF7mWMBeVLjni1y9k_KWyLBYexHiriP3rAxol2Q_tu5Zv5ZVfG1sOkxViQOCr9UlNZf__1p73TiYhBGCi_-%3Dw1916-h866-no%3Fauthuser%3D0)

The last step is to click on generate and Gmail will generate a key or an app password. Make sure to copy this key or save it in a text file
![Search](https://res.cloudinary.com/practicaldev/image/fetch/s--Od2oNBNn--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://lh3.googleusercontent.com/pw/ACtC-3cch9URVsSAod-iG5bYAr4eitVATszD4mQkDXSuJEKfEkB587rrhKT409WahJTbYRH8Oz6_6EL4B_Jbhb6q70vRVDnn8Rqht2nkn0EgQfzr6usptPsXf4wnhjPV-XU2qgumfxRCs3mLNGFCYMkVYyGW%3Dw1916-h866-no%3Fauthuser%3D0)

Then just add it to EMAIL_PASSWORD in settings_constants


## 2. Database settings:

https://www.2ndquadrant.com/en/blog/pginstaller-install-postgresql/ - an example of installing database. After it you need to add all settings into ProzorroPlatform/settings_constants.py(Name, user, password, host and port)

## 3. Celery settings:

For this project I used RabbitMQ as message broker. How to install it you can read here: https://www.rabbitmq.com/download.html


If you want to use other message broker, you may read it: https://docs.celeryproject.org/en/stable/getting-started/first-steps-with-celery.html#celerytut-broker


To choose your timezone you may use the next link: https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568. Then add it to CELERY_TIMEZONE in ProzorroPlatform/settings_constants.py

To start celery you shoul open Terminal and enter the next:


'$ Celery -A ProzorroPlatform worker -l INFO'


And this:

```
Celery -A ProzorroPlatform beat -l INFO
```


If you use Windows, you should enter this:


  $ Celery -A ProzorroPlatform worker -l INFO --pool=solo





```
if (isAwesome){
  return true
}
```







