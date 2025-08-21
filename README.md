### `AI Agent Debt Collector`

This project is an AI-powered agent designed to create custom, friendly debt collection messages. It pulls debt information from a Google Sheet, uses a large language model to generate a custom message, and can now send these messages via WhatsApp.

-----

### **Features**

  * **Google Sheets Integration**: Connects to a specified Google Sheet to retrieve dynamic debt data.
  * **Dynamic Message Creation**: Uses the `gemini-2.5-flash` model from the Google GenAI library to create a unique, friendly, and non-confrontational debt message based on data from the sheet.
  * **WhatsApp Integration**: The project can now **send the generated messages directly to debtors via WhatsApp** using the **Evolution API**.
  * **Customizable Prompt**: The AI's system instructions and prompt can be easily modified to change the tone and content of the generated messages.

-----

### **How It Works**

The `AiAgentCardDebtCollector` class handles the core logic.

1.  The `__init__` method loads environment variables, which include API keys and spreadsheet IDs, and initializes the Google GenAI client.
2.  The `DebtsDataFromSheet` method makes a `GET` request to the Google Sheets API to fetch data from a specified range.
3.  The `AgentCreatMessage` method takes a person's name, debt description, and total price. It then uses these values to create a prompt for the Gemini model, which returns a custom message.
4.  The `if __name__ == '__main__':` block demonstrates the primary workflow: it reads data from the sheet, generates a message for each row, and then **sends the message via WhatsApp**.

-----

### **Current Status & Deployment**

The WhatsApp integration is currently running in a **Docker container on a local machine** to facilitate testing and development.

-----

### **Future Features**

  * **Error Handling and Logging**: Implement more robust error handling and logging to monitor the system's performance and diagnose issues.
  * **Scheduled Runs**: Set up automated, scheduled runs to fetch new data and send messages at regular intervals.

-----


### **Configuration**

1.  **Environment Variables**: Create a `.env` file in the project's root directory to store your sensitive information.

    ```env
    GEMINI_API_KEY=YOUT_GEMINI_API_KEY
    API_KEY=YOUR_GOOGLE_SHEETS_API_KEY
    SPREADSHEET_ID=YOUR_GOOGLE_SHEETS_ID
    EVOLUTION_API_URL=YOUR_EVOLUTION_API_URL
    EVOLUTION_API_KEY=YOUR_EVOLUTION_API_KEY
    CONFIG_SESSION_PHONE_VERSION=2.3000.1023204200
    ```

2.  **Google Sheets Setup**:

      * Ensure your Google Sheet is publicly accessible or that your API key has the necessary permissions.
      * The `sheet_range_to_read` variable in the `if __name__ == '__main__':` block uses a dynamic range based on the current month and year (e.g., `jan-25!D13:G22`). Make sure your sheet tabs and data ranges match this format.

3.  **Docker Setup**:

      * Make sure you have Docker installed and configured to run the Evolution API component.

-----


