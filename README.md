# DemoBankAPI

This app requires curl. To use this app, visit the following url. You will be prompted to make some accounts.
Below are some templates for the curl commands, depending on your system they might be different.

//Initial User Creation  <br>
`curl http://7fa18a5e.ngrok.io/` <br>

//Add an account  <br>
`curl -X POST -H "Content-Type: application/json" -d '{"name": "Main Account"}'  http://7fa18a5e.ngrok.io/accounts/new_ac`  <br>

//Add a transaction. Replace accountid with the account desired. Negatives represent withdrawals.   <br>
`curl -X POST -H "Content-Type: application/json" -d '{"amount": 10000}'  http://7fa18a5e.ngrok.io/accounts/accountid/tx/new`  <br>
`curl -X POST -H "Content-Type: application/json" -d '{"amount": -789}'  http://7fa18a5e.ngrok.io/accounts/accountid/tx/new`  <br>

//JSON Endpoints. Replace txid and accountid with the desired accounts/transactions <br>
Account <br>
`curl http://7fa18a5e.ngrok.io/accounts/accountid/JSON` <br>
 <br>
All transactions for a specific account <br>
`curl http://7fa18a5e.ngrok.io/accounts/accountid/tx/JSON` <br>
 <br>
Specific transaction information <br>
`curl http://7fa18a5e.ngrok.io/accounts/accountid/tx/txid/JSON` <br>
 <br>
//Reset application  <br>
`curl http://7fa18a5e.ngrok.io/reset`  <br>
<br>


If you follow along with each command below, you will be exposed to the different functionality of the app. Comments welcome!
```
curl http://7fa18a5e.ngrok.io/
curl -X POST -H "Content-Type: application/json" -d '{"name": "Main Account"}'  http://7fa18a5e.ngrok.io/accounts/new_ac
curl -X POST -H "Content-Type: application/json" -d '{"amount": 10000}'  http://7fa18a5e.ngrok.io/accounts/accountid/tx/new
curl -X POST -H "Content-Type: application/json" -d '{"amount": -789}'  http://7fa18a5e.ngrok.io/accounts/accountid/tx/new
curl http://7fa18a5e.ngrok.io/accounts/accountid/JSON
curl http://7fa18a5e.ngrok.io/accounts/accountid/tx/JSON
curl http://7fa18a5e.ngrok.io/accounts/accountid/tx/txid/JSON
curl http://7fa18a5e.ngrok.io/
curl http://7fa18a5e.ngrok.io/reset```
