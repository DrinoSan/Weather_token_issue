# Simple Weather checker

This is a simple composition of Api and Smart contracts to check the weather in a city.

## What does it do?
- Request weather data from openWeather API
- Check intensity of rainfall
- issue x$ if rainfall > threshold
- otherwise user has to pay x$ contribution

### Todo
1. Find Chainlink datafeed or whatever with needed data
   * If not avaiblable maybe run locale api server :/ ?
     * [x] Will use own API server. Could not find adapter on Kovan
     * [ ] Using Chainlink Alarm Clock to auto execute Contract
2. Create Token for issue
3. Create Smartcontract
   * Deposit colleteral
   * Daily update for rain fall
   * Requesting Daily/Weekly/Monthly tokens from participants
     * [ ] Will be solved with Chainlink Alarm Clock 
   * Issuing Tokens if Rainfall > threshold to all participants
     * [ ] Chainlink Alarm Clock 
4. Creating Scripts
   * Deploy
   * Basic Interaction
   * TESTING ( I bet this will be the shortest, but I try my best )
5. Creating UI
   * Absolute noob