# Budget
This is a tool I'm working on to help me analyze my bank activity statements. 

I wanted a way to automate the process of associating a particular expense with a category (starbucks -> coffee, kroger -> grocery, etc). This is what the `categorizer` module does: it looks for activity with no recognizable keywords and asks the user where it belongs.

The purpose of the `summarizer` module is to then look at the activity and add up the total expenses for each category.