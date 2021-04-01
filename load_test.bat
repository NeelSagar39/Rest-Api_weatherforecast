@echo off
set API_list[0]=http://3.82.248.105/get-temp-predictions
set API_list[1]=http://3.82.248.105/get-rainfall-predictions
set API_list[2]=http://3.82.248.105/get-humidity-predictions
set API_list[3]=http://3.82.248.105/get-wind-predictions
set API_list[4]=http://3.82.248.105/get-cloudy-predictions
set API_list[5]=http://3.82.248.105/get-temp-weekly
set API_list[6]=http://3.82.248.105/get-rain-weekly
set API_list[7]=http://3.82.248.105/get-humidity-weekly
set API_list[8]=http://3.82.248.105/get-cloud-weekly
set API_list[9]=http://3.82.248.105/get-wind-weekly
set API_amount=0
:SymLoop 
if defined API_list[%API_amount%] ( 
   set /a "API_amount+=1"
   GOTO :SymLoop 
)
call echo API_amount= %API_amount%
@REM pick one function from "get prediction" and "get weekly data"
set get_prediction_test=http://3.82.248.105/get-humidity-predictions
set get_weekly_test=http://3.82.248.105/get-humidity-weekly
call ab -n 1000 -c 100 -g ./1000_100_Predictions.dat %get_prediction_test%
call ab -n 1000 -c 100 -g ./1000_100_weekly.dat %get_weekly_test%
pause
