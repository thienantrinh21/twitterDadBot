# twitterDadBot
twitterDadBot utilizes TweePy, a  python library that connects to the twitter API, to search the latest tweets for the keyword "I'm".
If "I'm" is found in a tweet, twitterDadBot will automatically tweet back saying "hello {insert everything in tweet after the word "I'm"}, my name is Dad!"

For example:
@personA tweets "I'm so hungry I could eat a horse" 

twitterDadBot tweets back @personA "Hello 'so hungry I could eat a horse', my name is Dad!"
