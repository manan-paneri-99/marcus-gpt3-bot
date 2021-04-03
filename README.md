# marcus-gpt3-bot

Marcus is a GPT-3 based travel guide chatbot that give you friendly and creative travel suggestions

Here are some examples:
1. Where to chill in Las Vegas?
  ```python
  >>> from chatbot import ask, append_interaction_to_chat_log
  >>> chat_log = None
  >>> question_greet ="Hey how are you?"
  >>> answer_greet = ask(question_greet, chat_log)
  >>> answer_greet
  'I am informative, creative — and more. I can be an excellent travel guide for you.'
  >>> question = "Where can I chill in Las Vegas?"
  >>> answer = ask(question, chat_log)
  >>> answer
  'You can chill at Las Vegas Strip, or catch a show at Bellagio.'
  ```
2. Cool places in Singapore!?
  ```python
  question_1 = "What are some cool places in Singapore?"
  >>> answer_1 = ask(question_1, chat_log)
  >>> answer_1
  "You can take a food trail in Pinang Peranakan and learn about Singapore's culture."
  ```
3. As random as Beirut?
  ```
  question = "What can I do in Beirut?"
  >>> answer = ask(question, chat_log)
  >>> answer
  'The city has various landmarks like the Mediterranean Sea, Ottoman Bank, Corniche Beirut and others.
  I hope you liked your conversation with me. For more inspiring travel    destinations, keep visiting Marcus.ai'
  ```
  
 Beta version of Twilio SMS deployment is also available. Stay tuned!
 
 Sources:
 * [OpenAI Documentation](https://beta.openai.com/docs/introduction)
 * [Twilio blog](https://www.twilio.com/blog/openai-gpt-3-chatbot-python-twilio-sms)
 
 Maintained by **[Manan Paneri](github.com/manan-paneri-99)**
  
