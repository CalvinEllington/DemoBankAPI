# DemoBankAPI

This app requires curl. To use this app, visit the following url. You will be prompted to make some accounts.
Below are some templates for the curl commands, depending on your system they might be different.

//Initial User Creation
curl http://127.0.0.1:5000/

//Add an account
curl -X POST -H "Content-Type: application/json" -d '{"name": "Main Account"}'  http://127.0.0.1:5000/accounts/new_ac

//Add a transaction. Replace accountid with the account desired. Negatives represent withdrawals.
curl -X POST -H "Content-Type: application/json" -d '{"amount": 10000}'  http://127.0.0.1:5000/accounts/accountid/tx/new

//JSON Endpoints. Replace txid and accountid with the desired accounts/transactions
Account
curl http://127.0.0.1:5000/accounts/accountid/JSON

All transactions for a specific account
curl http://127.0.0.1:5000/accounts/accountid/tx/JSON

Specific transaction information
curl http://127.0.0.1:5000/accounts/accountid/tx/txid/JSON

//Reset application
curl http://127.0.0.1:5000/reset
