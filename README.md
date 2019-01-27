# scrapytest
Simple test of the python Scrapy library (https://scrapy.org/), which allows you to retrieve and parse information from HTTP websites.
In this case, I built a Django application with this features:

- We store the different webpages we want to parse in a table (Media).
- We created a management command to create some test media, called `create_media`. You can run that using `python3 management.py create_media`
- This command inserts in the table 3 of the most important Spanish newspapers. The table contains the newspaper URL and the rule to get each article title.
- We created another management command called `launch_read_all`, which creates a Scrapy Spider for each webpage, and launches a Crawler.
- Each webpage in the Media table will result in a dynamic Spider type, that will read the articles titles in the page and will insert them into another table, called `Articles`

TODO:
- Allow to filter articles by a topic, received as a parameter in the command.
- Send the new articles over Slack, using the nice Slacker library (https://github.com/os/slacker)
