# Tracker Bot

Tracker Bot is a versatile chatbot that allows you to track news updates, job openings, and more. It currently supports news tracking.

## Features

- **News Tracking**: Get the latest news articles from various categories, including technology, business, entertainment, general, health, science, and sports.

- **Job Openings**: Stay updated on job openings in your desired field.

- **Customizable**: Tracker Bot is highly customizable and can be extended to support additional features and functionalities.

## Live Deployed Version

You can interact with the live deployed version of Tracker Bot at [https://bot.textbase.ai/surajkumarkarn10/tracker-bot](https://bot.textbase.ai/surajkumarkarn10/tracker-bot).


## Installation

To run Tracker Bot, follow these simple steps:

1. **Clone the Repository:**

   You can clone the Tracker Bot repository from GitHub using the following command:

   ```bash
   git clone https://github.com/surazkarn/tracker-bot
   ```

2. **Navigate to the project folder:**

   ```bash
   cd tracker-bot
   ```

3. **Obtain News API Key**

- To fetch news articles, Tracker Bot relies on the News API. You need to obtain a News API key from [News API](https://newsapi.org/). Once you have your API key, follow the steps below to set it up in Tracker Bot.

   - Replace the `NEWS_API_KEY` in the `main.py` file with your actual News API key from [News API](https://newsapi.org/).

4. **Install Dependencies:**

   Make sure you have Python and `pip` installed. Then, install the required dependencies using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

   This will install the `textbase-client` package and other necessary dependencies.

5. **Run the Bot:**

   Start the bot with the following command:

   ```bash
   textbase-client test
   ```

   When prompted, provide the path to the `main.py` file:

   ```
   Path to the main.py file: main.py
   ```

   Your Tracker Bot will start, and you can interact with it to get news updates or engage in conversations.

## Usage

To get the latest news, type the following command when interacting with Your Bot:

```
!news [category]
```

Replace `[category]` with the desired news category (e.g., technology, business, entertainment, general, health, science, sports).

For job openings, use a similar command (e.g., `!jobs [category]`) to fetch the latest job listings in your field.

## Contributions

Contributions to this Bot are welcome! If you have suggestions or want to improve its functionality, please open an issue or create a pull request on the GitHub repository.

## License

This project is licensed under the [MIT License](LICENSE).

Happy chatting with Tracker Bot!